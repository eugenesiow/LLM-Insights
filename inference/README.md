## Engines

- [Transformers (default)](https://huggingface.co/docs/transformers/index)
- [vLLM](https://github.com/vllm-project/vllm)
- [text-generation-inference](https://github.com/huggingface/text-generation-inference)

## Inference Throughput

- The inference throughput for each engine on models of varying sizes is recorded below. 
- The throughput is measured by the average tokens per second that an engine can generate. Bigger is better.
- The experiments are averaged across 100 randomly sampled chat dialogue prompts from the [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206) dataset that covers 1000 well-curated chat-style instruction prompts and completions.
- The hardware used for testing, depending on model size, is one to two A100 (80GB) GPUs which are interconnected via NVLINK (SXM) on a DGX A100 (640GB).

| Engine                    | mpt-7b-chat   | vicuna-13b-v1.5 | oasst-30b   | llama2-70b-chat   |
|---------------------------|---------------|-----------------|-------------|-------------------|
| Transformers (default)    |               | 30.40           | 14.89       |                   |
| vLLM                      | **84.37**     | **48.42**       | **21.80**   | **17.00**         |
| text-generation-inference |               |                 |             |                   |