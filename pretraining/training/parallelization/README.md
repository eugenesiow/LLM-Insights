# Parallelization

LLMs impose extreme memory requirements. Storing the model parameters, gradients, and optimizer states for even moderately sized models can easily exceed the memory capacity of a single high-end GPU. For instance, a 7B model requires approximately 112GB for its states, surpassing the 80GB capacity of an NVIDIA A100 GPU. Training a trillion-parameter model necessitates terabytes of memory (estimated 24TB). This "memory wall" makes it impossible to train large models on a single device.

To overcome these memory and computational barriers, distributed training using various parallelism techniquesallows the distribution of the model's memory footprint and computational workload across multiple GPUs, enabling the training of models that would otherwise be intractable.

## Parallelism Strategies

1. [**Data Parallelism (DP)**](#data-parallelism-dp): Replicates the model on multiple GPUs and processes different subsets of the input data on each replica.   
2. [**Tensor Parallelism (TP)**](#tensor-parallelism-tp): Splits individual tensors or layers (intra-layer parallelism) within the model across multiple GPUs.   
3. [**Pipeline Parallelism (PP)**](#pipeline-parallelism-pp): Partitions the model's layers sequentially into stages (inter-layer parallelism) distributed across GPUs, processing micro-batches in a pipelined fashion.   
4. [**Sequence Parallelism (SP) / Context Parallelism (CP)**](#sequence-and-context-parallelism-spcp): Partitions the input sequence length across GPUs, primarily to handle the memory demands of long contexts in attention mechanisms.   
5. [**Expert Parallelism (EP)**](#expert-parallelism-ep-for-moe): Specifically designed for Mixture-of-Experts (MoE) models, distributing different "expert" sub-networks across GPUs.

### Data Parallelism (DP)

The core principle of DP is model replication combined with data splitting. The entire LLM, including all its parameters, is duplicated onto each participating GPU (often referred to as a worker or rank) in the training cluster. The global training mini-batch is then divided into smaller micro-batches, and each GPU receives a distinct micro-batch to process. Each GPU independently performs the forward pass (calculating predictions and loss) and the backward pass (calculating gradients) using its local data micro-batch and its local copy of the model.

### Tensor Parallelism (TP)

Instead of replicating the entire model, TP splits the weight matrices and activations of individual layers (like linear layers or attention mechanisms) across a group of GPUs. Each GPU in the TP group holds only a slice of the parameters and performs computations on a corresponding slice of the activations. This allows the aggregate memory of the TP group to accommodate very large layers. 

Nvidia's Megatron-LM framework provides a strategy for applying TP to Transformer layers:

* **MLP Layers:** Transformer MLP blocks typically consist of two linear layers often separated by a non-linearity like GeLU. Megatron-LM parallelizes the first linear layer's weight matrix ($A$) column-wise across the TP GPUs ($A = [A_1, A_2, ..., A_N]$). The input activation ($X$) is broadcast to all GPUs. Each GPU computes $XA_i$. The subsequent GeLU activation can be applied independently on each GPU's result ($Y_i = \text{GeLU}(XA_i)$), avoiding communication before the non-linearity. The second linear layer's weight matrix ($B$) is partitioned row-wise ($B^T$). Each GPU computes $Y_i B_i$. The final output requires summing the partial results from all GPUs, which is accomplished using an All-Reduce communication operation across the TP group.

* **Attention Layers:** The multi-head attention mechanism is inherently parallelizable. The projection matrices for Query (Q), Key (K), and Value (V) are partitioned column-wise, effectively assigning different attention heads (or parts of heads) to different GPUs. Each GPU computes attention for its subset of heads locally. The output projection layer, which combines the results from the heads, is then partitioned row-wise. Similar to the MLP, an All-Reduce is required after the output projection to combine the partial results.

* **Embedding Layer:** For models with large vocabularies, the embedding table can be a significant memory consumer. Megatron-LM parallelizes the input embedding table column-wise along the vocabulary dimension. After the embedding lookup, an All-Reduce is needed because each GPU only has the embeddings for a fraction of the vocabulary. For the output layer (which projects hidden states back to vocabulary size), instead of gathering the full logits (which would involve communicating a very large tensor), Megatron-LM fuses the final linear layer's computation with the cross-entropy loss calculation. This optimization significantly reduces communication, as only the scalar loss values need to be aggregated across the TP group.

TP relies heavily on collective communication operations, primarily All-Reduce, to synchronize the partial results computed on each GPU within the TP group. These operations occur frequently, typically within every Transformer layer during both the forward and backward passes. This high frequency of communication makes TP extremely sensitive to the bandwidth and latency of the interconnect between GPUs.   

Consequently, TP performs best when implemented within a single node where GPUs are connected via high-speed interconnects like NVIDIA's NVLink or NVSwitch, which offer hundreds of GB/s bandwidth. Attempting to perform TP across nodes connected by slower network links (e.g., InfiniBand or Ethernet), while possible, typically results in significant performance degradation due to increased communication latency and lower bandwidth. Techniques exist to overlap TP communication (All-Reduce, or its components All-Gather and Reduce-Scatter ) with computation (GEMMs) to mitigate latency, often involving careful scheduling and kernel fusion.

### Pipeline Parallelism (PP)

In PP, the sequence of layers comprising the LLM is divided into multiple contiguous segments called stages. Each stage, consisting of one or more layers, is assigned to a specific GPU or a group of GPUs (which might themselves be using TP). To enable concurrent processing across these stages and improve hardware utilization, the training mini-batch is further subdivided into smaller micro-batches. These micro-batches flow through the pipeline stages sequentially, akin to an assembly line. As soon as a stage finishes processing a micro-batch, it passes the resulting activations to the next stage and immediately begins working on the subsequent micro-batch. 

### Sequence and Context Parallelism (SP/CP)

The core idea of SP/CP is to partition the input tensors (activations) along the sequence length dimension and distribute these chunks across multiple GPUs. Each GPU in the SP/CP group is responsible for processing only a segment of the full sequence. This distribution directly reduces the activation memory footprint on each individual GPU  and allows for the distributed storage of the potentially massive KV cache required for long contexts.

### Expert Parallelism (EP for MoE)

Expert Parallelism is a specialized technique tailored specifically for training and deploying Mixture-of-Experts (MoE) models. While MoE reduces computation per token, the total number of parameters across all experts in an MoE layer can be substantial, often making it impossible to fit all experts onto a single GPU. Expert Parallelism (EP) addresses this by distributing the experts across multiple GPUs within a parallel group. Each GPU becomes responsible for storing the parameters and performing the computations for only a subset of the total experts in a layer. For example, with 8 experts and 4 GPUs using EP, each GPU might hold 2 experts.

EP necessitates communication to route tokens to the correct experts residing on potentially different GPUs. The typical communication flow involves two main steps using the All-to-All collective operation:

* **Token Dispatch (Permute Send):**  After the gating network on each GPU determines the target expert(s) for its local tokens, an All-to-All communication is performed. Each GPU sends tokens destined for experts on other GPUs and receives tokens that are assigned to its locally hosted experts. This effectively permutes the tokens across the GPUs according to the routing decisions. 
* **Result Gathering (Permute Receive):** Once each GPU has processed the tokens received in the first step using its local experts, a second All-to-All communication is performed. This operation sends the computed expert outputs back to the GPUs where the corresponding tokens originated, effectively reversing the permutation from the first step. The results are then combined on the originating GPU to produce the final output of the MoE layer. 

## ZeRo

Closely related to these are memory optimization techniques that operate within the data-parallel paradigm, such as the [Zero Redundancy Optimizer (ZeRO)](https://arxiv.org/abs/1910.02054) and Fully Sharded Data Parallel (FSDP), which partition model states (parameters, gradients, optimizer states) across data-parallel (DP) workers to drastically reduce memory redundancy.

### Communication

In ZeRo, given M parameters,
- in the forward pass we need to do all-gather to collect M parameters,
- in the backward pass we need to do all-gather to re-collect M parameters then each GPU can calculate local gradients, 
- also in the backward pass, we then need to do a reduce-scatter function to aggregate and redistribute gradients (of size M parameters) across all GPUs.
- Hence, there is a total of 3M communication per M weights.
- This gives a model-to-communications ratio of 1:3.

[ZeRo++](https://arxiv.org/abs/2306.10209) reduces this from 1:0.75 or for M parameters, only 0.75M communications over the forward and backward passes.