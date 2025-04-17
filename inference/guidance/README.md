# Guidance

Guidance, also called guided decoding, structured outputs, structured decoding or constrainted decoding is about providing a fixed format (e.g. a JSON structure, a YAML or XML structure, regex or grammar) for the output generation.

1. [lm-format-enforcer](lm-format-enforcer.md)
2. [JSONFormer](jsonformer.md)
3. [XGrammar](xgrammar.md)
4. [Outlines](outlines.md)

## Notes

1. According to OpenAI's [cookbook](https://cookbook.openai.com/examples/gpt4-1_prompting_guide) for GPT-4.1, JSON works less effectively as an output format for long-context dependencies than XML.
2. Lee at al. (Jun 2024) in [Can Long-Context Language Models Subsume Retrieval, RAG, SQL, and More?](https://arxiv.org/abs/2406.13121) introduce the following format which also seems to work well `ID: 0 | TITLE: Shinji Okazaki | CONTENT: Shinji Okazaki is a Japanese … | END ID: 0`