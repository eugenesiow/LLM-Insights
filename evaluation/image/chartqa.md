# ChartQA

ChartQA is a multimodal benchmark for question-answering (with vision language models (VLMs) or multimodal models) about charts (images) using visual and logical reasoning by Masry et al. from York University, Nanyang Technological University and Salesforce Research. It was from the paper [ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning](https://arxiv.org/abs/2203.10244) published in Mar 2022. The benchmark covers 9.6K human-written questions as well as 23.1K questions generated from human-written chart summaries.

## Links

* Abstract: https://arxiv.org/abs/2203.10244
* Homepage: https://github.com/vis-nlp/ChartQA
* Dataset: https://huggingface.co/datasets/HuggingFaceM4/ChartQA
* License: [GPL-3.0](https://huggingface.co/datasets/HuggingFaceM4/ChartQA/blob/main/README.md)

## Implementation

NOTE: Taken from the Mistral implementation of the task: https://github.com/mistralai/mistral-evals/blob/main/eval/tasks/chartqa.py.

Below are [configurations](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/chartqa) from [EleutherAI's Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness).

<details>
<summary>chartqa</summary>

```yaml
dataset_path: HuggingFaceM4/ChartQA
test_split: test
output_type: generate_until
task: chartqa
doc_to_image:
  - image
doc_to_text: |
  <image>{{query}}
  Analyze the image and question carefully, using step-by-step reasoning.
  First, describe any image provided in detail. Then, present your reasoning. And finally your final answer in this format:
  Final Answer: <answer>
  where <answer> follows the following instructions:
  - <answer> should should be a single phrase or number.
  - <answer> should not paraphrase or reformat the text in the image.
  - If <answer> is a ratio, it should be a decimal value like 0.25 instead of 1:4.
  - If the question is a Yes/No question, <answer> should be Yes/No.
  - If <answer> is a number, it should not contain any units.
  - If <answer> is a percentage, it should include a % sign.
  - If <answer> is an entity, it should include the full label from the graph.
  IMPORTANT: Remember, to end your answer with Final Answer: <answer>.
doc_to_target: "{{ label[0] }}"
generation_kwargs:
  until: []
  temperature: 0.0
  do_sample: false
  max_gen_toks: 512
metric_list:
  - metric: !function utils.exact_match
    aggregation: mean
    higher_is_better: true
  - metric: !function utils.relaxed_accuracy
    aggregation: mean
    higher_is_better: true
  - metric: !function utils.anywhere_accuracy
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/chartqa/chartqa.yaml
</details>

## Citations

```bibtex
@misc{masry2022chartqabenchmarkquestionanswering,
      title={ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning},
      author={Ahmed Masry and Do Xuan Long and Jia Qing Tan and Shafiq Joty and Enamul Hoque},
      year={2022},
      eprint={2203.10244},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2203.10244},
}
```