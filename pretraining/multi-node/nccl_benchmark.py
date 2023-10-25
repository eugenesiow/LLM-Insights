#!/usr/bin/env python

# this version has been derived from https://github.com/stas00/ml-engineering/blob/master/multi-node/all_reduce_bench.py
# which in turn is derived from https://github.com/NVIDIA/nccl-tests
#
# to run for 2 nodes on rank 0 node:
# python -m torch.distributed.run --nproc_per_node=2 --node-rank=0 nccl_benchmark.py
#
# the printed results are already n_gpu-agnostic (i.e. averaged for the world size)

import fcntl
import os
import socket
import torch
import torch.distributed as dist

TRIALS = 5

# 4GB
N = 500000
M = 500 * 4


def printflock(*msgs):
    """ print """
    with open(__file__, "r") as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            print(*msgs)
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)


def timed_allreduce(mat, id, start_event, end_event):
    start_event.record()
    dist.all_reduce(mat)
    end_event.record()

    torch.cuda.synchronize()
    duration = start_event.elapsed_time(end_event) / 1000

    tput = ((M*N*4*2)/duration)*8 # *2 is for send + receive, *8 for gigabits/second
    size = M * N * 4 # 4 is fp32
    n = dist.get_world_size()
    busbw = (size / duration) * (2 * (n - 1) / n) * 8
    printflock(f"{id}:\n",
               f"duration: {duration:.4f} sec\n",
               f"algo throughput: {tput:.4f} bps, {tput/1e9:.4f} Gbps\n",
               f"busbw: {busbw / 1e9:.4f}  Gbps"
    )


def run(local_rank):
    hostname = socket.gethostname()
    id = f"{hostname}:{local_rank}"
    global_rank = dist.get_rank()

    printflock(f"{id} data size: {M*N*4/1e9} GB")
    mat = torch.rand(N, M, dtype=torch.float32).cuda(local_rank)

    start_event = torch.cuda.Event(enable_timing=True)
    end_event = torch.cuda.Event(enable_timing=True)
    for i in range(TRIALS):
        dist.barrier()
        if global_rank == 0:
            print(f"\n\n\n-----------trial-{i}----------------")
        timed_allreduce(mat, id, start_event, end_event)


def init_processes(local_rank, fn, backend='nccl'):
    torch.cuda.set_device(local_rank)
    dist.init_process_group(backend)
    fn(local_rank)


if __name__ == "__main__":
    rank = int(os.environ["LOCAL_RANK"])
    printflock("local_rank: %d" % rank)
    init_processes(local_rank=rank, fn=run)