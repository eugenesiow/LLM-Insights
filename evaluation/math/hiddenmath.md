# HiddenMath

HiddenMath is one of Google's internal (contains unique problems held-out from our training sets) Math benchmark dataset. HiddenMath comprises 179 competition-level math problems, crafted by experts and evaluated automatically. 

The following table shows some benchmark results of various models on the HiddenMath dataset. Google stopped reporting results for the dataset publicly since Gemini 2.5.

| Model                             | HiddenMath (0-shot) |
|-----------------------------------|---------------------|
| Gemini 2.0 Pro                    | **65.2**                |
| Gemini 2.0 Flash                  | 63.5                |
| Gemma 3 (27B)                     | 60.3                |
| Gemma 3 (12B)                     | 54.5                |
| Gemma 3 (4B)                      | 43.0                |
| Gemini 1.5 Pro (Math-Specialized) | 35.2                |
| GPT-4-Turbo                       | 24.6                |
| Gemini 1.5 Pro                    | 20.1                |
| Claude 3 Opus                     | 17.3                |
| Gemma 3 (1B)                      | 15.8                |
| Gemma 2 (27B)                     | 14.8                |
| Gemini 1.0 Ultra                  | 11.2                |
| Gemma 2 (9B)                      | 10.4                |
| Gemini 1.5 Flash                  | 6.7                 |
| Gemini 1.0 Pro                    | 6.1                 |
| Gemma 2 (2B)                      | 1.8                 |

## Links

* Gemini 1.5 Report: https://arxiv.org/abs/2403.05530
* Gemma 3 Report: https://arxiv.org/abs/2503.19786

## Citation

```
@misc{geminiteam2024gemini15unlockingmultimodal,
      title={Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context}, 
      author={Google Team},
      year={2024},
      eprint={2403.05530},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2403.05530}, 
}
```

```
@misc{gemmateam2025gemma3technicalreport,
      title={Gemma 3 Technical Report}, 
      author={Google Team},
      year={2025},
      eprint={2503.19786},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2503.19786}, 
}
```