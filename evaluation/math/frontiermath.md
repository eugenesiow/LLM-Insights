# FrontierMath

FrontierMath is a benchmark of hundreds of original, exceptionally challenging mathematics problems crafted and vetted by expert mathematicians. The questions cover most major branches of modern mathematics -- from computationally intensive problems in number theory and real analysis to abstract questions in algebraic geometry and category theory. Solving a typical problem requires multiple hours of effort from a researcher in the relevant branch of mathematics, and for the upper end questions, multiple days. FrontierMath uses new, unpublished problems and automated verification to reliably evaluate models while minimizing risk of data contamination. 

The benchmark was published and is run by [Epoch AI](https://epoch.ai/frontiermath) (commissioned and funded by [OpenAI](https://epoch.ai/blog/openai-and-frontiermath), who has access to the statements and solutions, except for a 50-question holdout set). It was published by Glazer et al. in Nov to Dec 2024 with the paper [FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI](https://arxiv.org/abs/2411.04872). The final dataset is a 300 problem dataset with a 50 solution hold out set (from OpenAI) for evaluation purposes.

## Links

* Abstract: https://arxiv.org/abs/2411.04872
* Homepage: https://epoch.ai/frontiermath/the-benchmark
* License: Unknown

## Example Questions

Below is a released example question.

<details>
<summary>Testing Artin's primitive root conjecture</summary>

For a positive integer $n$, let $v_p(n)$ denote the largest integer $v$ such that $p^v \mid n$. For a prime $p$ and $a \not\equiv 0 \pmod{p}$, let $\text{ord}_p(a)$ denote the smallest positive integer $o$ such that $a^o \equiv 1 \pmod{p}$. For $x > 0$, let

$$\text{ord}_{p,x}(a) = \prod_{\substack{q \le x \\ q \text{ prime}}} q^{v_q(\text{ord}_p(a))} \prod_{\substack{q > x \\ q \text{ prime}}} q^{v_q(p-1)}.$$

Let $S_x$ denote the set of primes $p$ for which

$$\text{ord}_{p,x}(2) > \text{ord}_{p,x}(3),$$

and let $d_x$ denote the density

$$d_x = \lim_{t \to \infty} \frac{|\{p \le t : p \in S_x\}|}{|\{p \le x : p \text{ prime}\}|}$$

of $S_x$ in the primes. Let

$$d_\infty = \lim_{x \to \infty} d_x.$$

Compute $\lfloor 10^6 d_\infty \rfloor$.

Source: https://epoch.ai/frontiermath/benchmark-problems

</details>

## Citation

```
@misc{glazer2024frontiermathbenchmarkevaluatingadvanced,
      title={FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI}, 
      author={Elliot Glazer and Ege Erdil and Tamay Besiroglu and Diego Chicharro and Evan Chen and Alex Gunning and Caroline Falkman Olsson and Jean-Stanislas Denain and Anson Ho and Emily de Oliveira Santos and Olli Järviniemi and Matthew Barnett and Robert Sandler and Matej Vrzala and Jaime Sevilla and Qiuyu Ren and Elizabeth Pratt and Lionel Levine and Grant Barkley and Natalie Stewart and Bogdan Grechuk and Tetiana Grechuk and Shreepranav Varma Enugandla and Mark Wildon},
      year={2024},
      eprint={2411.04872},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2411.04872}, 
}
```