# pass@k

> **pass@k** measures the probability that at least one of the top k generated solutions is correct. Higher pass@k values indicate better performance.

Traditional natural language processing (NLP) and specifically natural language generation (NLG) tasks predominantly used methods that matched a generated answer against a reference. This matching could be exact or fuzzy (e.g. BLEU, by [Papineni et al. (2002)](https://aclanthology.org/P02-1040/), and ROUGE score, by [Lin (2004)](https://aclanthology.org/W04-1013/)). However, such match-based metrics would be limited when trying to evaluate working solutions for reasoning or software coding problems, where the reference answer could just be one possibility within a large space of equivalent solutions.

Enter functional correctness as an alternative method for evaluation, e.g. a piece of software code is deemed correct if it passes a set of unit tests. In another words, instead of comparing an answer to just one or a few possible reference answers, instead we test this answer to see if its outcome is successful. This was first developed by Kulal et al. (June 2019) from Stanford in their [SPoC: Search-based Pseudocode to Code](https://arxiv.org/abs/1906.04908) paper, where they defined their main metric of evaluation as success rate at B, i.e. the fraction of test examples where the system generates an accepted program under the budget of B trials. In another words, this meant generating k code samples per problem, while considering a problem being solved if any sample passes the unit tests, while the total fraction of problems solved is reported. However, this method of computing functional correctness can exhibit high variance.

Hence, [Chen et al. (July 2021)](https://arxiv.org/abs/2107.03374) from OpenAI, proposed an unbiased estimator (meant to reduce variance and increase accuracy by law of large numbers) where they generated n ≥ k samples per task (e.g. n = 200 and k ≤ 100), counted the number of correct samples c ≤ n which pass unit tests, and calculated the unbiased estimator as shown in the equation below:

$$\text{pass}@k := \mathbb{E}_{\text{Problems}} \left[ 1 - \frac{\binom{n-c}{k}}{\binom{n}{k}} \right]$$

n is the number of samples (e.g. 200 coding solutions), c is the number of solutions which passed unit tests.

$\binom{n-c}{k}$ is the number of k combinations which did not succeed at the unit test, out of n. $\binom{n}{k}$ is the number of k combinations, out of n.

While the fraction $\frac{\binom{n-c}{k}}{\binom{n}{k}}$ refers to the probablity that all k generated coding solutions fail to pass the unit test. By inverting the minus sign, it becomes the unbiased estimation of the functional correctness, a metric we call **pass@k** when aggregated across all problems ($\mathbb{E}_{\text{Problems}}$) in the evaluation set.

## Implementation

[Chen et al. (July 2021)](https://arxiv.org/abs/2107.03374) also provide a numerically stable script (a `numpy` implementation that simplifies the expression and evaluates the product term-by-term to avoid very large numbers and numerical instability) for calculating pass@k. If n-c (the number of incorrect solutions) is less than k, the pass@k will return 1 as there is always at least one solution is correct, out of k.

```python
def pass_at_k(n, c, k):
    """
    :param n: total number of samples
    :param c: number of correct samples
    :param k: k in pass@$k$
    """
    if n - c < k:
        return 1.0
    return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))
```

The following is the [huggingface implementation](https://github.com/huggingface/evaluate/blob/main/metrics/code_eval/code_eval.py#L198) which estimates the pass@k for each problem and returns them in an array.

```python
def estimate_pass_at_k(num_samples, num_correct, k):
    """Estimates pass@k of each problem and returns them in an array."""

    def estimator(n: int, c: int, k: int) -> float:
        """Calculates 1 - comb(n - c, k) / comb(n, k)."""
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

    if isinstance(num_samples, int):
        num_samples_it = itertools.repeat(num_samples, len(num_correct))
    else:
        assert len(num_samples) == len(num_correct)
        num_samples_it = iter(num_samples)

    return np.array([estimator(int(n), int(c), k) for n, c in zip(num_samples_it, num_correct)])
```

Finally [this code](https://github.com/huggingface/evaluate/blob/main/metrics/code_eval/code_eval.py#L183) calculates the pass@k by taking the mean of the the results (array) from all the problems.
```python
total, correct = [], []
for result in results.values():
    result.sort()
    passed = [r[1]["passed"] for r in result]
    total.append(len(passed))
    correct.append(sum(passed))
total = np.array(total)
correct = np.array(correct)

ks = k
pass_at_k = {f"pass@{k}": estimate_pass_at_k(total, correct, k).mean() for k in ks if (total >= k).all()}
```

## Use in Generative Evaluations

pass@k can also be applied to evaluating generative evaluations for foundation models (FMs), especially for evaluating long-output reasoning models. For example, in the DeepSeek-R1 paper, [Guo et al. (Jan 2025)](https://arxiv.org/abs/2501.12948) from DeepSeek AI opined that using greedy decoding to evaluate long-output reasoning models results in higher repetition rates and significant variability across different checkpoints (they set a maximum generation length of 32,768 tokens for models in their evaluations).

Hence, they defaulted many of their evaluations to use pass@k instead, in particular pass@1, and reported their results with pass@1 using a non-zero temperature (they used a sampling temperature of 0.6 and a top-p value of 0.95 to generate k responses, typically between 4 and 64, depending on the test set size) for each question. They calculated pass@1 as follows:

$$
\text{pass@1} = \frac{1}{k} \sum_{i=1}^{k} p_i
$$

where $p_i$ denotes the correctness of the i-th response. They felt that this method provided more reliable performance estimates.