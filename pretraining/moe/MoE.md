# Mixture of Experts

- **Params:** The total number of parameters in the MoE model. This includes all weights and biases in the model, both within the shared layers and the expert layers.
- **Total Routed:** This indicates the total number of available experts this MoE model has.
- **Activated Routed:** This refers to the specific experts that are activated and used for a given input. In MoE models, only a subset of all available experts are activated for processing each input.
- **Shared Experts:** The experts in the MoE model that are accessible and used by multiple input tokens or instances. These experts are shared across different parts of the input space.
- **Layers:** This stands for the number of layers in the model. It signifies the depth of the neural network, i.e., how many successive layers of processing the data goes through.
- **Heads:** This refers to the number of heads in a multi-head attention mechanism, which is commonly used in transformer models. Multi-head attention allows the model to focus on different parts of the input simultaneously.

The following is a standard transformer block (generalised version of the dense [Llama 1/2/3 architecture](../architecture/)).

![Transformer block based on the Llama architecture](./figures/llama_transformer_block_dark.svg#gh-dark-mode-only)
![Transformer block based on the Llama architecture](./figures/llama_transformer_block.svg#gh-light-mode-only)

The feed forward network (FFN) on the transformer block is replaced by an Mixture of Experts (MoE) block. This architecture includes both a shared expert and routed experts (like DeepseekMoE and Meta Llama-4).

![Transformer block based on the Llama architecture](./figures/llama_transformer_block_dark.svg#gh-dark-mode-only)
![Transformer block based on the Llama architecture](./figures/llama_transformer_block.svg#gh-light-mode-only)

| Model            | Params | Shared | Total Routed | Activated Routed | Fine-grain  | Affiliation    | Release   |
|------------------|--------|--------|--------------|------------------|-------------|----------------|-----------|
| [DeepSeek-V3](../architecture/DeepseekV3.md)      | 671B   | 1      | 256          | 8                | Y           | DeepSeek-AI    | 2024.12   |
| Hunyuan-Large    | 389B   | 1      | 16           | 1                | N           | Tencent        | 2024.11   |
| GRIN-MoE         | 41.9B  | 0      | 16           | 2                | N           | Microsoft      | 2024.09   |
| Phi-3            | 41.9B  | 0      | 16           | 2                | N           | Microsoft      | 2024.08   |
| OLMoE            | 6.92B  | 0      | 64           | 8                | N           | AllenAI        | 2024.07   |
| LLaMA-MoE        | 6.7B   | 0      | 8            | 2                | N           | Zhu et al.     | 2024.06   |
| Skywork-MoE      | 13B    | 0      | 16           | 2                | N           | Kunlun Tech    | 2024.05   |
| Yuan2            | 40B    | 0      | 32           | 2                | N           | IEIT-Yuan      | 2024.05   |
| Qwen2-57B-A14B   | 57.4B  | 0      | 64           | 8                | Y           | Alibaba        | 2024.05   |
| Arctic           | 482B   | 0      | 128          | 2                | N           | Snowflake      | 2024.04   |
| Mixtral-8x22B    | 141B   | 0      | 8            | 2                | N           | Mistral AI     | 2024.04   |
| DeepSeek-V2      | 236B   | 2      | 160          | 6                | Y           | DeepSeek-AI    | 2024.04   |
| JetMoE           | 8.52B  | 0      | 8            | 2                | N           | MIT et al.     | 2024.03   |
| Jamba            | 51.6B  | 0      | 16           | 2                | N           | ai21labs       | 2024.03   |
| DBRX             | 132B   | 0      | 16           | 4                | N           | Databricks     | 2024.03   |
| Grok-1           | 314B   | 0      | 8            | 2                | ?           | xAI            | 2024.03   |
| Qwen1.5-MoE      | 14.3B  | 0      | 60           | 4                | Y           | Alibaba        | 2024.02   |
| DeepSeekMoE      | 16.4B  | 2      | 64           | 6                | Y           | DeepSeek-AI    | 2024.01   |
| Mixtral-8x7B     | 46.7B  | 0      | 8            | 2                | N           | Mistral AI     | 2023.12   |
| OpenMoE          | 34B    | 0      | 16           | 2                | N           | NUS et al.     | 2023.12   |

## References

- DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models. - https://arxiv.org/abs/2401.06066

