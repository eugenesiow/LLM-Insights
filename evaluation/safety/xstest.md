# XSTest

XSTEST is a test suite designed to identify "exaggerated safety behaviours" in Large Language Models (LLMs). Exaggerated safety refers to models refusing to answer clearly safe prompts because they use language superficially similar to unsafe prompts or mention sensitive topics. While safety safeguards are crucial for LLMs to avoid generating harmful content, an overemphasis on harmlessness can significantly reduce a model's helpfulness. 

XSTEST comprises 250 safe prompts across ten prompt types that well-calibrated models should not refuse to comply with, and 200 unsafe prompts as contrasts that models, for most applications, should refuse. The safe prompt types are designed to superficially resemble unsafe prompts through the use of homonyms, figurative language, safe targets, safe contexts, definitions of sensitive terms, discrimination against nonsensical groups, nonsense discrimination against real groups, historical events, and privacy requests for public or fictional entities.

## Links

- Abstract: https://arxiv.org/abs/2308.01263
- Code: https://github.com/paul-rottger/xstest
- Dataset: https://huggingface.co/datasets/Paul/XSTest
- License: [CC-BY-4.0](https://huggingface.co/datasets/Paul/XSTest/blob/main/README.md)

## Citations

```bibtex
@misc{röttger2024xstesttestsuiteidentifying,
      title={XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models}, 
      author={Paul Röttger and Hannah Rose Kirk and Bertie Vidgen and Giuseppe Attanasio and Federico Bianchi and Dirk Hovy},
      year={2024},
      eprint={2308.01263},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2308.01263}, 
}
```