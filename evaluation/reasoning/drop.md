# DROP

DROP stands for [Discrete Reasoning Over the content of Paragraphs](https://arxiv.org/abs/1903.00161) and is a question-answering (QA) dataset which tests comprehensive understanding of paragraphs. It consists of 96k question-answer samples. To answer the questions, a model must resolve multiple references in a question, map them onto a paragraph, and perform discrete operations over them (such as addition, counting, or sorting).

## Links

* Abstract: https://arxiv.org/abs/1903.00161
* Code: https://github.com/allenai/allennlp-reading-comprehension/blob/master/allennlp_rc/eval/drop_eval.py
* Dataset: https://huggingface.co/datasets/EleutherAI/drop
* License: [CC-BY-4.0](https://huggingface.co/datasets/EleutherAI/drop/blob/main/README.md)

## Implementation

Below are [configurations](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/drop) from [EleutherAI's Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness).

<details>
<summary>drop/default</summary>

```yaml
task: drop
dataset_path: EleutherAI/drop
output_type: generate_until
training_split: train
validation_split: validation
process_docs: !function utils.process_docs
doc_to_text: "{{passage}} {{question}}"
doc_to_target: "{{ answer|join(',')}}"
target_delimiter: ""
process_results: !function utils.process_results
should_decontaminate: true
doc_to_decontamination_query: "{{passage}} {{question}}"
generation_kwargs:
  until:
    - "."
metric_list:
  - metric: em
    aggregation: mean
    higher_is_better: true
  - metric: f1
    aggregation: mean
    higher_is_better: true
metadata:
  version: 3.0
dataset_kwargs:
  trust_remote_code: true

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/drop/default.yaml
</details>

## Citations

```bibtex
@misc{dua2019drop,
    title={DROP: A Reading Comprehension Benchmark Requiring Discrete Reasoning Over Paragraphs},
    author={Dheeru Dua and Yizhong Wang and Pradeep Dasigi and Gabriel Stanovsky and Sameer Singh and Matt Gardner},
    year={2019},
    eprint={1903.00161},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

