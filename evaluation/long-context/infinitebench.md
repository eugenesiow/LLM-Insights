# InfiniteBench

∞Bench is a long-context LLM benchmark, published in the paper [$\infty${B}ench: Extending Long Context Evaluation Beyond 100{K} Tokens](https://arxiv.org/abs/2402.13718) by Zhang et al. from Tsinghua University in Feb 2024. The benchmark features samples with an average data length surpassing 100K tokens. ∞Bench comprises synthetic and realistic tasks spanning diverse domains, presented in both English and Chinese. The tasks in ∞Bench are designed to require the understanding of long dependencies in contexts and are harder than simply retrieving a limited number of passages from contexts. The tasks are summarised in the table below.

| Task Name            | Context       | # Examples | Avg Input Tokens | Avg Output Tokens | Description                                                                                 |
| -------------------- | ------------- | ---------- | ---------------- | ----------------- | ------------------------------------------------------------------------------------------- |
| En.Sum               | Fake Book     | 103        | 171.5k           | 1.1k              | Summarization of a fake book created with core entity substitution.                         |
| En.QA                | Fake Book     | 351        | 192.6k           | 4.8               | Free-form question answering based on the fake book.                                        |
| En.MC                | Fake Book     | 229        | 184.4k           | 5.3               | Multiple choice questions derived from the fake book.                                       |
| En.Dia               | Script        | 200        | 103.6k           | 3.4               | Identification of talkers in partially anonymized scripts.                                  |
| Zh.QA                | New Book      | 175        | 2068.6k          | 6.3               | Question answering on a set of newly collected books.                                       |
| Code.Debug           | Code Document | 394        | 114.7k           | 4.8               | Finding which function in a code repo contains an crashing error (in multiple choice form). |
| Code.Run             | Synthetic     | 400        | 75.2k            | 1.3               | Simulating execution of multiple simple, synthetic functions.                               |
| Math.Calc            | Synthetic     | 50         | 43.9k            | 43.9k             | Calculations involving super-long arithmetic equations.                                     |
| Math.Find            | Synthetic     | 350        | 87.9k            | 1.3               | Finding special integers in a lengthy list.                                                 |
| Retrieve.PassKey[^1] | Synthetic     | 590        | 122.4k           | 2.0               | Retrieving hidden keys in a noisy long context.                                             |
| Retrieve.Number      | Synthetic     | 590        | 122.4k           | 4.0               | Locating repeated hidden numbers in a noisy long context.                                   |
| Retrieve.KV[^2]      | Synthetic     | 500        | 89.9k            | 22.7              | Finding the corresponding value from a dictionary and a key.                                |

## Links

* Abstract: https://arxiv.org/abs/2402.13718
* Code: https://github.com/OpenBMB/InfiniteBench
* Dataset: https://huggingface.co/datasets/xinrongzhang2022/InfiniteBench
* License: [Apache 2.0](https://huggingface.co/datasets/xinrongzhang2022/InfiniteBench/blob/main/README.md)

## Citations

```bibtex
@inproceedings{zhang-etal-2024-bench,
    title = "$\infty${B}ench: Extending Long Context Evaluation Beyond 100{K} Tokens",
    author = "Zhang, Xinrong  and
      Chen, Yingfa  and
      Hu, Shengding  and
      Xu, Zihang  and
      Chen, Junhao  and
      Hao, Moo  and
      Han, Xu  and
      Thai, Zhen  and
      Wang, Shuo  and
      Liu, Zhiyuan  and
      Sun, Maosong",
    editor = "Ku, Lun-Wei  and
      Martins, Andre  and
      Srikumar, Vivek",
    booktitle = "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.acl-long.814",
    pages = "15262--15277",
    abstract = "Processing and reasoning over long contexts is crucial for many practical applications of Large Language Models (LLMs), such as document comprehension and agent construction. Despite recent strides in making LLMs process contexts with more than 100K tokens, there is currently a lack of a standardized benchmark to evaluate this long-context capability. Existing public benchmarks typically focus on contexts around 10K tokens, limiting the assessment and comparison of LLMs in processing longer contexts. In this paper, we propose , the first LLM benchmark featuring an average data length surpassing 100K tokens. comprises synthetic and realistic tasks spanning diverse domains in English and Chinese. The tasks in are designed to require an understanding of long dependencies in contexts and make simply retrieving a limited number of passages from contexts not sufficient for these tasks. Based on , we evaluate several state-of-the-art LLMs tailored for processing long contexts. The experimental results indicate that existing long-context LLMs still require significant advancements to process 100K+ contexts effectively. Furthermore, we present three intriguing analyses regarding the behavior of LLMs processing long context. Our code and data is released.",
}
```