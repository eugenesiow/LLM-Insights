# Evaluation

Evaluations generally consist of some datasets with ground truth answers and some code to run them (e.g. an evaluation harness).

Some general points on evaluations:
- Many evaluations are designed to run on base models. 
    - When they are run on base models, their prompts should be setup in such a way that base models can answer the questions by continuing the generation.
- Evaluations that expect fixed outputs like multiple-choice-questions or classification with a fixed set of classes (e.g. sentiment analysis) usually will set the max number of tokens, truncate outputs by setting stop tokens or evaluate based on the log likelihood of the output tokens of the class.
- Some evaluations (e.g. reasoning evals) can be setup to measure zero-shot or n-shot Chain of Thought (CoT) performances.
- LLM-as-a-Judge is another popular method of evaluation. It uses a judge LLM to verify if the output answer is correct.