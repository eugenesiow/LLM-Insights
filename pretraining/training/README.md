# Training

## Glossary

We tend to run into lots of training jargon so here's a glossary.

- MFU: Model Flops Utilization - ratio of the observed throughput to the theoretical maximum throughput if the benchmarked hardware setup were operating at peak FLOPS with no memory or communication overhead [1].
- MBS: Micro Batch Size - refers to the batch size per gpu.
- GBS: Global Batch Size - refers to the total batch size per iteration and may include gradient accumulation.
- GAS: Gradient Accumulation Steps - how many forward/backward cycles to perform before one full iteration is complete.

## References
1. [Reiner Pope, Sholto Douglas, Aakanksha Chowdhery, Jacob Devlin, James Bradbury, Anselm Levskaya, Jonathan Heek, Kefan Xiao, Shivani Agrawal, & Jeff Dean. (2022). Efficiently Scaling Transformer Inference.](https://arxiv.org/abs/2211.05102)