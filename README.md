# LLM Insights

1. Infrastructure/Platform
   - [Hardware](infrastructure/hardware/)
   - [Alternative Accelerators](infrastructure/hardware/alternatives/)
2. Data Engineering
   - [Common Crawl](dataengineering/cc/README.md)
3. Pre-Training Stage
   - [Tokenization](pretraining/tokenization/)
   - [Model Architecture](pretraining/architecture/)
   - [Multi-Node](pretraining/multi-node/)
   - [Training](pretraining/training/)
4. Fine-Tuning Stage
   - [Adapters](finetuning/adapters/)
5. Alignment Stage
   - [Reducing Hallucination](alignment/hallucination/)
6. Evaluation Stage
   - [Overview](evaluation/README.md)
   - [General](evaluation/general/) - knowledge, language ability (e.g. reading comprehesion), broad/multi-domain.
   - [Steerability](evaluation/steerability/) - instruction-following ability.
   - [Math](evaluation/math/) - solving math problems, math reasoning or math programming problems.
   - [Reasoning](evaluation/reasoning/) - logical thinking, making inferences, and drawing conclusions from given information; usually harder problems require multiple steps.
   - [Coding](evaluation/coding/) - writing programming code, doing software engineering and developing applications.
   - [Factuality](evaluation/factuality/) - ability to produce accurate and truthful information.
   - [Multilingual](evaluation/multilingual/) - performance on languages other than English and especially on low-resource languages.
   - [Image](evaluation/image/) - multimodal image understanding, knowledge, advanced perception and multimodal reasoning ability.
   - [Audio](evaluation/audio/) - multimodal audio understanding, end-to-end speech-to-text translation, etc.
   - [Video](evaluation/video/) - multimodal video language understanding, long-form video understanding, etc.
7. Inference Stage
   - [Estimating Model Size](inference/README.md##estimating-model-size)
   - [Speed](inference/README.md#generative-inference-speed)
   - [Throughput](inference/README.md#generative-inference-throughput)
   - [Guidance](inference/guidance/README.md)
8. Applications
   - [Agents](applications/agents/README.md)

## Acknowledgements

I'm grateful to my employers for trusting me to lead the team that built the GPU supercompute platform/infrastructure and to co-lead the team doing LLM pre-training. This allowed me to work on large on-premise GPU compute clusters with A100s and then H100s, which is certainly a privilege. Hopefully sharing some of these notes and insights helps the community.