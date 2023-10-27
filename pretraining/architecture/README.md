# Model Architecture

|   Model Name   | Sizes | N Tokens | Context Length | Global​ Batch Size​ | Embedding Type​ | Attention Type​ | Dimension | N Heads | N Layers | Learning Rate | Optimizer | Activation Function​ |
|:----------:|:---------:|:-------:|:--------:|:-------------:|:----------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
|   [LLaMA](LLAMA.md)        |   6.7B<br/>13.0B<br/>32.5B<br/>65.2B    |   1.0T<br/>1.0T<br/>1.4T<br/>1.4T<br/>    |    2048    |     1024    |     RoPE     |   MHA   | 4096​<br/>5120​<br/>6656​<br/>8192​ | 32<br/>40<br/>52<br/>64 | 32<br/>40<br/>60<br/>64 | 3.0e-4<br/>3.0e-4<br/>1.5e-4<br/>1.5e-4 | AdamW​<br/>β1 = 0.9, β2 = 0.95<br/>ε = 10−5<br/>wd=0.1<br/>gc=0.1​ | SwiGLU |
|   [LLaMA-2](LLAMA2.md)        |   7B<br/>13B<br/>34B<br/>70B    |   2.0T<br/>2.0T<br/>2.0T<br/>2.0T<br/>    |    4096    |     1024    |     RoPE     |   MQA<br/>MQA<br/>GQA<br/>GQA   | 4096​<br/>5120​<br/>8192<br/>8192​ | 32<br/>40<br/>64<br/>64 | 32<br/>40<br/>48<br/>64 | 3.0e-4<br/>3.0e-4<br/>1.5e-4<br/>1.5e-4 | AdamW​<br/>β1 = 0.9, β2 = 0.95<br/>ε = 10−5<br/>wd=0.1<br/>gc=0.1​ | SwiGLU |
