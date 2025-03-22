# Evaluation

Evaluations generally consist of some datasets with ground truth answers and some code to run them (e.g. an evaluation harness).

## Evaluating Capabilities

1. [General](general/) - knowledge, language ability (e.g. reading comprehesion), broad/multi-domain.
2. [Steerability](steerability/) - instruction-following ability.
3. [Math](math/) - solving math problems, math reasoning or math programming problems.
4. [Reasoning](reasoning/) - logical thinking, making inferences, and drawing conclusions from given information; usually harder problems require multiple steps.
5. [Coding](coding/) - writing programming code, doing software engineering and developing applications.
6. [Factuality](factuality/) - ability to produce accurate and truthful information.
7. [Multilingual](multilingual/) - performance on languages other than English and especially on low-resource languages.
8. [Image](image/) - multimodal image understanding, knowledge, advanced perception and multimodal reasoning ability.
9. [Audio](audio/) - multimodal audio understanding, end-to-end speech-to-text translation, etc.
10. [Video](video/) - multimodal video language understanding, long-form video understanding, etc.

## Evaluation Coverage

| Capability              | Evaluation Benchmark | License    | o3-mini | claude-3.7-sonnet | gemini-2.0 | llama-3.3 | grok-2 | mistral-small-3.1 | olmo-2 | openllm-leaderboard |
|-------------------------|----------------------|------------|---------|-------------------|------------|-----------|--------|-------------------|--------|---------------------|
| Math                    | [MATH](math/math.md)                 | MIT        | ✓       | ✓                 | ✓          | ✓         | ✓      | ✓                 | ✓      | ✓                   |
| Reasoning               | [GPQA](reasoning/gpqa.md)                 | CC-BY-4.0  | ✓       | ✓                 | ✓          | ✓         | ✓      | ✓                 |        | ✓                   |
| General                 | [MMLU](general/mmlu.md)                 | MIT        | ✓       |                   |            | ✓         | ✓      | ✓                 | ✓      |                     |
| General                 | [MMLU-Pro](general/mmlu.md)             | MIT        |         |                   | ✓          | ✓         | ✓      | ✓                 |        | ✓                   |
| Steerability            | [IFEval](steerability/ifeval.md)               | Apache 2.0 |         | ✓                 |            | ✓         |        |                   | ✓      | ✓                   |
| Image                   | [MMMU](image/mmmu.md)                 | Apache 2.0           |         | ✓                 | ✓          |           | ✓      | ✓                 |        |                     |
| Coding                  | [HumanEval](coding/humaneval.md)            | MIT           |         |                   |            | ✓         | ✓      | ✓                 |        |                     |
| Factuality              | [SimpleQA](factuality/simpleqa.md)             | MIT           | ✓       |                   | ✓          |           |        | ✓                 |        |                     |
| General                 | [BBH](general/bbh.md)                  | MIT        |         |                   |            |           |        |                   | ✓      | ✓                   |
| Math                    | AIME24               | MIT        | ✓       | ✓                 |            |           |        |                   |        |                     |
| Math                    | [GSM8K](math/gsm8k.md)                | MIT        |         |                   |            | ✓         |        |                   | ✓      |                     |
| Code                    | LiveCodeBench (v5)   |            | ✓       |                   | ✓          |           |        |                   |        |                     |
| Coding                  | SWE-Bench Verified   |            | ✓       | ✓                 |            |           |        |                   |        |                     |
| Multilingual            | [MGSM](multilingual/mgsm.md)                 | CC-BY-SA-4.0            | ✓       |                   |            | ✓         |        |                   |        |                     |
| Image                   | MathVista            |            |         |                   |            |           | ✓      | ✓                 |        |                     |
| Image                   | DocVQA               |            |         |                   |            |           | ✓      | ✓                 |        |                     |
| General                 | TriviaQA             |            |         |                   |            |           |        | ✓                 |        |                     |
| Reasoning               | DROP                 |            |         |                   |            |           |        |                   | ✓      |                     |
| Steerability            | AlpacaEval V2        |            |         |                   |            |           |        |                   | ✓      |                     |
| General                 | PopQA                |            |         |                   |            |           |        |                   | ✓      |                     |
| Math                    | HiddenMath           | -          |         |                   | ✓          |           |        |                   |        |                     |
| Math                    | FrontierMath         |            | ✓       |                   |            |           |        |                   |        |                     |
| Code                    | Codeforces           |            | ✓       |                   |            |           |        |                   |        |                     |
| Reasoning               | [ARC Challenge](reasoning/arc.md)        | CC-BY-SA-4.0           |         |                   |            | ✓         |        |                   |        |                     |
| Reasoning, Long-context | MUSR                 |            |         |                   |            |           |        |                   |        | ✓                   |
| Long-context            | MRCR (1M)            |            |         |                   | ✓          |           |        |                   |        |                     |
| Code                    | Bird-SQL (Dev)       |            |         |                   | ✓          |           |        |                   |        |                     |
| Code                    | MBPP EvalPlus        |            |         |                   |            | ✓         |        |                   |        |                     |
| Factuality              | FACTS Grounding      |            |         |                   | ✓          |           |        |                   |        |                     |
| Factuality              | TruthfulQA           |            |         |                   |            |           |        |                   | ✓      |                     |
| Multilingual            | Global MMLU (Lite)   |            |         |                   | ✓          |           |        |                   |        |                     |
| Multilingual            | MMMLU                |            |         | ✓                 |            |           |        |                   |        |                     |
| Image                   | MMMU-Pro             |            |         |                   |            |           |        | ✓                 |        |                     |
| Image                   | MM-MT-Bench          |            |         |                   |            |           |        | ✓                 |        |                     |
| Image                   | ChartQA              |            |         |                   |            |           |        | ✓                 |        |                     |
| Image                   | AI2D                 |            |         |                   |            |           |        | ✓                 |        |                     |
| Audio                   | CoVoST2 (21 lang)    |            |         |                   | ✓          |           |        |                   |        |                     |
| Video                   | EgoSchema (test)     |            |         |                   | ✓          |           |        |                   |        |                     |
| Agentic                 | TAU-Bench            |            |         | ✓                 |            |           |        |                   |        |                     |
| Tool Use                | BFCLv2               |            |         |                   |            | ✓         |        |                   |        |                     |
| Tool Use                | Nexus                |            |         |                   |            | ✓         |        |                   |        |                     |
| Long-context            | ZeroSCROLLS/QuALITY  |            |         |                   |            | ✓         |        |                   |        |                     |
| Long-context            | InfiniteBench/En.MC  |            |         |                   |            | ✓         |        |                   |        |                     |
| Long-context            | NIH/Multi-needle     |            |         |                   |            | ✓         |        |                   |        |                     |
| Long-context            | LongBench v2         |            |         |                   |            |           |        | ✓                 |        |                     |
| Long-context            | RULER                |            |         |                   |            |           |        | ✓                 |        |                     |
| Safety                  | XSTest               |            | ✓       |                   |            |           |        |                   |        |                     |
| Safety                  | Tülu 3 Safety        |            |         |                   |            |           |        |                   | ✓      |                     |
| Hallucinations          | PersonQA             |            | ✓       |                   |            |           |        |                   |        |                     |
| Jailbreaking            | StrongREJECT         |            | ✓       |                   |            |           |        |                   |        |                     |
| Code, Reasoning         | IOI                  | CC-BY      |         |                   |            |           |        |                   |        |                     |
| Code                    | CodeELO              |            |         |                   |            |           |        |                   |        |                     |
| Reasoning               | SuperGPQA            |            |         |                   |            |           |        |                   |        |                     |
| Code                    | SWE-Lancer           |            |         |                   |            |           |        |                   |        |                     |

## General Notes

Some general points on evaluations:
- Many evaluations are designed to run on base models. 
    - When they are run on base models, their prompts should be setup in such a way that base models can answer the questions by continuing the generation.
- Evaluations that expect fixed outputs like multiple-choice-questions or classification with a fixed set of classes (e.g. sentiment analysis) usually will set the max number of tokens, truncate outputs by setting stop tokens or evaluate based on the log likelihood of the output tokens of the class.
- Some evaluations (e.g. reasoning evals) can be setup to measure zero-shot or n-shot Chain of Thought (CoT) performances.
- LLM-as-a-Judge is another popular method of evaluation. It uses a judge LLM to verify if the output answer is correct.