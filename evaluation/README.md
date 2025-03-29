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

The following is a curated benchmark list covering a range of model capabilities. The benchmarks are **ranked based on how many frontier models evaluated on them**.

| Capability              | Evaluation                                  | License         | o3-mini | claude-3.7-sonnet | gemini-2.5 | gemini-2.0 | llama-3.3 | grok-2 | mistral-small-3.1 | olmo-2 | openllm-leaderboard | deepseek-r1 |
|-------------------------|---------------------------------------------|-----------------|---------|-------------------|------------|------------|-----------|--------|-------------------|--------|---------------------|-------------|
| Math                    | [MATH](math/math.md)                        | MIT             | ✓       | ✓                 |            | ✓          | ✓         | ✓      | ✓                 | ✓      | ✓                   | ✓           |
| Reasoning               | [GPQA](reasoning/gpqa.md)                   | CC-BY-4.0       | ✓       | ✓                 | ✓          | ✓          | ✓         | ✓      | ✓                 |        | ✓                   | ✓           |
| General                 | [MMLU](general/mmlu.md)                     | MIT             | ✓       |                   |            |            | ✓         | ✓      | ✓                 | ✓      |                     | ✓           |
| General                 | [MMLU-Pro](general/mmlu.md)                 | MIT             |         |                   |            | ✓          | ✓         | ✓      | ✓                 |        | ✓                   | ✓           |
| Steerability            | [IFEval](steerability/ifeval.md)            | Apache 2.0      |         | ✓                 |            |            | ✓         |        |                   | ✓      | ✓                   | ✓           |
| Factuality              | [SimpleQA](factuality/simpleqa.md)          | MIT             | ✓       |                   | ✓          | ✓          |           |        | ✓                 |        |                     | ✓           |
| Image                   | [MMMU](image/mmmu.md)                       | Apache 2.0      |         | ✓                 | ✓          | ✓          |           | ✓      | ✓                 |        |                     |             |
| Math                    | [AIME24](math/aime.md)                      | Unknown ⚠️      | ✓       | ✓                 | ✓          |            |           |        |                   |        |                     | ✓           |
| Coding                  | [LiveCodeBench](coding/livecodebench.md)    | CC              | ✓       |                   | ✓          | ✓          |           |        |                   |        |                     | ✓           |
| Coding                  | [SWE-Bench](coding/swe_bench.md)                          | MIT                 | ✓       | ✓                 | ✓          |            |           |        |                   |        |                     | ✓           |
| Coding                  | [HumanEval](coding/humaneval.md)            | MIT             |         |                   |            |            | ✓         | ✓      | ✓                 |        |                     |             |
| General                 | [BBH](general/bbh.md)                       | MIT             |         |                   |            |            |           |        |                   | ✓      | ✓                   |             |
| Reasoning               | [DROP](reasoning/drop.md)                   | CC-BY-4.0       |         |                   |            |            |           |        |                   | ✓      |                     | ✓           |
| Steerability            | [AlpacaEval](steerability/alpacaeval.md)    | CC-BY-NC-4.0 ⚠️ |         |                   |            |            |           |        |                   | ✓      |                     | ✓           |
| Math                    | [GSM8K](math/gsm8k.md)                      | MIT             |         |                   |            |            | ✓         |        |                   | ✓      |                     |             |
| Coding                  | Codeforces                                  |                 | ✓       |                   |            |            |           |        |                   |        |                     | ✓           |
| Long-context            | MRCR                                        |                 |         |                   | ✓          | ✓          |           |        |                   |        |                     |             |
| Multilingual            | [Global MMLU](multilingual/global_mmlu.md)  | Apache 2.0      |         |                   | ✓          | ✓          |           |        |                   |        |                     |             |
| Multilingual            | [MGSM](multilingual/mgsm.md)                | CC-BY-SA-4.0 ⚠️ | ✓       |                   |            |            | ✓         |        |                   |        |                     |             |
| Image                   | MathVista                                   |                 |         |                   |            |            |           | ✓      | ✓                 |        |                     |             |
| Image                   | DocVQA                                      |                 |         |                   |            |            |           | ✓      | ✓                 |        |                     |             |
| Coding                  | [Aider-Polygot](coding/aider_polygot.md)                               | MIT                 |         |                   | ✓          |            |           |        |                   |        |                     | ✓           |
| General                 | [TriviaQA](general/triviaqa.md)             | Apache 2.0      |         |                   |            |            |           |        | ✓                 |        |                     |             |
| General                 | PopQA                                       |                 |         |                   |            |            |           |        |                   | ✓      |                     |             |
| Math                    | HiddenMath                                  | Unknown ⚠️      |         |                   |            | ✓          |           |        |                   |        |                     |             |
| Math                    | FrontierMath                                |                 | ✓       |                   |            |            |           |        |                   |        |                     |             |
| Reasoning               | [ARC Challenge](reasoning/arc.md)           | CC-BY-SA-4.0 ⚠️ |         |                   |            |            | ✓         |        |                   |        |                     |             |
| Reasoning, Long-context | MUSR                                        |                 |         |                   |            |            |           |        |                   |        | ✓                   |             |
| Coding                  | Bird-SQL (Dev)                              |                 |         |                   |            | ✓          |           |        |                   |        |                     |             |
| Coding                  | [MBPP EvalPlus](coding/mbpp.md)             | Apache 2.0      |         |                   |            |            | ✓         |        |                   |        |                     |             |
| Factuality              | FACTS Grounding                             |                 |         |                   |            | ✓          |           |        |                   |        |                     |             |
| Factuality              | [TruthfulQA](factuality/truthfulqa.md)      | Apache 2.0      |         |                   |            |            |           |        |                   | ✓      |                     |             |
| Multilingual            | MMMLU                                       |                 |         | ✓                 |            |            |           |        |                   |        |                     |             |
| Image                   | MMMU-Pro                                    |                 |         |                   |            |            |           |        | ✓                 |        |                     |             |
| Image                   | MM-MT-Bench                                 |                 |         |                   |            |            |           |        | ✓                 |        |                     |             |
| Image                   | [ChartQA](image/chartqa.md)                 | GPL-3.0 ⚠️      |         |                   |            |            |           |        | ✓                 |        |                     |             |
| Image                   | AI2D                                        |                 |         |                   |            |            |           |        | ✓                 |        |                     |             |
| Audio                   | CoVoST2 (21 lang)                           |                 |         |                   |            | ✓          |           |        |                   |        |                     |             |
| Video                   | EgoSchema (test)                            |                 |         |                   |            | ✓          |           |        |                   |        |                     |             |
| Agentic                 | TAU-Bench                                   |                 |         | ✓                 |            |            |           |        |                   |        |                     |             |
| Tool Use                | BFCLv2                                      |                 |         |                   |            |            | ✓         |        |                   |        |                     |             |
| Tool Use                | Nexus                                       |                 |         |                   |            |            | ✓         |        |                   |        |                     |             |
| Long-context            | ZeroSCROLLS/QuALITY                         |                 |         |                   |            |            | ✓         |        |                   |        |                     |             |
| Long-context            | InfiniteBench/En.MC                         |                 |         |                   |            |            | ✓         |        |                   |        |                     |             |
| Long-context            | NIH/Multi-needle                            |                 |         |                   |            |            | ✓         |        |                   |        |                     |             |
| Long-context            | LongBench v2                                |                 |         |                   |            |            |           |        | ✓                 |        |                     |             |
| Long-context            | RULER                                       |                 |         |                   |            |            |           |        | ✓                 |        |                     |             |
| Safety                  | XSTest                                      |                 | ✓       |                   |            |            |           |        |                   |        |                     |             |
| Safety                  | Tülu 3 Safety                               |                 |         |                   |            |            |           |        |                   | ✓      |                     |             |
| Hallucinations          | PersonQA                                    |                 | ✓       |                   |            |            |           |        |                   |        |                     |             |
| Jailbreaking            | StrongREJECT                                |                 | ✓       |                   |            |            |           |        |                   |        |                     |             |
| General, Style-control  | ArenaHard                                   |                 |         |                   |            |            |           |        |                   |        |                     | ✓           |
| RAG                     | FRAMES                                      |                 |         |                   |            |            |           |        |                   |        |                     | ✓           |
| Math                    | CMNO24                                      |                 |         |                   |            |            |           |        |                   |        |                     | ✓           |
| Chinese                 | CLUEWSC                                     |                 |         |                   |            |            |           |        |                   |        |                     | ✓           |
| Chinese                 | C-Eval                                      |                 |         |                   |            |            |           |        |                   |        |                     | ✓           |
| Chinese                 | C-SimpleQA                                  |                 |         |                   |            |            |           |        |                   |        |                     | ✓           |
| General                 | Humanity's Last Exam                        |                 |         |                   | ✓          |            |           |        |                   |        |                     |             |
| Math                    | AIME25                                      |                 |         |                   | ✓          |            |           |        |                   |        |                     |             |
| Image                   | Vibe-Eval                                   |                 |         |                   | ✓          |            |           |        |                   |        |                     |             |
| Coding, Reasoning       | IOI                                         | CC-BY           |         |                   |            |            |           |        |                   |        |                     |             |
| Coding                  | CodeELO                                     |                 |         |                   |            |            |           |        |                   |        |                     |             |
| Reasoning               | SuperGPQA                                   |                 |         |                   |            |            |           |        |                   |        |                     |             |
| Coding                  | SWE-Lancer                                  |                 |         |                   |            |            |           |        |                   |        |                     |             |

