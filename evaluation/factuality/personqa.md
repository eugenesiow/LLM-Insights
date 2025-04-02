# PersonQA

PersonQA is an OpenAI, currently unpublished (private), benchmark. It was reported in the OpenAI [o3-mini system card](https://openai.com/index/o3-mini-system-card/). It is an evaluation that aims to elicit hallucinations. In the system card report, OpenAI describes PersonQA as a dataset of questions and publicly available facts about people that measures the model's accuracy on attempted answers.

The following table shows the evaluation on PersonQA done for GPT-4o, o1-mini, and o3-mini. 

| Metric                                | GPT 4o-mini | o1-mini | o3-mini |
|---------------------------------------|------------|---------|---------|
| PersonQA accuracy (higher is better)  | 28.4%      | 19.6%   | 21.7%   |
| PersonQA hallucination rate (lower is better) | 52.4% | 27.4%   | 14.8%   |

- accuracy (did the model answer the question correctly)
- hallucination rate (checking how often the model hallucinated)