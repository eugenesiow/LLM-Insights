# Model Architecture

## Dense Models

### Llama 1,2,3

The Llama 1/2/3 architecture, which is a pretty standard decoder-only transformer architecture (quite similar to GPT) and is shown in the diagram below:

![Llama architecture](./figures/llama_architecture_dark.svg#gh-dark-mode-only)
![Llama architecture](./figures/llama_architecture.svg#gh-light-mode-only)

The input sequence is sent into this architecture during inference, and passes through the following blocks:

1. **Embeddings.** In this layer, the input tokens are converted into dense vector representations called embeddings. Each unique token in the vocabulary is mapped to a fixed-size vector which captures some semantic and syntactic information about the token.
2. **Transformer Block.** This is the fundamental building block of the Llama architecture. It is repeated multiple times and forms the "deep" part of this transformer architecture.
    - **RMSNorm (Root Mean Square Layer Normalization).** This is a normalization technique applied before the Attention and FFN sub-layers. It normalizes the input features by dividing by the root mean square of the feature values. RMSNorm helps to stabilize the training process and allows for the use of larger learning rates.
    - **Attention.** This is the core mechanism that allows the model to weigh the importance of different parts of the input sequence when processing a specific token. It computes a weighted sum of the input embeddings, where the weights are determined by the relevance of other tokens to the current token. The specific attention mechanism in Llama 1 and 2 models is [Multi-Head Attention (MHA)](./attention.md), allowing the model to attend to different aspects of the input simultaneously. Llama 3 models, along with the largest 70B parameter class model in Llama 2, use [Grouped-Query Attention (GQA)](./attention.md).
    - **⊕.** This is a skip connection. The output of the Attention and Feed-Forward Network (FFN) sub-layers are added to the original input (after it has been processed by the initial RMSNorm). This skip connection helps to mitigate the vanishing gradient problem in deep networks, allowing for the training of deeper models.
    - **FFN (Feed-Forward Network).** This is a two-layer Multi-Layer Perceptron (MLP) with a non-linear activation function. The FFN helps the model to learn non-linear transformations of the representations.
3. **RMSNorm.** After passing through multiple Transformer Blocks, the final sequence of processed embeddings is passed through one last RMSNorm layer. This normalization step helps to stabilize the final representations before they are fed into the linear layer.
4. **Linear.** A linear fully connected transformation layer that maps the high-dimensional processed embeddings to the vocabulary size. The output of this layer contains logits (roughly corresponds to the probability of the token in the vocabulary given the input sequence) for each token in the vocabulary.
5. **Softmax.** The softmax function is applied to the logits from the linear layer coverting them into a probability distribution over the vocabulary.

|   Model Name   | Sizes | N Tokens | Context Length | Global​ Batch Size​ | Embedding Type​ | Attention Type​ | Dimension | N Heads | N Layers | Learning Rate | Optimizer | Activation Function​ |
|:----------:|:---------:|:-------:|:--------:|:-------------:|:----------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
|   [LLaMA](llama.md)        |   6.7B<br/>13.0B<br/>32.5B<br/>65.2B    |   1.0T<br/>1.0T<br/>1.4T<br/>1.4T<br/>    |    2048    |     1024    |     RoPE     |   MHA   | 4096​<br/>5120​<br/>6656​<br/>8192​ | 32<br/>40<br/>52<br/>64 | 32<br/>40<br/>60<br/>64 | 3.0e-4<br/>3.0e-4<br/>1.5e-4<br/>1.5e-4 | AdamW​<br/>β1 = 0.9, β2 = 0.95<br/>ε = 10−5<br/>wd=0.1<br/>gc=0.1​ | SwiGLU |
|   [LLaMA-2](llama2.md)        |   7B<br/>13B<br/>34B<br/>70B    |   2.0T<br/>2.0T<br/>2.0T<br/>2.0T<br/>    |    4096    |     1024    |     RoPE     |   MQA<br/>MQA<br/>GQA<br/>GQA   | 4096​<br/>5120​<br/>8192<br/>8192​ | 32<br/>40<br/>64<br/>64 | 32<br/>40<br/>48<br/>64 | 3.0e-4<br/>3.0e-4<br/>1.5e-4<br/>1.5e-4 | AdamW​<br/>β1 = 0.9, β2 = 0.95<br/>ε = 10−5<br/>wd=0.1<br/>gc=0.1​ | SwiGLU |
|   [LLaMA-3](llama3.md)        |   8B<br/>70B    |   15.0T<br/>15.0T    |    8192    |     ?    |     RoPE     |   GQA<br/>GQA   | ?​<br/>? | ?<br/>? | ?<br/>? | ?<br/>? | AdamW​<br/>? | SwiGLU |

## Mixture of Experts (MoEs)

1. [Mixture of Expert (MoE) Models](../moe/)
2. [Sparse Upcycling MoE Models](../moe/upcycling.md)