**Permissive Licenses**: [MIT](https://choosealicense.com/licenses/mit/), [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/), [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) ([Attribution](https://creativecommons.org/licenses/by/4.0/#ref-appropriate-credit))
<br>
**Copyleft Licenses** ⚠️: [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/), [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/) ([ShareAlike](https://creativecommons.org/licenses/by-sa/4.0/#src-same-license)), [CC-BY-NC-4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en) ([NonCommercial](https://creativecommons.org/licenses/by-nc/4.0/deed.en#src-commercial-purposes))

## Metrics

- [pass@k](metrics/pass@k.md) - applied to determine functional correctness in coding benchmarks with unit tests and increasingly to reduce the variability for generative benchmarks (i.e. with pass@1) using non-zero temperatures and sampling rather than greedy decoding.

## General Notes

Some general points on evaluations:
- Many evaluations are designed to run on base models. 
    - When they are run on base models, their prompts should be setup in such a way that base models can answer the questions by continuing the generation.
- Evaluations that expect fixed outputs like multiple-choice-questions or classification with a fixed set of classes (e.g. sentiment analysis) usually will set the max number of tokens, truncate outputs by setting stop tokens or evaluate based on the log likelihood of the output tokens of the class.
- Some evaluations (e.g. reasoning evals) can be setup to measure zero-shot or n-shot Chain of Thought (CoT) performances.
- LLM-as-a-Judge is another popular method of evaluation. It uses a judge LLM to verify if the output answer is correct.
- **Saturation.** Many benchmarks are increasingly becoming saturated, meaning the performance of models on the benchmark is getting close to the maximum or that it is becoming increasingly difficult to see gains in performance on that benchmark.