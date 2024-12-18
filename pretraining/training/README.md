# Training

## Terms

We tend to run into lots of training jargon so here's a glossary of terms.

- MFU: Model Flops Utilization - ratio of the observed throughput to the theoretical maximum throughput if the benchmarked hardware setup were operating at peak FLOPS with no memory or communication overhead [1], or more succinctly how efficiently, usually a percentage, we are using our GPUs.
- MBS: Micro Batch Size - refers to the batch size per gpu, we kind of want to tweak this to as large as possible without running OOM (out-of-memory) as it affects our MFU.
- GBS: Global Batch Size - refers to the total batch size per iteration and may include gradient accumulation, for pre-training its pretty large (e.g. 1024 or 2048).
- GAS: Gradient Accumulation Steps - how many forward/backward cycles to perform before one full iteration is complete.

## Memory

Weights have to be loaded into the GPU memory of each GPU. We also have to load two other large sets into memory, gradients, which have a 1:1 ratio with weights, and optimizer state, if you’re using Adam its about 3 times the size of our weights (individual adaptive learning rates and estimates of first and second moments of the gradients). So if we’re doing FP32 training, each parameter/weight is 4 bytes (floating point 32 bits is equal to 4 bytes as 1 byte is 8 bits). So if we’re training a 7 billion parameter model, that’s about 28GB weights, 28GB gradients and 84GB optimizer states, a whopping 140GB in total.

## Parallelization

In pre-training we need to scale beyond a single node to multiple nodes with network between them, how we distribute and parallelize this training is essential (both time and memory constrained). See the dedicated [parallelization](parallelization/README.md) section for more information on the various techniques.

## Gradient Accumulation

Gradient accumulation is a way to virtually increase the batch size (simulate a larger batch size) during training, which is very useful when the available GPU memory is insufficient to accommodate the desired batch size. In gradient accumulation, gradients are computed for smaller batches and accumulated (usually summed or averaged) over multiple iterations instead of updating the model weights after every batch. Once the accumulated gradients reach the target "virtual" batch size, the model weights are updated with the accumulated gradients [2].

## Hyperparameters

### Learning Rate and Scheduling

Learning rate is a critical hyperparameter for pre-training LLMs and a [scheduler](SCHEDULER.md) implements some scheduling strategy to dynamically adhyst the learning rate accordingly during the training run. During the start of training a large learning rate can quickly update parameters, potentially overshooting the optimal solution and causing instability, hence, warmup to increase the learning rate gradually is sometimes done. As the model continues to train, a smaller learning rate is usually desireable to avoid overfitting and prevent forgetting.

## References
1. [Reiner Pope, Sholto Douglas, Aakanksha Chowdhery, Jacob Devlin, James Bradbury, Anselm Levskaya, Jonathan Heek, Kefan Xiao, Shivani Agrawal, & Jeff Dean. (2022). Efficiently Scaling Transformer Inference.](https://arxiv.org/abs/2211.05102)
2. [Sebastian Raschka. (Mar 2023). Finetuning LLMs on a Single GPU Using Gradient Accumulation](https://lightning.ai/blog/gradient-accumulation/)