# Parallelization

## ZeRo

[Zero Redundancy Optimizer (ZeRO)](https://arxiv.org/abs/1910.02054) is an approach to data parallelism and model partitioning across GPUs.

### Communication

In ZeRo, given M parameters,
- in the forward pass we need to do all-gather to collect M parameters,
- in the backward pass we need to do all-gather to re-collect M parameters then each GPU can calculate local gradients, 
- also in the backward pass, we then need to do a reduce-scatter function to aggregate and redistribute gradients (of size M parameters) across all GPUs.
- Hence, there is a total of 3M communication per M weights.
- This gives a model-to-communications ratio of 1:3.

[ZeRo++](https://arxiv.org/abs/2306.10209) reduces this from 1:0.75 or for M parameters, only 0.75M communications over the forward and backward passes.

## 3D Parallelism