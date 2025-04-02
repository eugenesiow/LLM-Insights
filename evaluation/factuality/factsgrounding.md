# FACTS Grounding

FACTS Grounding is a benchmark from Google DeepMind and Google Research designed to measure the performance of AI Models on factuality and grounding. This dataset is a collection 860 examples (public set) crafted by humans for evaluating how well an AI system grounds their answers to a given context. This dataset consists the "public" set (860) while Google maintains a "private" (859) held out set (to protect againsts benchmark contamination and leaderboard hacking). 

## Links

* Abstract: https://arxiv.org/abs/2501.03200
* Homepage: https://deepmind.google/discover/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/
* Leaderboard: https://www.kaggle.com/facts-leaderboard
* Code: https://www.kaggle.com/code/andrewmingwang/facts-grounding-benchmark-starter-code
* Dataset: https://www.kaggle.com/datasets/deepmind/facts-grounding-examples
* License: [CC-BY-4.0](https://www.kaggle.com/datasets/deepmind/facts-grounding-examples?select=LICENSE.txt)

## Example Questions

Each example consists of a system instruction, user request and a context document (maximum of 32k tokens), and requires a long-form response. AI generated responses to these examples are evaluated by an ensemble of automated judge models. The following is an example question:

**System Instruction**

```
Answer the question using only the information provided in the context.
```

**User Request**

```
What color is an apple?
```

**Context Document**

```
Apples are red fruits. Bananas are yellow fruits.
```

**Example Generated Response**

```
Apples are red. Bananas are cheaper than apples. Bananas are green. Enjoy your fruit!
```

**Example Grounding Evaluation**

| Sentence: | Classification: | Explanation: |
|---|---|---|
| "Apples are red." | ✅ Supported | The sentence is grounded to the given context. |
| "Bananas are cheaper than apples." | ❌ Unsupported | The sentence is not grounded to the given context. |
| "Bananas are green." | ❌ Contradictory | The sentence is falsified by the given context. |
| "Enjoy your fruit!" | 🟢 Irrelevant | The sentence does not required factual attribution. |

**Judgement**

```
❌ Fail - at least one sentence is "unsupported" or "contradictory".
```

## Citations

```bibtex
@misc{jacovi2025factsgroundingleaderboardbenchmarking,
      title={The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground Responses to Long-Form Input}, 
      author={Alon Jacovi and Andrew Wang and Chris Alberti and Connie Tao and Jon Lipovetz and Kate Olszewska and Lukas Haas and Michelle Liu and Nate Keating and Adam Bloniarz and Carl Saroufim and Corey Fry and Dror Marcus and Doron Kukliansky and Gaurav Singh Tomar and James Swirhun and Jinwei Xing and Lily Wang and Madhu Gurumurthy and Michael Aaron and Moran Ambar and Rachana Fellinger and Rui Wang and Zizhao Zhang and Sasha Goldshtein and Dipanjan Das},
      year={2025},
      eprint={2501.03200},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.03200}, 
}
```