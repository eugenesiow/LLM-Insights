## Metrics

- [ANLS (Average Normalized Levenshtein Similarity) and ANLS*](anls.md) - metrics for evaluating document understanding and reasoning that are more robust to errors in the text recognition stage e.g. not overly penalising question-answering on images where the text recognition from images has errors.
- [ChrF (Character n-gram F-score) and ChrF++](chrf.md) - metrics for automatic evaluation of machine translation output. They measure the F-score for character n-gram matches. ChrF++ additionally adds word n-grams (unigrams and bigrams).
- Exact Match (EM) - a metric that measures how much of the model's responses perfectly match the correct answers.
- [pass@k](pass@k.md) - applied to determine functional correctness in coding benchmarks with unit tests and increasingly to reduce the variability for generative benchmarks (i.e. with pass@1) using non-zero temperatures and sampling rather than greedy decoding.
- [pass^k](pass^k.md) - a metric to evaluate the reliability of agent behavior over multiple trials.
## Inference Techniques

- [n-shot Prompting](../../inference/techniques/nshot.md) - the method of conditioning a language model with *n* example pairs that demonstrate the desired task, guiding the model to produce outputs consistent with the provided examples. Increasing the number of examples can help clarify task expectations and often leads to better performance. 0-shot prompting is a special case where only instructions are provided, without any examples.
- [Chain-of-Thought Prompting](../../inference/techniques/cot.md) - encourages language models to generate intermediate reasoning steps before arriving at a final answer. This technique helps models break down complex problems into manageable sub-steps, improving performance on tasks that require multi-step reasoning.
- [ReAct Prompting](../../inference/techniques/react_prompting.md) - ReAct (Reason + Act) is a framework where LLMs are conditioned (via prompt exemplars) to generate both reasoning traces and task-specific actions in an interleaved manner.