# Instruct Models Evaluation

- [Instruct Models Evaluation](#instruct-models-evaluation)
  - [Truthfulness](#truthfulness)
    - [TruthfulQA](#truthfulqa)
  - [Commonsense Reasoning Tasks](#commonsense-reasoning-tasks)
    - [HellaSwag](#hellaswag)
    - [OBQA](#obqa)
    - [WinoGrande](#winogrande)
    - [ARC](#arc)
    - [BoolQ](#boolq)
    - [PIQA](#piqa)

The types of evaluations and the models evaluated are not meant to be exhaustive, there are leaderboards like the [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) for that. What is presented is a set of quantitative evaluations that we used to sanity check our models during training, comparing them against the leading instruction-tuned models of that parameter count were performing.

Running each of these evaluations on our own (even if results have previously been reported somewhere) let's us work out any kinks in the evaluation code base (e.g. multi-GPU, different architectures, etc.) on our own hardware.

## Truthfulness

### TruthfulQA

| Model                    | MC1   | MC2   | Avg   |
|--------------------------|-------|-------|-------|
| [openhermes2.5_mistral_7b](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B) | 36.11 | 53.07 | 44.59 |
| [llama2_chat_13b](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf)          | 28.03 | 43.95 | 35.99 |
| [orca2_13b](https://huggingface.co/microsoft/Orca-2-13b)                | **39.17** | **55.76** | **47.47** |
| [llama2_chat_70b](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf)          | 35.74 | 52.77 | 44.26 |

There are two parts to the [TruthfulQA](https://github.com/sylinrl/TruthfulQA) evaluation. There is a main generation task, which measures the truthfulness and informativeness of generated answers. However, this is difficult to evaluate automatically (the usual metrics like BLEURT, ROUGE, and BLEU as well as GPT-judge can be used), this is **NOT INCLUDED** in the above evaluations. There is also an alternative multiple-choice option where the model is evaluated based on its ability to identify true statements from a list of multiple-choice statements. 

The two metrics, MC1 and MC2 are described below:

- MC1 (Single-true): Given a question and 4-5 answer choices, select the only correct answer. The model's selection is the answer choice to which it assigns the highest log-probability of completion following the question, independent of the other answer choices. The score is the simple accuracy across all questions.
- MC2 (Multi-true): Given a question and multiple true / false reference answers, the score is the normalized total probability assigned to the set of true answers. 

From the paper, [TruthfulQA: Measuring How Models Mimic Human Falsehoods](https://arxiv.org/abs/2109.07958).

## Commonsense Reasoning Tasks

| Model                    | Avg   | [HellaSwag](#hellaswag) | [OBQA](#obqa)  | [WinoGrande](#winogrande) | [ARC_c](#arc) | [ARC_e](#arc) | [BoolQ](#boolq) | [PIQA](#piqa)  |
|--------------------------|-----------|-------|------------|-------|-------|-------|-------|-------|
| [openhermes2.5_mistral_7b](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B) | 70.61 | 78.53     | 46.2  | 74.43      | 53.07 | 75.93 | 88.29 | 77.8  |
| [llama2_chat_13b](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf)          | 72.97 | 81.74     | 44.2  | 74.27      | 59.98 | 81.52 | 86.61 | 82.48 |
| [orca2_13b](https://huggingface.co/microsoft/Orca-2-13b)                | 68.46 | 79.65     | 44.00 | 70.96      | 50.17 | 73.74 | 81.62 | 79.11 |
| [llama2_chat_70b](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf)          | 71.53 | 82.15     | 45.40 | 74.98      | 54.27 | 76.30 | 86.73 | 80.90 |

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