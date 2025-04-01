# MathVista

**MathVista** is a mathematical reasoning benchmark involving visual contexts published with the paper [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://arxiv.org/abs/2310.02255) at ICLR 2024 in May 2024 by Lu et al. from UCLA, University of Washington and Microsoft Research. It consists of datasets **IQTest, FunctionQA, and PaperQA**, which address the missing visual domains and are tailored to evaluate logical reasoning on puzzle test figures, algebraic reasoning over functional plots, and scientific reasoning with academic paper figures, respectively. Additionally, it also incorporates 9 MathQA datasets and 19 VQA datasets from the literature, which enrich the diversity and complexity of visual perception and mathematical reasoning challenges within the benchmark. In total, MathVista includes **6,141 samples** collected from 31 different datasets.

## Links

* Abstract: https://arxiv.org/abs/2310.02255
* Homepage: https://mathvista.github.io/
* Code: https://github.com/lupantech/MathVista
* Dataset: https://huggingface.co/datasets/AI4Math/MathVista
* License: [CC-BY-SA-4.0](https://huggingface.co/datasets/AI4Math/MathVista/blob/main/README.md)

## Example Questions

Below are example questions from the IQTest, FunctionQA, and PaperQA datasets:

<img src="https://raw.githubusercontent.com/lupantech/MathVista/main/assets/our_new_3_datasets.png" style="zoom:40%;" />

<details>
<summary>1. Arithmetic Reasoning</summary>

<img src="https://raw.githubusercontent.com/lupantech/MathVista/main/assets/skills/ari.png" style="zoom:40%;" />

</details>

<details>
<summary>2. Statistical Reasoning</summary>

<img src="https://raw.githubusercontent.com/lupantech/MathVista/main/assets/skills/sta.png" style="zoom:40%;" />

</details>

<details>
<summary>3. Algebraic Reasoning</summary>

<img src="https://raw.githubusercontent.com/lupantech/MathVista/main/assets/skills/alg.png" style="zoom:40%;" />

</details>

<details>
<summary>4. Geometry Reasoning</summary>

<img src="https://raw.githubusercontent.com/lupantech/MathVista/main/assets/skills/geo.png" style="zoom:40%;" />

</details>

<details>
<summary>5. Numeric common sense</summary>

<img src="https://raw.githubusercontent.com/lupantech/MathVista/main/assets/skills/num.png" style="zoom:40%;" />

</details>

<details>
<summary>6. Scientific Reasoning</summary>

<img src="https://raw.githubusercontent.com/lupantech/MathVista/main/assets/skills/sci.png" style="zoom:40%;" />

</details>

<details>
<summary>7. Logical Reasoning</summary>

<img src="https://raw.githubusercontent.com/lupantech/MathVista/main/assets/skills/log.png" style="zoom:40%;" />

</details>

## Citations

```bibtex
@misc{lu2024mathvistaevaluatingmathematicalreasoning,
      title={MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts}, 
      author={Pan Lu and Hritik Bansal and Tony Xia and Jiacheng Liu and Chunyuan Li and Hannaneh Hajishirzi and Hao Cheng and Kai-Wei Chang and Michel Galley and Jianfeng Gao},
      year={2024},
      eprint={2310.02255},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2310.02255}, 
}
```