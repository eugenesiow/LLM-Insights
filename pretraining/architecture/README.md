# Model Architecture

### LLaMA

```
LlamaForCausalLM(
  (model): LlamaModel(
    (embed_tokens): Embedding(32000, 4096, padding_idx=0)
    (layers): ModuleList(
      (0-31): 32 x LlamaDecoderLayer(
        (self_attn): LlamaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (v_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (rotary_emb): LlamaRotaryEmbedding()
        )
        (mlp): LlamaMLP(
          (gate_proj): Linear(in_features=4096, out_features=11008, bias=False)
          (down_proj): Linear(in_features=11008, out_features=4096, bias=False)
          (up_proj): Linear(in_features=4096, out_features=11008, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): LlamaRMSNorm()
        (post_attention_layernorm): LlamaRMSNorm()
      )
    )
    (norm): LlamaRMSNorm()
  )
  (lm_head): Linear(in_features=4096, out_features=32000, bias=False)
)
```

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