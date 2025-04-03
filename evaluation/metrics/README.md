## Metrics

- [pass@k](pass@k.md) - applied to determine functional correctness in coding benchmarks with unit tests and increasingly to reduce the variability for generative benchmarks (i.e. with pass@1) using non-zero temperatures and sampling rather than greedy decoding.
- [pass^k](pass^k.md) - a metric to evaluate the reliability of agent behavior over multiple trials.

## Inference Techniques

- [n-shot Prompting](../../inference/techniques/nshot.md) - the method of conditioning a language model with *n* example pairs that demonstrate the desired task, guiding the model to produce outputs consistent with the provided examples. Increasing the number of examples can help clarify task expectations and often leads to better performance. 0-shot prompting is a special case where only instructions are provided, without any examples.
- [Chain-of-Thought Prompting](../../inference/techniques/cot.md) - encourages language models to generate intermediate reasoning steps before arriving at a final answer. This technique helps models break down complex problems into manageable sub-steps, improving performance on tasks that require multi-step reasoning.
- [ReAct Prompting](../../inference/techniques/react_prompting.md) - ReAct (Reason + Act) is a framework where LLMs are conditioned (via prompt exemplars) to generate both reasoning traces and task-specific actions in an interleaved manner.