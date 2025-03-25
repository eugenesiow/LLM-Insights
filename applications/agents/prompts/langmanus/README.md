# LangManus

[LangManus](https://github.com/langmanus/langmanus) is an academically driven open-source project to explore ideas Multi-Agent and DeepResearch ideas. It is an AI automation framework that combines language models with specialized tools for tasks like web search, crawling, and Python code execution.

It builds on:
- [Qwen](https://github.com/QwenLM/Qwen) as the LLM of choice
- [Tavily](https://tavily.com/) for web search querying (requires API key)
- [Jina](https://jina.ai/) for embeddings and search
- [Browser-use](https://pypi.org/project/browser-use/) for controlling and automating browser use

## Prompts

The system consists of the following agents working together, their prompts (retrieved [25 Mar 2025](https://github.com/langmanus/langmanus/commit/53819ceea4d2273f749a4b24615d6a2513190964), [MIT License](https://github.com/langmanus/langmanus/tree/main?tab=MIT-1-ov-file#readme)) are linked below:

1. [Coordinator](coordinator.md) - The entry point that handles initial interactions and routes tasks
2. [Planner](planner.md) - Analyzes tasks and creates execution strategies
3. [Supervisor](supervisor.md) - Oversees and manages the execution of other agents
4. [Researcher](researcher.md) - Gathers and analyzes information
5. [Coder](coder.md) - Handles code generation and modifications
6. [Browser](browser.md) - Performs web browsing and information retrieval
7. [Reporter](reporter.md) - Generates reports and summaries of the workflow results