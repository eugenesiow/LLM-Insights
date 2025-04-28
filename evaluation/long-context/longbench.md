# LongBench

LongBench v2 is a benchmark designed to evaluate the capability of large language models (LLMs) to perform deep understanding and reasoning tasks over exceptionally long contexts, ranging from 8K to 2M n words. It was created to address limitations in existing long-context benchmarks, which often relied on simpler extractive questions or synthetic tasks that did not accurately reflect real-world challenges or require true deep comprehension and reasoning. Questions in LongBench v2 are designed to avoid simple counting, direct retrieval, or reliance on external knowledge. The benchmark uses real-world data from diverse sources and features a multiple-choice question format for reliable evaluation, addressing the unreliability of metrics like F1 and ROUGE used in some other benchmarks. 

LongBench v2 consists of 503 multiple-choice questions across six major task categories:

- Single-Document QA: Questions based on academic, literary, legal, financial, governmental, and detective documents, including event ordering tasks.
- Multi-Document QA: Questions requiring information from multiple documents, including academic, legal, financial, governmental, and multi-news sources.
- Long In-context Learning: Tasks such as answering questions based on user guides, translating new languages using a vocabulary book, and many-shot learning for classification.
- Long-dialogue History Understanding: Questions testing comprehension of lengthy conversation histories, including LLM agent interactions and user-LLM dialogues.
- Code Repository Understanding: Questions requiring understanding and reasoning across multiple files within a code repository.
- Long Structured Data Understanding: Tasks involving reasoning over long tables and complex queries on knowledge graphs.

The data was collected by 97 highly educated annotators with diverse professional backgrounds. The data collection followed a multi-step pipeline:

- Document Collection: Annotators uploaded long English documents (8k to 2M words).
- Data Annotation: Annotators created multiple-choice questions requiring deep understanding and reasoning, avoiding simple or tricky questions. They also provided the correct answer and evidence.
- Automated Review: Three LLMs automatically attempted to answer the questions. If all three answered correctly, the question was deemed too easy and required revision.
- Manual Review: Professional human experts reviewed the questions, attempting to answer them within a time limit (encouraged under 15 minutes). They assessed if the question met the requirements, if the answer was correct and objective, and recorded the time taken. Questions answered correctly by experts within 3 minutes were also flagged as too easy. Data that failed any review stage required revision by the annotator. This iterative process and the use of both automated and manual checks, along with clear guidelines and incentives for longer and harder data, aimed to ensure high quality, difficulty, and practicality.

Currently, the benchmark is limited to English only, not capturing performance across multiple languages. Additionally, there are inconsistencies in the length distribution across different task categories, making direct performance comparisons across length intervals for a single model challenging. The creators recommend comparing models on a per-interval basis due to this uneven distribution.

## Links

- Abstract: https://arxiv.org/abs/2412.15204
- Code: https://github.com/THUDM/LongBench
- Dataset: https://huggingface.co/datasets/THUDM/LongBench
- License: [MIT](https://github.com/THUDM/LongBench?tab=MIT-1-ov-file#readme)

## Citations

```bibtex
@misc{bai2025longbenchv2deeperunderstanding,
      title={LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks}, 
      author={Yushi Bai and Shangqing Tu and Jiajie Zhang and Hao Peng and Xiaozhi Wang and Xin Lv and Shulin Cao and Jiazheng Xu and Lei Hou and Yuxiao Dong and Jie Tang and Juanzi Li},
      year={2025},
      eprint={2412.15204},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.15204}, 
}
```