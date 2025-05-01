# RULER

[RULER: What’s the Real Context Size of Your Long-Context Language Models?](https://arxiv.org/abs/2404.06654) by Hsieh et al. from Nvidia, published Aug 2024, introduces a new synthetic benchmark designed to provide a more comprehensive evaluation of long-context language models than existing methods, particularly the widely used "needle-in-a-haystack" (NIH) test. The authors argue that the vanilla NIH test only assesses a superficial form of long-context understanding – simple retrieval. RULER expands upon this by introducing diverse task categories (Retrieval, Multi-hop Tracing, Aggregation, and Question Answering) with flexible configurations for sequence length and complexity. 

## Links

- Abstract: https://arxiv.org/abs/2404.06654
- Code: https://github.com/hsiehjackson/RULER
- Dataset: https://github.com/gkamradt/LLMTest_NeedleInAHaystack/tree/main/needlehaystack/PaulGrahamEssays, https://rajpurkar.github.io/SQuAD-explorer/, https://hotpotqa.github.io/
- License: [Apache 2.0](https://github.com/NVIDIA/RULER?tab=Apache-2.0-1-ov-file)

## Citations

```bibtex
@article{hsieh2024ruler,
  title={RULER: What's the Real Context Size of Your Long-Context Language Models?},
  author={Cheng-Ping Hsieh and Simeng Sun and Samuel Kriman and Shantanu Acharya and Dima Rekesh and Fei Jia and Yang Zhang and Boris Ginsburg},
  year={2024},
  journal={arXiv preprint arXiv:2404.06654},
}
```