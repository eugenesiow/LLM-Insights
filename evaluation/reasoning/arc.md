# ARC

The [AI2's Reasoning Challenge (ARC)](https://allenai.org/data/arc) dataset is a multiple-choice question-answering dataset, containing questions from science exams from grade 3 to grade 9. The dataset is split in two partitions: Easy (ARC_e) and Challenge (ARC_c), where the latter partition contains the more difficult questions that require reasoning. Most of the questions have 4 answer choices, with <1% of all the questions having either 3 or 5 answer choices. 

## Links

* Abstract: https://arxiv.org/abs/1803.05457
* Homepage: https://allenai.org/data/arc
* Dataset: https://huggingface.co/datasets/allenai/ai2_arc
* License: [CC-BY-SA-4.0](https://huggingface.co/datasets/allenai/ai2_arc/blob/main/README.md)

## Implementation

Below are [configurations](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/arc) from [EleutherAI's Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness).

<details>
<summary>arc/arc_challenge_chat</summary>

```yaml
tag:
  - llama
task: arc_challenge_chat
dataset_path: allenai/ai2_arc
dataset_name: ARC-Challenge
output_type: generate_until
training_split: train
validation_split: validation
test_split: test
fewshot_split: train
doc_to_text: 'Given the following question and four candidate answers (A, B, C and D), choose the best answer.\nQuestion: {{question.strip()}}\nA. {{choices.text[0]}}\nB. {{choices.text[1]}}\nC. {{choices.text[2]}}{% if choices.text|length > 3 %}\nD. {{choices.text[3]}}{% endif %}\nYour response should end with "The best answer is [the_answer_letter]" where the [the_answer_letter] is one of A, B, C or D.'
gen_prefix: 'The best answer is'
fewshot_delimiter: "\n\n"
doc_to_target: "{{ 'ABCD'[answerKey|int - 1] if answerKey|string in '1234' else answerKey }}"
num_fewshot: 0
generation_kwargs:
  max_gen_toks: 100
  until:
    - "\n\n"
    - "."
metric_list:
  - metric: exact_match
    aggregation: mean
    higher_is_better: true
    ignore_case: true
    ignore_punctuation: true
filter_list:
  - name: remove_whitespace
    filter:
      - function: remove_whitespace
      - function: take_first
metadata:
  version: 1.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/arc/arc_challenge_chat.yaml
</details>

<details>
<summary>arc/arc_easy</summary>

```yaml
tag:
  - ai2_arc
task: arc_easy
dataset_path: allenai/ai2_arc
dataset_name: ARC-Easy
output_type: multiple_choice
training_split: train
validation_split: validation
test_split: test
doc_to_text: "Question: {{question}}\nAnswer:"
doc_to_target: "{{choices.label.index(answerKey)}}"
doc_to_choice: "{{choices.text}}"
should_decontaminate: true
doc_to_decontamination_query: "Question: {{question}}\nAnswer:"
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
  - metric: acc_norm
    aggregation: mean
    higher_is_better: true
metadata:
  version: 1.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/arc/arc_easy.yaml
</details>

## Citations

```bibtex
@article{Clark2018ThinkYH,
  title={Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge},
  author={Peter Clark and Isaac Cowhey and Oren Etzioni and Tushar Khot and Ashish Sabharwal and Carissa Schoenick and Oyvind Tafjord},
  journal={ArXiv},
  year={2018},
  volume={abs/1803.05457}
}
```