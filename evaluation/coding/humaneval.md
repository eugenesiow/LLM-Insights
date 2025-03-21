# HumanEval

The HumanEval dataset released by OpenAI includes 164 programming problems with a function signature, docstring, body, and several unit tests. They were handwritten to ensure not to be included in the training set of code generation models.

The programming problems are written in Python and contain English natural text in comments and docstrings.

## Links

* Abstract: https://arxiv.org/abs/2107.03374
* Homepage: https://github.com/openai/human-eval
* Dataset: https://huggingface.co/datasets/openai/openai_humaneval
* License: [MIT](https://huggingface.co/datasets/openai/openai_humaneval/blob/main/README.md)

## Example Questions

Below is an example prompt, canonical solution and unit test to test for correctness of solution.

<details>
<summary>Example Prompt</summary>

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
```
</details>

<details>
<summary>Example Canonical Solution</summary>

```python
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False
```
</details>

<details>
<summary>Example Unit Test</summary>

```python
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False
```

</details>

## Implementation

NOTE: See the official implementation of the task: https://github.com/openai/grade-school-math/blob/master/grade_school_math/calculator.py.

Below we show [configurations](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/gsm8k) from [EleutherAI's Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness).


<details>
<summary>Zeroshot</summary>

```yaml
task: humaneval
dataset_path: openai/openai_humaneval
unsafe_code: true
output_type: generate_until
test_split: test
doc_to_text: "{{prompt}}"
doc_to_target: "{{test}}\ncheck({{entry_point}})"
metric_list:
  - metric: !function utils.pass_at_k
    aggregation: mean
    higher_is_better: true
    k: [1]
generation_kwargs:
  until:
    - "\nclass"
    - "\ndef"
    - "\n#"
    - "\nif"
    - "\nprint"
  max_gen_toks: 1024
  do_sample: false
repeats: 1
num_fewshot: 0
filter_list:
  - name: "create_test"
    filter:
      - function: "custom"
        filter_fn: !function utils.build_predictions
metadata:
  version: 1.0
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/gsm8k/gsm8k.yaml
</details>


<details>
<summary>pass@1</summary>

```yaml
tag:
  - math_word_problems
task: gsm8k_cot_zeroshot
dataset_path: gsm8k
dataset_name: main
output_type: generate_until
training_split: train
fewshot_split: train
test_split: test
doc_to_text: "Q: {{question}}\nA: Let's think step by step."
doc_to_target: "{{answer}}" #" {{answer.split('### ')[-1].rstrip()}}"
metric_list:
  - metric: exact_match
    aggregation: mean
    higher_is_better: true
    ignore_case: true
    ignore_punctuation: false
    regexes_to_ignore:
      - ","
      - "\\$"
      - "(?s).*#### "
      - "\\.$"
generation_kwargs:
  until:
    - "Q:"
    - "</s>"
    - "<|im_end|>"
  do_sample: false
repeats: 1
num_fewshot: 0
filter_list:
  - name: "strict-match"
    filter:
      - function: "regex"
        regex_pattern: "The answer is (\\-?[0-9\\.\\,]+)."
      - function: "take_first"
  - name: "flexible-extract"
    filter:
      - function: "regex"
        group_select: -1
        regex_pattern: "(-?[$0-9.,]{2,})|(-?[0-9]+)"
      - function: "take_first"
metadata:
  version: 3.0
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/humaneval/humaneval.yaml
</details>

<details>
<summary>pass@64</summary>

```yaml
include: humaneval.yaml
task: humaneval_64
repeats: 64
metric_list:
  - metric: !function utils.pass_at_k
    aggregation: mean
    higher_is_better: true
    k: [2,8,16,32,64]
generation_kwargs:
  until:
    - "\nclass"
    - "\ndef"
    - "\n#"
    - "\nif"
    - "\nprint"
  max_gen_toks: 1024
  do_sample: true
  temperature: 0.2
  top_p: 0.95
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/humaneval/humaneval_64.yaml
</details>

<details>
<summary>pass@1 (for instruction-tuned models)</summary>

```yaml
include: humaneval.yaml
task: humaneval_instruct
doc_to_text: "Write a solution to the following problem and make sure that it passes the tests:\n```{{prompt}}"
gen_prefix: "Here is the completed function:\n```python\n{{prompt}}\n"
filter_list:
  - name: "create_test"
    filter:
      - function: "custom"
        filter_fn: !function utils.build_predictions_instruct
metadata:
  version: 2.0
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/humaneval/humaneval_instruct.yaml
</details>

<details>
<summary>pass@64 (for instruction-tuned models)</summary>

```yaml
include: humaneval_64.yaml
task: humaneval_64_instruct
doc_to_text: "Write a solution to the following problem and make sure that it passes the tests:\n```{{prompt}}"
gen_prefix: "Here is the completed function:\n```python\n{{prompt}}\n"
filter_list:
  - name: "create_test"
    filter:
      - function: "custom"
        filter_fn: !function utils.build_predictions_instruct
metadata:
  version: 2.0
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/humaneval/humaneval_64_instruct.yaml
</details>

## Plus Version

[HumanEval+](https://huggingface.co/datasets/evalplus/humanevalplus) is a dataset which builds on HumanEval with 80x more tests than the original. It also fixes over 10% of HumanEval solutions which were incorrectly implemented or had incorrect ground-truth. For each task, based on around 30 ChatGPT-generated seed inputs, which are produced using 3 separate prompts, type-aware mutation is applied to generate 1000 additional inputs with a one-hour budget. 

## Citation

```
@article{chen2021codex,
  title={Evaluating Large Language Models Trained on Code},
  author={Mark Chen and Jerry Tworek and Heewoo Jun and Qiming Yuan and Henrique Ponde de Oliveira Pinto and Jared Kaplan and Harri Edwards and Yuri Burda and Nicholas Joseph and Greg Brockman and Alex Ray and Raul Puri and Gretchen Krueger and Michael Petrov and Heidy Khlaaf and Girish Sastry and Pamela Mishkin and Brooke Chan and Scott Gray and Nick Ryder and Mikhail Pavlov and Alethea Power and Lukasz Kaiser and Mohammad Bavarian and Clemens Winter and Philippe Tillet and Felipe Petroski Such and Dave Cummings and Matthias Plappert and Fotios Chantzis and Elizabeth Barnes and Ariel Herbert-Voss and William Hebgen Guss and Alex Nichol and Alex Paino and Nikolas Tezak and Jie Tang and Igor Babuschkin and Suchir Balaji and Shantanu Jain and William Saunders and Christopher Hesse and Andrew N. Carr and Jan Leike and Josh Achiam and Vedant Misra and Evan Morikawa and Alec Radford and Matthew Knight and Miles Brundage and Mira Murati and Katie Mayer and Peter Welinder and Bob McGrew and Dario Amodei and Sam McCandlish and Ilya Sutskever and Wojciech Zaremba},
  year={2021},
  eprint={2107.03374},
  archivePrefix={arXiv},
  primaryClass={cs.LG}
}
```