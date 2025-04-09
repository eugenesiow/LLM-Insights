# Llama 4

## Llama 4 Scout (Llama-4-Scout-17B-16E)

```
Llama4Config {
  "architectures": [
    "Llama4ForConditionalGeneration"
  ],
  "boi_token_index": 200080,
  "eoi_token_index": 200081,
  "image_token_index": 200092,
  "model_type": "llama4",
  "text_config": {
    "attention_bias": false,
    "attention_chunk_size": 8192,
    "attention_dropout": 0.0,
    "attn_scale": 0.1,
    "attn_temperature_tuning": 4,
    "bos_token_id": 200000,
    "eos_token_id": [
      200001,
      200007,
      200008
    ],
    "floor_scale": 8192,
    "for_llm_compressor": false,
    "head_dim": 128,
    "hidden_act": "silu",
    "hidden_size": 5120,
    "initializer_range": 0.02,
    "interleave_moe_layer_step": 1,
    "intermediate_size": 8192,
    "intermediate_size_mlp": 16384,
    "max_position_embeddings": 262144,
    "model_type": "llama4_text",
    "moe_layers": [
      0..47
    ],
    "no_rope_layers": [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0],
    "num_attention_heads": 40,
    "num_experts_per_tok": 1,
    "num_hidden_layers": 48,
    "num_key_value_heads": 8,
    "num_local_experts": 16,
    "output_router_logits": false,
    "pad_token_id": 200018,
    "rms_norm_eps": 1e-05,
    "rope_scaling": {
      "factor": 8.0,
      "high_freq_factor": 4.0,
      "low_freq_factor": 1.0,
      "original_max_position_embeddings": 8192,
      "rope_type": "llama3"
    },
    "rope_theta": 500000.0,
    "router_aux_loss_coef": 0.001,
    "router_jitter_noise": 0.0,
    "torch_dtype": "bfloat16",
    "use_cache": true,
    "use_qk_norm": true,
    "vocab_size": 202048
  },
  "tie_word_embeddings": false,
  "transformers_version": "4.51.0",
  "vision_config": {
    "attention_dropout": 0.0,
    "hidden_act": "gelu",
    "hidden_size": 1408,
    "image_size": 336,
    "initializer_range": 0.02,
    "intermediate_size": 5632,
    "model_type": "llama4_vision_model",
    "multi_modal_projector_bias": false,
    "norm_eps": 1e-05,
    "num_attention_heads": 16,
    "num_channels": 3,
    "num_hidden_layers": 34,
    "patch_size": 14,
    "pixel_shuffle_ratio": 0.5,
    "projector_dropout": 0.0,
    "projector_input_dim": 4096,
    "projector_output_dim": 4096,
    "rope_theta": 10000,
    "vision_feature_layer": -1,
    "vision_feature_select_strategy": "default",
    "vision_output_dim": 4096
  }
}
```

Total Trainable Params: 109,676,279,296 (109B)

```
+----------------------------------------------------------------------------+------------+
|                                  Modules                                   | Parameters |
+----------------------------------------------------------------------------+------------+
|                        vision_model.class_embedding                        |    1408    |
|                   vision_model.positional_embedding_vlm                    |   812416   |
|                 vision_model.patch_embedding.linear.weight                 |   827904   |
|                     vision_model.layernorm_pre.weight                      |    1408    |
|                      vision_model.layernorm_pre.bias                       |    1408    |
|                     vision_model.layernorm_post.weight                     |    1408    |
|                      vision_model.layernorm_post.bias                      |    1408    |
|            vision_model.model.layers.0.self_attn.q_proj.weight             |  1982464   |
|             vision_model.model.layers.0.self_attn.q_proj.bias              |    1408    |
|            vision_model.model.layers.0.self_attn.k_proj.weight             |  1982464   |
|             vision_model.model.layers.0.self_attn.k_proj.bias              |    1408    |
|            vision_model.model.layers.0.self_attn.v_proj.weight             |  1982464   |
|             vision_model.model.layers.0.self_attn.v_proj.bias              |    1408    |
|            vision_model.model.layers.0.self_attn.o_proj.weight             |  1982464   |
|             vision_model.model.layers.0.self_attn.o_proj.bias              |    1408    |
|                 vision_model.model.layers.0.mlp.fc1.weight                 |  7929856   |
|                  vision_model.model.layers.0.mlp.fc1.bias                  |    5632    |
|                 vision_model.model.layers.0.mlp.fc2.weight                 |  7929856   |
|                  vision_model.model.layers.0.mlp.fc2.bias                  |    1408    |
|             vision_model.model.layers.0.input_layernorm.weight             |    1408    |
|              vision_model.model.layers.0.input_layernorm.bias              |    1408    |
|        vision_model.model.layers.0.post_attention_layernorm.weight         |    1408    |
|         vision_model.model.layers.0.post_attention_layernorm.bias          |    1408    |
|                        ... layers.1 to layers.33 ...                       |     ...     |
|                 vision_model.vision_adapter.mlp.fc1.weight                 |   23068672  |
|                 vision_model.vision_adapter.mlp.fc2.weight                 |   16777216  |
|                   multi_modal_projector.linear_1.weight                    |   20971520  |
|                  language_model.model.embed_tokens.weight                  |  1034485760 |
|           language_model.model.layers.0.self_attn.q_proj.weight            |   26214400  |
|           language_model.model.layers.0.self_attn.k_proj.weight            |   5242880   |
|           language_model.model.layers.0.self_attn.v_proj.weight            |   5242880   |
|           language_model.model.layers.0.self_attn.o_proj.weight            |   26214400  |
|        language_model.model.layers.0.feed_forward.gate_proj.weight         |   83886080  |
|         language_model.model.layers.0.feed_forward.up_proj.weight          |   83886080  |
|        language_model.model.layers.0.feed_forward.down_proj.weight         |   83886080  |
|            language_model.model.layers.0.input_layernorm.weight            |     5120    |
|       language_model.model.layers.0.post_attention_layernorm.weight        |     5120    |
|                        ... layers.1 to layers.47 ...                       |     ...     |          
|                      language_model.model.norm.weight                      |     5120    |
|                       language_model.lm_head.weight                        |  1034485760 |
+----------------------------------------------------------------------------+-------------+
```

References:
- https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E
- https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E