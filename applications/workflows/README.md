# Workflows

Workflows are systems where Foundation Models (FMs) and tools are orchestrated through predefined code paths. They offer predictability and consistency for well-defined tasks.

Note: I use Foundation Models (FMs) to represent the superset which includes LLMs, Large Multimodal Models (LMMs) like Vision Language Models (VLMs) or other models involving speech, video or other forms.

### Routing

The routing workflow first classifies an input (`In`) with an `FM Call Router` and directs it to a specialized followup task (e.g. `FM Call 1`). This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs.

```mermaid
flowchart LR
    A([In]) --> B[FM Call Router]
    B --> C[FM Call 1]
    B -.-> D[FM Call 2]
    B -.-> E[FM Call 3]
    C --> F([Out])
    D -.-> F
    E -.-> F
```

**When to use this workflow**: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an FM or a more traditional classification model/algorithm (e.g. a BERT model with a classification head or even a classical machine learning model).

Examples where routing is useful:

1. My team used a routing workflow for one of our QA chatbots. The call router was a supervised BERT model (eventually replaced by a more performant and low-cost smol FM) doing [Dialogue Act Classification (DAC)](https://paperswithcode.com/task/dialogue-act-classification), where we differentiated whether the query/question required retrieval from a RAG system, did not require retrieval (i.e. was a follow up question that could be answered with previous context) or was irrelevant to this chatbot's domain. Then the query was routed to a separate downstream process (`FM Call x`).
2. Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools.
3. Routing easy/common questions to smaller models (less capable FMs) and hard/unusual questions to more capable models (Frontier models) to optimize cost and speed.

### Parallelization

The parallelization workflow puts FMs to work simultaneously on a task and have their outputs aggregated programmatically. There are 2 key variations:

- **Sectioning**: Breaking a task into independent subtasks run in parallel.
- **Voting**: Running the same task multiple times to get diverse outputs.

```mermaid
flowchart LR
    A([In]) --> C[FM Call 1]
    A --> D[FM Call 2]
    A --> E[FM Call 3]
    C --> B[Aggregator]
    D --> B
    E --> B
    B --> F([Out])
```

**When to use this workflow**: Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results (combining multiple generations can lead to a higher rate of success in solving the task, see the [pass@k metric](../../evaluation/metrics/pass@k.md)). For complex tasks with multiple considerations, FMs generally perform better when each consideration is handled by a separate FM call, allowing focused attention on each specific aspect.

Examples where parallelization is useful:

1. *Sectioning.* Implementing guardrails where one model instance processes user queries while another screens them for inappropriate content or requests. This tends to perform better than having the same FM call handle both guardrails and the core response.
2. *Sectioning.* Automating evals for evaluating FM performance, where each FM call evaluates a different aspect of the model’s performance on a given prompt.
3. *Voting.* Reviewing a piece of code for vulnerabilities, where several different prompts review and flag the code if they find a problem.
4. *Voting.* Evaluating whether a given piece of content is inappropriate, with multiple prompts evaluating different aspects or requiring different vote thresholds to balance false positives and negatives.

The above workflows heavily reference Anthropic's [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) blog post by Schluntz et al. (Dec 2024).