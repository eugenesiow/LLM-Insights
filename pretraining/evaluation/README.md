# Base Model Evaluation

- [Base Model Evaluation](#base-model-evaluation)
  - [Problem Solving](#problem-solving)
    - [MMLU](#mmlu)
    - [BBH](#bbh)
    - [HumanEval](#humaneval)
    - [DROP](#drop)
  - [Commonsense Reasoning Tasks](#commonsense-reasoning-tasks)
    - [HellaSwag](#hellaswag)
    - [OBQA](#obqa)
    - [WinoGrande](#winogrande)
    - [ARC](#arc)
    - [BoolQ](#boolq)
    - [PIQA](#piqa)

The types of evaluations and the models evaluated are not meant to be exhaustive, there are leaderboards like the [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) for that. What is presented is a basic set of evaluations that we used to sanity check our models during training, comparing them against how the leading (or most popular) base models of that parameter count were performing.

Running each of these evaluations on our own (even if results have previously been reported somewhere) let's us work out any kinks in the evaluation code base (e.g. multi-GPU, different architectures, etc.) on our own hardware.

## Problem Solving

The [instruct-eval](https://github.com/declare-lab/instruct-eval) harness provides a consistent way to execute a suite of 4 problem solving benchmarks, [MMLU](#mmlu), [BBH](#bbh), [HumanEval](#humaneval) and [DROP](#drop) for language and coding questions.

| Model                    | [MMLU](#mmlu)  | [BBH](#bbh)   | [HumanEval](#humaneval) | [Drop](#drop)  |
|--------------------------|-------|-------|-----------|-------|
| [btlm_3b_8k](https://huggingface.co/cerebras/btlm-3b-8k-base) | 28.01	| 30.79 |	10.98 |	17.87 |
| [llama2_7b](https://huggingface.co/meta-llama/Llama-2-7b-hf) | 45.96 | 32.04 | 14.02     | 31.57 |
| [mistral_7b_v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) | 62.61 | 43.99 | **23.78**     | 46.56 |
| [llama2_13b](https://huggingface.co/meta-llama/Llama-2-13b-hf) | 55.68 | 37.62 | 14.63     | 41.58 |
| [yi_34b](https://huggingface.co/01-ai/Yi-34B) | **76.34** | **52.15** | 17.68     | **74.65** |
| [llama2_70b](https://huggingface.co/meta-llama/Llama-2-70b-hf) | 69.12 | 50.46 | 17.68     | 62.53 |

### MMLU

[MMLU](https://arxiv.org/abs/2009.03300v3) benchmark is designed to measure world knowledge and problem-solving ability in multiple subjects.

### BBH

[BIG-Bench Hard (BBH)](https://github.com/google/BIG-bench) is a subset of 23 challenging tasks from the BIG-Bench benchmark, which focuses on tasks believed to be beyond the capabilities of current language models. It requires models to follow challenging instructions such as navigation, logical deduction, and fallacy detection.

### HumanEval

[HumanEval](https://github.com/openai/human-eval) is a problem-solving benchmark used for evaluating large language models trained on code.

### DROP

[Discrete Reasoning Over Paragraphs (DROP)](https://aclanthology.org/N19-1246/) is a math-based reading comprehension task that requires a system to perform discrete reasoning over passages extracted from Wikipedia articles.

## Commonsense Reasoning Tasks

| Model                    | Avg   | [HellaSwag](#hellaswag) | [OBQA](#obqa)  | [WinoGrande](#winogrande) | [ARC_c](#arc) | [ARC_e](#arc) | [BoolQ](#boolq) | [PIQA](#piqa)  |
|--------------------------|-----------|-------|------------|-------|-------|-------|-------|-------|
| [btlm_3b_8k](https://huggingface.co/cerebras/btlm-3b-8k-base) | 61.10 |69.66 | 40.8 |	65.82 |	37.63 |	66.92 |	69.48 |	77.42 |
| [llama2_7b](https://huggingface.co/meta-llama/Llama-2-7b-hf) | 66.71| 75.98     | 44.20 | 69.06      | 46.33 | 74.58 | 77.74 | 79.11  |
| [mistral_7b_v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) | 71.17| 81.01     | 44.20 | 74.11      | 53.67 | 79.46 | 83.61 | 82.15  |
| [llama2_13b](https://huggingface.co/meta-llama/Llama-2-13b-hf)| 69.28| 79.38     | 45.40 | 72.45      | 49.15 | 77.53 | 80.55 | 80.52  |
| [yi_34b](https://huggingface.co/01-ai/Yi-34B) | **75.14** | 83.69     | 46.60 | **78.93**      | **61.52** | **84.26** | **88.32** | 82.64  |
| [llama2_70b](https://huggingface.co/meta-llama/Llama-2-70b-hf)| 73.61 | **83.81** |	**48.80** |	77.98 |	57.25 |	80.98 |	83.7 |	82.75 |

### HellaSwag

From the paper, [HellaSwag: Can a Machine Really Finish Your Sentence?](https://arxiv.org/abs/1905.07830).

### OBQA

[OpenBookQA (OBQA)](https://github.com/allenai/OpenBookQA) is an open book question answering dataset and benchmark.

From the paper, [Can a Suit of Armor Conduct Electricity? A New Dataset for Open Book Question Answering](https://www.semanticscholar.org/paper/24c8adb9895b581c441b97e97d33227730ebfdab).

### WinoGrande

[WinoGrande](https://github.com/allenai/winogrande) from the paper [WinoGrande: An Adversarial Winograd Schema Challenge at Scale](https://arxiv.org/abs/1907.10641).

### ARC

The [AI2's Reasoning Challenge (ARC)](https://allenai.org/data/arc) dataset is a multiple-choice question-answering dataset, containing questions from science exams from grade 3 to grade 9. The dataset is split in two partitions: Easy (ARC_e) and Challenge (ARC_c), where the latter partition contains the more difficult questions that require reasoning. Most of the questions have 4 answer choices, with <1% of all the questions having either 3 or 5 answer choices. 

### BoolQ

[BoolQ](https://github.com/google-research-datasets/boolean-questions) is a question answering dataset for yes/no questions containing 15942 examples. These questions are naturally occurring ---they are generated in unprompted and unconstrained settings.

From the paper, [BoolQ: Exploring the Surprising Difficulty of Natural Yes/No Questions](https://arxiv.org/abs/1905.10044).

### PIQA

[Physical Interaction QA (PIQA)](https://github.com/ybisk/ybisk.github.io/tree/master/piqa) is a dataset for commonsense reasoning, and was created to investigate the physical knowledge of models.

PIQA is a commonsense QA benchmark for naive physics reasoning focusing on how we interact with everyday objects in everyday situations. This dataset focuses on affordances of objects, i.e., what actions each physical object affords (e.g., it is possible to use a shoe as a doorstop), and what physical interactions a group of objects afford (e.g., it is possible to place an apple on top of a book, but not the other way around). The dataset requires reasoning about both the prototypical use of objects (e.g., shoes are used for walking) and non-prototypical but practically plausible use of objects (e.g., shoes can be used as a doorstop). The dataset includes 20,000 QA pairs that are either multiple-choice or true/false questions.

From the paper, [PIQA: Reasoning about Physical Commonsense in Natural Language](https://arxiv.org/abs/1911.11641v1).