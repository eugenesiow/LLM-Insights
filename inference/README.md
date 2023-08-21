# Inference

- [Transformers (default)](https://huggingface.co/docs/transformers/index)
    - Version: 4.31.0
- [vLLM](https://github.com/vllm-project/vllm)
    - Version: 0.1.3
- [text-generation-inference](https://github.com/huggingface/text-generation-inference)
    - Version: 1.0.1

## Generative Inference Speed

- The inference speed for each engine on models of varying sizes is recorded below. 
- The speed is measured by the average tokens per second (tokens/s) that an engine can generate given a single request. Bigger is better.
- The experiments are averaged across 100 randomly sampled chat dialogue prompts from the [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206) dataset that covers 1000 well-curated chat-style instruction prompts and completions.
- The hardware used for testing, depending on model size, is one to two A100 (80GB) GPUs which are interconnected via NVLINK (SXM) on a DGX A100 (640GB).
- As much as possible, OpenAI-compatible chat completion APIs are used in the testing and the full round-trip for the request is measured.
- Only the completion/output tokens are counted in token/s calculations.

<!-- | Engine                    | mpt-7b-chat   | vicuna-13b-v1.5 | oasst-30b   | llama2-70b-chat   |
|---------------------------|---------------|-----------------|-------------|-------------------|
| Transformers (default)    |               | 30.40           | 14.89       | 9.53              |
| vLLM                      | **84.37**     | 48.42           | 21.80       | 17.00             |
| text-generation-inference | 67.16         | **49.48**       | **22.05**   | **18.61**         | -->

Engine                  | Transformers           | vLLM      | text-generation-inference
---                     | ---                    | ---       | ---
mpt-7b-chat             |                        | **84.37** | 67.16
falcon-7b-instruct      |                        | **82.68** | 
vicuna-13b-v1.3         |                        | 41.14     | 
vicuna-13b-v1.5         | 30.40                  | 48.42     | **49.48**
oasst-30b               | 14.89                  | 21.80     | **22.05**
llama2-70b-chat         | 9.53                   | 17.00     | **18.61**

## Generative Inference Throughput

- The throughput is measured by requests per minute (requests/min) that an engine can handle. Bigger is better.

Engine                  | Transformers           | vLLM      | text-generation-inference
---                     | ---                    | ---       | ---
llama2-70b-chat         |                    |      | 