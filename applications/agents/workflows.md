# Workflows

Workflows are systems where LLMs and tools are orchestrated through predefined code paths. They offer predictability and consistency for well-defined tasks.

### Routing

```mermaid
flowchart LR
    A([In]) --> B[LLM Call Router]
    B --> C[LLM Call 1]
    B -.-> D[LLM Call 2]
    B -.-> E[LLM Call 3]
    C --> F([Out])
    D -.-> F
    E -.-> F
```

The above workflows heavily reference Anthropic's [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) blog post by Schluntz et al. (Dec 2024).