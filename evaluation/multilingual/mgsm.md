# MGSM

Multilingual Grade School Math Benchmark (MGSM) is a benchmark of grade-school math problems, proposed in the paper [Language models are multilingual chain-of-thought reasoners](https://arxiv.org/abs/2210.03057).

The same 250 problems from [GSM8K](../math/gsm8k.md) are each translated via human annotators in 10 languages. The 10 languages are:

1. Spanish
2. French
3. German
4. Russian
5. Chinese
6. Japanese
7. Thai
8. Swahili
9. Bengali
10. Telugu

## Links

* Abstract: https://arxiv.org/abs/2210.03057
* Dataset: https://huggingface.co/datasets/juletxara/mgsm
* License: [CC-BY-SA-4.0](https://huggingface.co/datasets/juletxara/mgsm/blob/main/README.md)

## Implementation

Below are [configurations](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/mgsm) from [EleutherAI's Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness).

<details>
<summary>direct/direct_yaml</summary>

```yaml
# This file will be included in the generated language-specific task configs.
# It doesn't have a yaml file extension as it is not meant to be imported directly
# by the harness.
tag: mgsm_direct
dataset_path: juletxara/mgsm
dataset_name: null  # Overridden by language-specific config.
output_type: generate_until
training_split: train
test_split: test
target_delimiter: ""
generation_kwargs:
  until:
    - "\n\n"
    - "\n"
  do_sample: false
  temperature: 0.0
filter_list:
  - name: remove_whitespace
    filter:
      - function: remove_whitespace
      - function: take_first
  - filter:
    - function: regex
      group_select: -1
      regex_pattern: (-?[$0-9.,]{2,})|(-?[0-9]+)
    - function: take_first
    name: flexible-extract
metric_list:
  - metric: exact_match
    aggregation: mean
    higher_is_better: true
    ignore_case: true
    ignore_punctuation: true
metadata:
  version: 3.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/direct/direct_yaml
</details>

<details>
<summary>en_cot/cot_yaml</summary>

```yaml
# This file will be included in the generated language-specific task configs.
# It doesn't have a yaml file extension as it is not meant to be imported directly
# by the harness.
tag: mgsm_cot_native
dataset_path: juletxara/mgsm
dataset_name: null  # Overridden by language-specific config.
output_type: generate_until
training_split: train
test_split: test
generation_kwargs:
  until:
    - "\n\n"
    - "\n"
  do_sample: false
  temperature: 0.0
target_delimiter: " "
metric_list:
  - metric: exact_match
    aggregation: mean
    higher_is_better: true
    ignore_case: true
    ignore_punctuation: true
filter_list:
  - name: "strict-match"
    filter:
      - function: "regex"
        regex_pattern: "The answer is (\\-?[0-9\\.\\,]+)"
      - function: "take_first"
  - filter:
    - function: regex
      group_select: -1
      regex_pattern: (-?[$0-9.,]{2,})|(-?[0-9]+)
    - function: take_first
    name: flexible-extract
metadata:
  version: 3.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/en_cot/cot_yaml
</details>

<details>
<summary>native_cot/cot_yaml</summary>

```yaml
# This file will be included in the generated language-specific task configs.
# It doesn't have a yaml file extension as it is not meant to be imported directly
# by the harness.
tag: mgsm_cot_native
dataset_path: juletxara/mgsm
dataset_name: null  # Overridden by language-specific config.
output_type: generate_until
training_split: train
test_split: test
# target_delimiter: ""
generation_kwargs:
  until:
    - "\n\n"
    - "\n"
  do_sample: false
  temperature: 0.0
target_delimiter: " "
metric_list:
  - metric: exact_match
    aggregation: mean
    higher_is_better: true
    ignore_case: true
    ignore_punctuation: true
filter_list:
  - name: "get-answer"
    filter:
      - function: "regex"
        regex_pattern: "The answer is (\\-?[0-9\\.\\,]+)"
      - function: "take_first"
metadata:
  version: 4.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/native_cot/cot_yaml
</details>

## Citations

```bibtex
@misc{cobbe2021training,
    title={Training Verifiers to Solve Math Word Problems},
    author={Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},
    year={2021},
    eprint={2110.14168},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
@misc{shi2022language,
    title={Language Models are Multilingual Chain-of-Thought Reasoners},
    author={Freda Shi and Mirac Suzgun and Markus Freitag and Xuezhi Wang and Suraj Srivats and Soroush Vosoughi and Hyung Won Chung and Yi Tay and Sebastian Ruder and Denny Zhou and Dipanjan Das and Jason Wei},
    year={2022},
    eprint={2210.03057},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

