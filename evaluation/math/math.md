# MATH

MATH is a dataset of 12,500 challenging competition mathematics problems compiled by Hendrycks et al. from UC Berkeley and published with the [Measuring Mathematical Problem Solving With the MATH Dataset](https://arxiv.org/abs/2103.03874) paper in Mar to Nov 2021. Each problem in MATH has a full step-by-step solution which can be used to teach models to generate answer derivations and explanations. 

MATH-500 is a 500 sample split of the Hendrycks et al. MATH test set. It was used in OpenAI's [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) paper by Lightman et al. in May 2023. Out of the 12,500 problems in MATH, 7,500 were in the training set while 5,000 were in the test set. OpenAI took 4,500 of the MATH test split problems and included them in the training set leaving the remaining 500 held-out problems for MATH-500. They selected these 500 test problems uniformly at random, which they felt were representative of the test set as a whole.

It's an extremely widely used benchmark (MATH or MATH-500) and [almost every frontier model](../README.md) benchmarks on it.

## Links

### MATH

* Abstract: https://arxiv.org/abs/2103.03874
* Homepage: https://github.com/hendrycks/math
* Dataset: https://huggingface.co/datasets/hendrycks/competition_math - This dataset [received](https://huggingface.co/datasets/hendrycks/competition_math/discussions/5) a [DMCA Takedown notice](https://huggingface.co/datasets/huggingface-legal/takedown-notices/blob/main/2025/2025-01-02-AoPS.md) from the [Art of Problem Solving (AoPS)](https://artofproblemsolving.com/) alleging that part of the dataset contained AoPS Incorporated's intellectual property that was shared without their knowledge or permission.
* Dataset: https://huggingface.co/datasets/EleutherAI/hendrycks_math
* License: [MIT](https://huggingface.co/datasets/hendrycks/competition_math) (Some issues, see the [DMCA Takedown notice](https://huggingface.co/datasets/huggingface-legal/takedown-notices/blob/main/2025/2025-01-02-AoPS.md))

### MATH-500

* Abstract: https://arxiv.org/abs/2305.20050
* Dataset: https://huggingface.co/datasets/HuggingFaceH4/MATH-500
* License: [Unknown](https://huggingface.co/datasets/HuggingFaceH4/MATH-500/discussions/2)

## Example Questions

Below are 3 example questions. They are from the MATH-500 test set.

<details>
<summary>test/number_theory/572</summary>

Problem: How many positive whole-number divisors does 196 have?

Solution: First prime factorize $196=2^2\cdot7^2$. The prime factorization of any divisor of 196 cannot include any primes other than 2 and 7. We are free to choose either 0, 1, or 2 as the exponent of 2 in the prime factorization of a divisor of 196. Similarly, we may choose 0, 1, or 2 as the exponent of 7. In total, there are $3\times 3=9$ possibilities for the prime factorization of a divisor of 196. Distinct prime factorizations correspond to distinct integers, so there are $\boxed{9}$ divisors of 196.

Answer: 9

Level: 3
</details>

<details>
<summary>test/algebra/2584</summary>

Problem: If $f(x) = \frac{3x-2}{x-2}$, what is the value of $f(-2) +f(-1)+f(0)$? Express your answer as a common fraction.

Solution: $f(-2)+f(-1)+f(0)=\frac{3(-2)-2}{-2-2}+\frac{3(-1)-2}{-1-2}+\frac{3(0)-2}{0-2}=\frac{-8}{-4}+\frac{-5}{-3}+\frac{-2}{-2}=2+\frac{5}{3}+1=\boxed{\frac{14}{3}}$

Answer: $\frac{14}{3}$

Level: 3
</details>

<details>
<summary>test/intermediate_algebra/134</summary>

Problem: Compute: $1-2+3-4+5- \dots +99-100$.

Solution: $(1-2)+(3-4)+ \dots +(97-98)+(99-100) = 50(-1) = \boxed{-50}.$

Answer: -50

Level: 1
</details>

## Implementation

NOTE: See the official implementation of the task: https://github.com/hendrycks/math/blob/main/modeling/eval_math_gpt.py.

Below are configurations from [EleutherAI's Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness).


<details>
<summary>default</summary>

```yaml
dataset_path: EleutherAI/hendrycks_math
process_docs: !function utils.process_docs
output_type: generate_until
training_split: train
test_split: test
doc_to_text:  !function utils.doc_to_text
process_results: !function utils.process_results
doc_to_target: "{{answer if few_shot is undefined else solution}}"
generation_kwargs:
  until:
    - "Problem:"
  do_sample: false
  temperature: 0
  max_gen_toks: 1024
metric_list:
  - metric: exact_match
    aggregation: mean
    higher_is_better: true
num_fewshot: 4
metadata:
  version: 2.0
dataset_kwargs:
  trust_remote_code: true
fewshot_config:
  sampler: first_n
  samples: !function utils.list_fewshot_samples
```

Adapted From: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/leaderboard/math/_template_yaml
</details>

<details>
<summary>hendrycks_math_algebra</summary>

```yaml
tag:
  - math_word_problems
task: hendrycks_math_algebra
dataset_path: EleutherAI/hendrycks_math
process_docs: !function utils.process_docs
dataset_name: algebra
output_type: generate_until
training_split: train
test_split: test
doc_to_text:  "Problem: {{problem}}\nAnswer:"
process_results: !function utils.process_results
doc_to_target: "{{answer}}"
generation_kwargs:
  until:
    - "Problem:"
  do_sample: false
  temperature: 0
metric_list:
  - metric: exact_match
    aggregation: mean
    higher_is_better: true
metadata:
  version: 1.0
dataset_kwargs:
  trust_remote_code: true
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/hendrycks_math/hendrycks_math_algebra.yaml
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