# Inference

- [Inference](#inference)
  - [Estimating Model Size](#estimating-model-size)
    - [Inference Memory](#inference-memory)
    - [Tools](#tools)
  - [Generative Inference Speed](#generative-inference-speed)
  - [Generative Inference Throughput](#generative-inference-throughput)
  - Techniques
    - [n-shot Prompting](techniques/nshot.md) - the method of conditioning a language model with *n* example pairs that demonstrate the desired task, guiding the model to produce outputs consistent with the provided examples. Increasing the number of examples can help clarify task expectations and often leads to better performance. 0-shot prompting is a special case where only instructions are provided, without any examples.
    - [Chain-of-Thought Prompting](techniques/cot.md) - encourages language models to generate intermediate reasoning steps before arriving at a final answer. This technique helps models break down complex problems into manageable sub-steps, improving performance on tasks that require multi-step reasoning.

## Estimating Model Size

### Inference Memory

A frequent question we have is estimating how much GPU memory (VRAM) is required for inference for different models of different parameter sizes. Based on EleutherAI's [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) estimates, this is about 1.2 times the total model size in memory. The following is a table of common models and how much memory they require for inference. The memory required is also dependent on what precision the weights are stored with in GPU memory. This can vary from full precision (FP32), half precision (FP16/BF16) or quantised 8-bit (INT8) and 4-bit (INT4) precisions. In my experience, FP16/BF16 are good precisions for LLMs to work with. With INT8 and INT4 there might be some drop in accuracy depending on how it was quantized.

|  Model  |        Parameters        |                      FP32                      |                   FP16/BF16                   |                    INT8                     |                    INT4                    |
|---------|--------------------------|------------------------------------------------|-----------------------------------------------|---------------------------------------------|--------------------------------------------|
|CodeLLaMA|13b<br/>34b               |58.2 GB<br/>150.58 GB                           |29.1 GB<br/>75.29 GB                           |14.55 GB<br/>37.64 GB                        |7.28 GB<br/>18.82 GB                        |
|LLaMA    |7b<br/>13b<br/>30b<br/>65b|29.61 GB<br/>57.55 GB<br/>144.6 GB<br/>290.87 GB|14.81 GB<br/>28.77 GB<br/>72.3 GB<br/>145.43 GB|7.4 GB<br/>14.39 GB<br/>36.15 GB<br/>72.72 GB|3.7 GB<br/>7.19 GB<br/>18.08 GB<br/>36.36 GB|
|LLaMA-2  |7b<br/>13b<br/>70b        |29.61 GB<br/>57.55 GB<br/>307.55 GB             |14.81 GB<br/>28.77 GB<br/>153.78 GB            |7.4 GB<br/>14.39 GB<br/>76.89 GB             |3.7 GB<br/>7.19 GB<br/>38.44 GB             |
|OpenLLaMA|3b                        |14.91 GB                                        |7.45 GB                                        |3.73 GB                                      |1.86 GB                                     |
|T5 v1.1  |11b                       |49.19 GB                                        |24.6 GB                                        |12.3 GB                                      |6.15 GB                                     |

### Tools

- [🤗 Model Memory Calculator](https://huggingface.co/spaces/hf-accelerate/model-memory-usage)
- [Can you run it? LLM version](https://huggingface.co/spaces/Vokturz/can-it-run-llm)

## Generative Inference Speed

- The inference speed for each engine on models of varying sizes is recorded below. 
- The speed is measured by the average tokens per second (tokens/s) that an engine can generate given a single request. Bigger is better.
- The experiments are averaged across 100 randomly sampled chat dialogue prompts from the [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206) dataset that covers 1000 well-curated chat-style instruction prompts and completions.
- The hardware used for testing, depending on model size, is one to two A100 (80GB) GPUs which are interconnected via NVLINK (SXM) on a DGX A100 (640GB).
- As much as possible, OpenAI-compatible chat completion APIs are used in the testing and the full round-trip for the request is measured.
- Only the completion/output tokens are counted in token/s calculations.
- [Transformers (default)](https://huggingface.co/docs/transformers/index)
  - Version: 4.31.0
- [vLLM](https://github.com/vllm-project/vllm)
  - Version: 0.1.3
- [text-generation-inference](https://github.com/huggingface/text-generation-inference) (TGI)
  - Version: 1.0.1

<!-- | Engine                    | mpt-7b-chat   | vicuna-13b-v1.5 | oasst-30b   | llama2-70b-chat   |
|---------------------------|---------------|-----------------|-------------|-------------------|
| Transformers (default)    |               | 30.40           | 14.89       | 9.53              |
| vLLM                      | **84.37**     | 48.42           | 21.80       | 17.00             |
| text-generation-inference | 67.16         | **49.48**       | **22.05**   | **18.61**         | -->

Engine                  | Transformers           | vLLM      | TGI
---                     | ---                    | ---       | ---
mpt-7b-chat             |                        | **84.37** | 67.16
falcon-7b-instruct      | 25.10                  | 82.68     | **86.71**
vicuna-7b-v1.3          | 28.71                  | 41.14     | **84.26**
vicuna-13b-v1.5         | 30.40                  | 48.42     | **49.48**
oasst-30b               | 14.89                  | 21.80     | **22.05**
llama2-70b-chat         | 9.53                   | 17.00     | **18.61**

- Custom CUDA kernels were turned off for these runs with TGI.

## Generative Inference Throughput

- The throughput is measured by requests per minute (requests/min) that an engine can handle. Bigger is better.

Engine                  | Transformers           | vLLM      | text-generation-inference
---                     | ---                    | ---       | ---
llama2-70b-chat         | 0.6                    | 14.4      | 6.0