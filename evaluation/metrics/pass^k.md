# pass^k

> **pass^k** (pronounced "pass power k") is a metric to evaluate the reliability of agent behavior over multiple trials.

Pass^k was introduced in [TAU-Bench](../agentic/taubench.md) in the paper published by Yao et al. in Jun 2024 from the agentic AI startup, [Sierra](https://sierra.ai/). It estimates the probability that an agent would succeed on all k independent attempts. This is useful for evaluating consistency and reliability in agent performance.

The formula is as follows:

$$
\text{Pass}^k = \left(\frac{c}{n}\right)^k
$$

Where $\left(\frac{c}{n}\right)$ represents the raw success rate on a single attempt, raised to the power of $ k $.

It is not to be confused with [pass@k](../metrics/pass@k.md).