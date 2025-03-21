# GSM8K

GSM8K (Grade School Math 8K) is a dataset of 8.5K high quality linguistically diverse grade school math word problems. The dataset was created by [OpenAI](https://huggingface.co/openai) to support the task of question answering on basic mathematical problems that require multi-step reasoning.

- These problems take between 2 and 8 steps to solve.
- Solutions primarily involve performing a sequence of elementary calculations using basic arithmetic operations (+ − ×÷) to reach the final answer.
- A bright middle school student should be able to solve every problem: from the [paper](https://arxiv.org/abs/2110.14168), "Problems require no concepts beyond the level of early Algebra, and the vast majority of problems can be solved without explicitly defining a variable."
- Solutions are provided in natural language, as opposed to pure math expressions. From the [paper](https://arxiv.org/abs/2110.14168): "We believe this is the most generally useful data format, and we expect it to shed light on the properties of large language models' internal monologues."

## Links

* Abstract: https://arxiv.org/abs/2110.14168
* Homepage: https://github.com/openai/grade-school-math
* Dataset: https://huggingface.co/datasets/openai/gsm8k
* License: [MIT](https://huggingface.co/datasets/openai/gsm8k/blob/main/README.md)

## Example Questions

Below are 3 example questions. 2 from the training set which has 7.47k samples and 1 from the test set which has 1.32k samples.

<details>
<summary>Train Set - Question 1</summary>

Problem: Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?

Solution: Natalia sold 48/2 = <<48/2=24>>24 clips in May. Natalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May. 

Final Answer: 72
</details>

<details>
<summary>Train Set - Question 2</summary>

Problem: Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?

Solution:  How much did she earn?
Weng earns 12/60 = $<<12/60=0.2>>0.2 per minute.
Working 50 minutes, she earned 0.2 x 50 = $<<0.2*50=10>>10.

Final Answer: 10
</details>

<details>
<summary>Test Set - Question 1</summary>

Problem: Janet’s ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for $2 per fresh duck egg. How much in dollars does she make every day at the farmers' market?

Solution: Janet sells 16 - 3 - 4 = <<16-3-4=9>>9 duck eggs a day.
She makes 9 * 2 = $<<9*2=18>>18 every day at the farmer’s market.

Final Answer: 18
</details>

## Implementation

NOTE: See the official implementation of the task: https://github.com/openai/grade-school-math/blob/master/grade_school_math/calculator.py.

Below are [configurations](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/gsm8k) from [EleutherAI's Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness).


<details>
<summary>Zeroshot</summary>

```yaml
tag:
  - math_word_problems
task: gsm8k
dataset_path: gsm8k
dataset_name: main
output_type: generate_until
training_split: train
fewshot_split: train
test_split: test
doc_to_text: "Question: {{question}}\nAnswer:"
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
    - "Question:"
    - "</s>"
    - "<|im_end|>"
  do_sample: false
  temperature: 0.0
repeats: 1
num_fewshot: 5
filter_list:
  - name: "strict-match"
    filter:
      - function: "regex"
        regex_pattern: "#### (\\-?[0-9\\.\\,]+)"
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

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/gsm8k/gsm8k.yaml
</details>


<details>
<summary>CoT Zeroshot</summary>

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

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/gsm8k/gsm8k-cot-zeroshot.yaml
</details>

<details>
<summary>CoT n-shot</summary>

```yaml
dataset_name: main
dataset_path: gsm8k
doc_to_target: '{{answer.split(''####'')[-1].strip() if answer is defined else target}}'
doc_to_text: 'Q: {{question}}

  A:'
fewshot_config:
  sampler: first_n
  samples:
  - question: There are 15 trees in the grove. Grove workers will plant trees in the
      grove today. After they are done, there will be 21 trees. How many trees did
      the grove workers plant today?
    target: There are 15 trees originally. Then there were 21 trees after some more
      were planted. So there must have been 21 - 15 = 6. The answer is 6.
  - question: If there are 3 cars in the parking lot and 2 more cars arrive, how many
      cars are in the parking lot?
    target: There are originally 3 cars. 2 more cars arrive. 3 + 2 = 5. The answer
      is 5.
  - question: Leah had 32 chocolates and her sister had 42. If they ate 35, how many
      pieces do they have left in total?
    target: Originally, Leah had 32 chocolates. Her sister had 42. So in total they
      had 32 + 42 = 74. After eating 35, they had 74 - 35 = 39. The answer is 39.
  - question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12
      lollipops. How many lollipops did Jason give to Denny?
    target: Jason started with 20 lollipops. Then he had 12 after giving some to Denny.
      So he gave Denny 20 - 12 = 8. The answer is 8.
  - question: Shawn has five toys. For Christmas, he got two toys each from his mom and
      dad. How many toys does he have now?
    target: Shawn started with 5 toys. If he got 2 toys each from his mom and dad,
      then that is 4 more toys. 5 + 4 = 9. The answer is 9.
  - question: There were nine computers in the server room. Five more computers were
      installed each day, from monday to thursday. How many computers are now in the
      server room?
    target: There were originally 9 computers. For each of 4 days, 5 more computers
      were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29. The answer is
      29.
  - question: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday,
      he lost 2 more. How many golf balls did he have at the end of wednesday?
    target: Michael started with 58 golf balls. After losing 23 on tuesday, he had
      58 - 23 = 35. After losing 2 more, he had 35 - 2 = 33 golf balls. The answer
      is 33.
  - question: Olivia has $23. She bought five bagels for $3 each. How much money does
      she have left?
    target: Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15
      dollars. So she has 23 - 15 dollars left. 23 - 15 is 8. The answer is 8.
filter_list:
- filter:
  - function: regex
    regex_pattern: The answer is (\-?[0-9\.\,]+).
  - function: take_first
  name: strict-match
- filter:
  - function: regex
    group_select: -1
    regex_pattern: (-?[$0-9.,]{2,})|(-?[0-9]+)
  - function: take_first
  name: flexible-extract
generation_kwargs:
  do_sample: false
  until:
  - 'Q:'
  - </s>
  - <|im_end|>
tag:
- chain_of_thought
metadata:
  version: 3.0
metric_list:
- aggregation: mean
  higher_is_better: true
  ignore_case: true
  ignore_punctuation: false
  metric: exact_match
  regexes_to_ignore:
  - ','
  - \$
  - '(?s).*#### '
  - \.$
num_fewshot: 8
output_type: generate_until
repeats: 1
task: gsm8k_cot
test_split: test
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/gsm8k/gsm8k-cot.yaml
</details>

<details>
<summary>CoT Self-Consistency</summary>

```yaml
include: gsm8k-cot.yaml
tag:
  - chain_of_thought
  - self_consistency
task: gsm8k_cot_self_consistency
generation_kwargs:
  until:
    - "Q:"
    - "\n\n"
  do_sample: true
  temperature: 0.2
repeats: 64
filter_list:
  - name: "score-first" # pick only the first response, and report metrics on that
    filter:
      - function: "regex"
        regex_pattern: "The answer is (\\-?[0-9\\.\\,]*[0-9]+)"
      - function: "take_first"
  - name: "maj@64"
    filter:
      - function: "regex"
        regex_pattern: "The answer is (\\-?[0-9\\.\\,]*[0-9]+)"
      - function: "majority_vote"
      - function: "take_first"
  - name: "maj@8" # get Maj@8 , via selecting the first 8 responses. Using a better estimator would be optimal.
    filter:
      - function: "take_first_k"
        k: 8
      - function: "regex"
        regex_pattern: "The answer is (\\-?[0-9\\.\\,]*[0-9]+)"
      - function: "majority_vote"
      - function: "take_first"
metadata:
  version: 2.0
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/gsm8k/gsm8k-cot-self-consistency.yaml
</details>


## Citation

```
@misc{cobbe2021trainingverifierssolvemath,
      title={Training Verifiers to Solve Math Word Problems}, 
      author={Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Mark Chen and Heewoo Jun and Lukasz Kaiser and Matthias Plappert and Jerry Tworek and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},
      year={2021},
      eprint={2110.14168},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2110.14168}, 
}
```