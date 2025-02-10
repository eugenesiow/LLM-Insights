# Deepseek V3

Deepseek V3 is a [Mixture of Experts](../moe/MoE.md) model. 

```
DeepseekV3Config {
  "_name_or_path": "deepseek-ai/DeepSeek-V3",
  "architectures": [
    "DeepseekV3ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "auto_map": {
    "AutoConfig": "deepseek-ai/DeepSeek-V3--configuration_deepseek.DeepseekV3Config",
    "AutoModel": "deepseek-ai/DeepSeek-V3--modeling_deepseek.DeepseekV3Model",
    "AutoModelForCausalLM": "deepseek-ai/DeepSeek-V3--modeling_deepseek.DeepseekV3ForCausalLM"
  },
  "aux_loss_alpha": 0.001,
  "bos_token_id": 0,
  "eos_token_id": 1,
  "ep_size": 1,
  "first_k_dense_replace": 3,
  "hidden_act": "silu",
  "hidden_size": 7168,
  "initializer_range": 0.02,
  "intermediate_size": 18432,
  "kv_lora_rank": 512,
  "max_position_embeddings": 163840,
  "model_type": "deepseek_v3",
  "moe_intermediate_size": 2048,
  "moe_layer_freq": 1,
  "n_group": 8,
  "n_routed_experts": 256,
  "n_shared_experts": 1,
  "norm_topk_prob": true,
  "num_attention_heads": 128,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 61,
  "num_key_value_heads": 128,
  "num_nextn_predict_layers": 1,
  "pretraining_tp": 1,
  "q_lora_rank": 1536,
  "qk_nope_head_dim": 128,
  "qk_rope_head_dim": 64,
  "quantization_config": {
    "activation_scheme": "dynamic",
    "fmt": "e4m3",
    "quant_method": "fp8",
    "weight_block_size": [
      128,
      128
    ]
  },
  "rms_norm_eps": 1e-06,
  "rope_scaling": {
    "beta_fast": 32,
    "beta_slow": 1,
    "factor": 40,
    "mscale": 1.0,
    "mscale_all_dim": 1.0,
    "original_max_position_embeddings": 4096,
    "type": "yarn"
  },
  "rope_theta": 10000,
  "routed_scaling_factor": 2.5,
  "scoring_func": "sigmoid",
  "seq_aux": true,
  "tie_word_embeddings": false,
  "topk_group": 4,
  "topk_method": "noaux_tc",
  "torch_dtype": "bfloat16",
  "transformers_version": "4.48.2",
  "use_cache": true,
  "v_head_dim": 128,
  "vocab_size": 129280
}
```

Total Parameters: 671,026,419,200

```
+-----------------------------------------------+------------+
|                    Modules                    | Parameters |
+-----------------------------------------------+------------+
|              embed_tokens.weight              | 926679040  |
|       layers.0.self_attn.q_a_proj.weight      |  11010048  |
|    layers.0.self_attn.q_a_layernorm.weight    |    1536    |
|       layers.0.self_attn.q_b_proj.weight      |  37748736  |
|  layers.0.self_attn.kv_a_proj_with_mqa.weight |  4128768   |
|    layers.0.self_attn.kv_a_layernorm.weight   |    512     |
|      layers.0.self_attn.kv_b_proj.weight      |  16777216  |
|        layers.0.self_attn.o_proj.weight       | 117440512  |
|         layers.0.mlp.gate_proj.weight         | 132120576  |
|          layers.0.mlp.up_proj.weight          | 132120576  |
|         layers.0.mlp.down_proj.weight         | 132120576  |
|        layers.0.input_layernorm.weight        |    7168    |
|    layers.0.post_attention_layernorm.weight   |    7168    |
|       layers.1.self_attn.q_a_proj.weight      |  11010048  |
|    layers.1.self_attn.q_a_layernorm.weight    |    1536    |
|       layers.1.self_attn.q_b_proj.weight      |  37748736  |
|  layers.1.self_attn.kv_a_proj_with_mqa.weight |  4128768   |
|    layers.1.self_attn.kv_a_layernorm.weight   |    512     |
|      layers.1.self_attn.kv_b_proj.weight      |  16777216  |
|        layers.1.self_attn.o_proj.weight       | 117440512  |
|         layers.1.mlp.gate_proj.weight         | 132120576  |
|          layers.1.mlp.up_proj.weight          | 132120576  |
|         layers.1.mlp.down_proj.weight         | 132120576  |
|        layers.1.input_layernorm.weight        |    7168    |
|    layers.1.post_attention_layernorm.weight   |    7168    |
|       layers.2.self_attn.q_a_proj.weight      |  11010048  |
|    layers.2.self_attn.q_a_layernorm.weight    |    1536    |
|       layers.2.self_attn.q_b_proj.weight      |  37748736  |
|  layers.2.self_attn.kv_a_proj_with_mqa.weight |  4128768   |
|    layers.2.self_attn.kv_a_layernorm.weight   |    512     |
|      layers.2.self_attn.kv_b_proj.weight      |  16777216  |
|        layers.2.self_attn.o_proj.weight       | 117440512  |
|         layers.2.mlp.gate_proj.weight         | 132120576  |
|          layers.2.mlp.up_proj.weight          | 132120576  |
|         layers.2.mlp.down_proj.weight         | 132120576  |
|        layers.2.input_layernorm.weight        |    7168    |
|    layers.2.post_attention_layernorm.weight   |    7168    |
|       layers.3.self_attn.q_a_proj.weight      |  11010048  |
|    layers.3.self_attn.q_a_layernorm.weight    |    1536    |
|       layers.3.self_attn.q_b_proj.weight      |  37748736  |
|  layers.3.self_attn.kv_a_proj_with_mqa.weight |  4128768   |
|    layers.3.self_attn.kv_a_layernorm.weight   |    512     |
|      layers.3.self_attn.kv_b_proj.weight      |  16777216  |
|        layers.3.self_attn.o_proj.weight       | 117440512  |
|    layers.3.mlp.experts.0.gate_proj.weight    |  14680064  |
|     layers.3.mlp.experts.0.up_proj.weight     |  14680064  |
|    layers.3.mlp.experts.0.down_proj.weight    |  14680064  |
|    layers.3.mlp.experts.1.gate_proj.weight    |  14680064  |
|     layers.3.mlp.experts.1.up_proj.weight     |  14680064  |
|    layers.3.mlp.experts.1.down_proj.weight    |  14680064  |
|     ... mlp.experts.2 to mlp.experts.255 ...  |    ...     |
|            layers.3.mlp.gate.weight           |  1835008   |
|   layers.3.mlp.gate.e_score_correction_bias   |    256     |
|  layers.3.mlp.shared_experts.gate_proj.weight |  14680064  |
|   layers.3.mlp.shared_experts.up_proj.weight  |  14680064  |
|  layers.3.mlp.shared_experts.down_proj.weight |  14680064  |
|        layers.3.input_layernorm.weight        |    7168    |
|    layers.3.post_attention_layernorm.weight   |    7168    |
|        ... layers.4 to layers.60 ...          |    ...     |
|                  norm.weight                  |    7168    |
+-----------------------------------------------+------------+
```

References:
- https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/main/README_WEIGHTS.md