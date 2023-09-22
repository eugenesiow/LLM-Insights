### LLaMA

- Pre-normalization: RMSNorm
- Activation function: SwiGLU, dimension of (2/3*4d) instead of 4d
- Position Embeddings: RoPE (Rotary Positional Embeddings)
- Optimizer: AdamW, beta_1 = 0.9, beta_2 = 0.95
- LR Scheduler: Cosine, final learning rate is equal to 10% of the max learning rate
- Weight Decay: 0.1
- Gradient Clipping: 1.0
- Warmup steps: 2000


|   Params   | Dimension | N Heads | N Layers | Learning Rate | Batch Size | N Tokens |
|:----------:|:---------:|:-------:|:--------:|:-------------:|:----------:|:--------:|
|   6.7B    |   4096    |   32    |    32    |     3.0e-4    |     4M     |   1.0T   |
|   13.0B   |   5120    |   40    |    40    |     3.0e-4    |     4M     |   1.0T   |
|   32.5B   |   6656    |   52    |    60    |     1.5e-4    |     4M     |   1.4T   |
|   65.2B   |   8192    |   64    |    80    |     1.5e-4    |     4M     |   1.4T   |

