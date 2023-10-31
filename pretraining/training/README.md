# Training

## Terms

We tend to run into lots of training jargon so here's a glossary of terms.

- MFU: Model Flops Utilization - ratio of the observed throughput to the theoretical maximum throughput if the benchmarked hardware setup were operating at peak FLOPS with no memory or communication overhead [1], or more succinctly how efficiently, usually a percentage, we are using our GPUs.
- MBS: Micro Batch Size - refers to the batch size per gpu, we kind of want to tweak this to as large as possible without running OOM (out-of-memory) as it affects our MFU.
- GBS: Global Batch Size - refers to the total batch size per iteration and may include gradient accumulation, for pre-training its pretty large (e.g. 1024 or 2048).
- GAS: Gradient Accumulation Steps - how many forward/backward cycles to perform before one full iteration is complete.

## Gradient Accumulation

Gradient accumulation is a way to virtually increase the batch size (simulate a larger batch size) during training, which is very useful when the available GPU memory is insufficient to accommodate the desired batch size. In gradient accumulation, gradients are computed for smaller batches and accumulated (usually summed or averaged) over multiple iterations instead of updating the model weights after every batch. Once the accumulated gradients reach the target "virtual" batch size, the model weights are updated with the accumulated gradients [2].

## References
1. [Reiner Pope, Sholto Douglas, Aakanksha Chowdhery, Jacob Devlin, James Bradbury, Anselm Levskaya, Jonathan Heek, Kefan Xiao, Shivani Agrawal, & Jeff Dean. (2022). Efficiently Scaling Transformer Inference.](https://arxiv.org/abs/2211.05102)
2. [Sebastian Raschka. (Mar 2023). Finetuning LLMs on a Single GPU Using Gradient Accumulation](https://lightning.ai/blog/gradient-accumulation/)