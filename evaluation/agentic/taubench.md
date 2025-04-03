# TAU-Bench

TAU-bench (τ -bench) evaluates Agents in real-world environments. It tests if an agent can reliably engage in a dynamic, multi-turn conversation with a user to figure out what needs to be done. The benchmark includes 10-15 tools across 50-115 different tasks for a retail and airline domain. The benchmark employs an efficient and faithful evaluation process that compares the database state at the end of a conversation with the annotated goal state.

## Methodology

1. Agent interacts with an simulated user to understand needs and to gather info over multiple turns.
2. Agent utilizes domain-specific API tools (e.g., book flight, return item).
3. Agent must adhere to a provided policy document containing domain-specific rules and restrictions.
4. Success is measured by comparing the final database state.
5. Uses the [pass^k metric](../metrics/pass^k.md) to evaluate reliability on the same task over multiple (k) trials.

## Links

* Abstract: https://arxiv.org/abs/2406.12045
* Homepage: https://github.com/sierra-research/tau-bench
* Leaderboard: https://github.com/sierra-research/tau-bench/blob/main/README.md#leaderboard
* Dataset: (Airline) https://github.com/sierra-research/tau-bench/tree/main/tau_bench/envs/airline/data, (Retail) https://github.com/sierra-research/tau-bench/tree/main/tau_bench/envs/retail/data
* License: [MIT](https://github.com/sierra-research/tau-bench/tree/main?tab=MIT-1-ov-file#readme)

## Citations

```bibtex
@misc{yao2024taubenchbenchmarktoolagentuserinteraction,
      title={$\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains}, 
      author={Shunyu Yao and Noah Shinn and Pedram Razavi and Karthik Narasimhan},
      year={2024},
      eprint={2406.12045},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2406.12045}, 
}
```