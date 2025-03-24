# Trivia QA

TriviaQA, or Trivia Question Answering, was developed by Joshi et al. from the University of Washington and Ai2 and published in the paper [TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension](https://arxiv.org/abs/1705.03551) in May 2017. It is a reading comprehension dataset containing over 650K question-answer-evidence triples. It includes 95K question-answer pairs authored by trivia enthusiasts and independently gathered evidence documents, six per question on average, that provide high quality distant supervision for answering the questions.

## Links

* Abstract: https://arxiv.org/abs/1705.03551
* Homepage: https://nlp.cs.washington.edu/triviaqa/
* Dataset: https://huggingface.co/datasets/trivia_qa
* License: [Apache 2.0](https://github.com/mandarjoshi90/triviaqa?tab=Apache-2.0-1-ov-file#readme)

## Example Questions

<details>
<summary>Question: The Dodecanese Campaign of WWII that was an attempt by the Allied forces to capture islands in the Aegean Sea was the inspiration for which acclaimed 1961 commando film?</summary>

Answer: The Guns of Navarone

Excerpt: The Dodecanese Campaign of World War II was an attempt by Allied forces to capture the Italian-held Dodecanese islands in the Aegean Sea following the surrender of Italy in September 1943, and use them as bases against the German-controlled Balkans. The failed campaign, and in particular the Battle of Leros, inspired the 1957 novel The Guns of Navarone and the successful 1961 movie of the same name.
</details>

<details>
<summary>Question: American Callan Pinckney’s eponymously named system became a best-selling (1980s-2000s) book/video franchise in what genre?</summary>

Answer: Fitness

Excerpt: Callan Pinckney was an American fitness professional. She achieved unprecedented success with her Callanetics exercises. Her 9 books all became international best-sellers and the video series that followed went on to sell over 6 million copies. Pinckney’s first video release ”Callanetics: 10 Years Younger In 10 Hours” outsold every other fitness video in the US.
</details>

## Implementation

Below are [configurations](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/triviaqa) from [EleutherAI's Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness).

<details>
<summary>triviaqa/default</summary>

```yaml
task: triviaqa
dataset_path: trivia_qa
dataset_name: rc.nocontext
output_type: generate_until
training_split: train
validation_split: validation
doc_to_text: "Question: {{question}}?\nAnswer:"
doc_to_target: "{{answer.aliases}}"
should_decontaminate: true
doc_to_decontamination_query: question
generation_kwargs:
  until:
    - "\n"
    - "."
    - ","
  do_sample: false
  temperature: 0.0
filter_list:
  - name: remove_whitespace
    filter:
      - function: remove_whitespace
      - function: take_first
target_delimiter: " "
metric_list:
  - metric: exact_match
    aggregation: mean
    higher_is_better: true
    ignore_case: true
    ignore_punctuation: true
metadata:
  version: 3.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/triviaqa/default.yaml
</details>

## Citations

```bibtex
@InProceedings{JoshiTriviaQA2017,
    author = {Joshi, Mandar and Choi, Eunsol and Weld, Daniel S. and Zettlemoyer, Luke},
    title = {TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension},
    booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics},
    month = {July},
    year = {2017},
    address = {Vancouver, Canada},
    publisher = {Association for Computational Linguistics},
}
```