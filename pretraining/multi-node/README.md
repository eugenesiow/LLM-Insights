# Multi-Node

When pre-training large models (more than a billion parameters) with large datasets (trillions of tokens), its almost certain that we will need to use multiple nodes (each node usually maxes out at 8 GPUs and 640GB VRAM) to distribute the training. When doing multi-node training, synchronization of GPUs across the network fabric is necessary (e.g. when averaging gradients). Hence, when doing pre-training, getting the multi-node design and config right ensures this sync  doesn't become a bottleneck.

## The Multi-Node GPU Stack

- NVIDIA Collective Communications Library ([NCCL](https://developer.nvidia.com/nccl)) - implements efficient multi-GPU and multi-node communication.

## Tools

- [nccl_benchmark.py](./nccl_benchmark.py) - benchmark the network bandwidth by performing an all_reduce using pytorch distributed over NCCL on a sizeable amount of data (e.g. 4GB).