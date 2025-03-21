# SimpleQA

SimpleQA is a factuality benchmark that measures the ability for language models to answer short, fact-seeking questions and was developed by Wei at al. from OpenAI in Oct 2024. It's goal was to create a dataset with the following properties:

- **High correctness.** Reference answers to questions are supported by sources from two independent AI trainers, and questions were written in such a way that the predicted answers are easy to grade. 
- **Diversity.** SimpleQA covers a wide range of topics, from science and technology to TV shows and video games.
- **Challenging for frontier models.** Compared to older benchmarks such as TriviaQA⁠ (2017) or NQ (2019), which have become saturated, SimpleQA was created to be a greater challenge for frontier models (e.g., GPT‑4o scores less than 40%).
- **Good researcher UX.** SimpleQA is intended to be fast and simple to run due to its concise questions and answers. Grading is also efficient whether through the OpenAI API or another frontier model API. Additionally, with 4,326 questions, SimpleQA should have relatively low variance as an evaluation benchmark.

## Methodology

1. The first set of AI trainers browsed the web and created short, fact-seeking questions and corresponding answers. Each question had to meet a strict set of criteria: it must have a single, indisputable answer for easy grading; the answer to the question should not change over time; and most questions had to induce hallucinations from either GPT‑4o or GPT‑3.5. 
2. A second set of independent AI trainers answered each question without seeing the original response. Only questions where both AI trainers’ answers agreed were included.
3. A third AI trainer answered a random sample of 1,000 questions from the dataset. The third AI trainer’s answer matched the original agreed answers 94.4% of the time, with a 5.6% disagreement rate. 2.8% of the 5.6% of disagreements were due to grader false negatives or human errors from the third trainer (e.g., incomplete answers or misinterpreting sources), and the remaining 2.8% were due to real issues with the question (e.g., ambiguous questions, or different websites giving conflicting answers). 
4. The inherent error rate of this dataset is approximately 3%.

## Links

* Abstract: https://arxiv.org/abs/2411.04368v1
* Homepage: https://openai.com/index/introducing-simpleqa/
* Code: https://github.com/openai/simple-evals/blob/main/simpleqa_eval.py
* Dataset: https://huggingface.co/datasets/basicv8vc/SimpleQA
* License: [MIT](https://github.com/openai/simple-evals/tree/main?tab=MIT-1-ov-file#readme)

## Citation

```
@misc{wei2024measuringshortformfactualitylarge,
      title={Measuring short-form factuality in large language models}, 
      author={Jason Wei and Nguyen Karina and Hyung Won Chung and Yunxin Joy Jiao and Spencer Papay and Amelia Glaese and John Schulman and William Fedus},
      year={2024},
      eprint={2411.04368},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2411.04368}, 
}
```