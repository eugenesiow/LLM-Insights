# Hardware

- [Hardware](#hardware)
  - [GPUs](#gpus)
    - [PCIe VS SXM](#pcie-vs-sxm)
    - [What Temperature Should My GPUs Run At?](#what-temperature-should-my-gpus-run-at)
  - [Intra-Node Connectivity](#intra-node-connectivity)
    - [NVLink](#nvlink)
    - [NVSwitch](#nvswitch)

## GPUs

### PCIe VS SXM

### What Temperature Should My GPUs Run At?

Inference workloads vary, so GPU utilization varies quite widely as well. Pre-training on the other hand will definitely run close to full load and put your GPU utilization close to 100% all-the-time. 

<u>Safe GPU temperatures at full load.</u> GPU temperatures on my team's pre-training workload varies in the **66-72C** range on A100s and slightly hotter at **70-75C** on H100s. This is assuming your DC is run at around 24C. All these are good signs that we aren't shortening the life of your GPUs by running them too hot. 

<u>Thermal throttling and shutdown temperatures.</u> Nvidia GPUs supposedly can run up to 100C but I think you really only want to run them up to 80C max. GPUs will **start to throttle past 80C**, specifically about 83C for A100s and H100s. Usually **thermal shutdown occurs at about 90-92C** and this can be considered the maximum operating temperature (T_limit) for the GPU. 

<u>Idle temperatures.</u> We usually get idle temperatures for A100s and H100s in DGX/HGX setups around 25-32C. Idle power for H100s is slightly higher. These temperatures are quite dependent on the fan speed/air inlet temperatures, which trigger at a threshold (can be set). There's not much point cooling something under 40C so these temperatures are probably just good for general awareness.

## Intra-Node Connectivity

### NVLink

[NVLink](https://www.nvidia.com/en-sg/data-center/nvlink/) is a high-speed intra-node connection for direct GPU-to-GPU interconnect (between pairs of GPUs on the same node) which increases multi-GPU input/output (IO) on the node. It allows the sending and receiving of data from shared pools of memory between GPUs faster.

Each generation of NVLink technology has been pushing up the bandwidth between GPUs (as shown below) and with the H100s with 18x NVLink 4.0, we can get a total bandwidth of 900GB/s.

| Connectivity  | Bandwidth (GB/s)  | Max Links  | Supported Architecture   |
|---|---|---|---|
| NVLink 1.0    | 240  | 4  | Pascal  |
| NVLink 2.0    | 300  | 6  | Volta  |
| NVLink 3.0    | 600  | 12  | Ampere  |
| NVLink 4.0    | 900  | 18  | Hopper  |

We can view the topology of our GPUs on a node using the following command:
```
nvidia-smi topo -m
```

On a DGX A100 (640GB) we will see something like the following (abbreviated) topology print out. There are 8x A100 GPUs, each has NVLink 3.0 connections with 12x (bonded set of) links with each of the other GPUs (see [NVSwitch](#nvswitch)), hence `NV12`. On a DGX H100, one would see `NV18`.
```
        GPU0    GPU1    GPU2    GPU3    GPU4    GPU5    GPU6    GPU7    ...
GPU0     X      NV12    NV12    NV12    NV12    NV12    NV12    NV12    ...
GPU1    NV12     X      NV12    NV12    NV12    NV12    NV12    NV12    ...
GPU2    NV12    NV12     X      NV12    NV12    NV12    NV12    NV12    ...
GPU3    NV12    NV12    NV12     X      NV12    NV12    NV12    NV12    ...
GPU4    NV12    NV12    NV12    NV12     X      NV12    NV12    NV12    ...
GPU5    NV12    NV12    NV12    NV12    NV12     X      NV12    NV12    ...
GPU6    NV12    NV12    NV12    NV12    NV12    NV12     X      NV12    ...
GPU7    NV12    NV12    NV12    NV12    NV12    NV12    NV12     X      ...
```

The following is a legend of the abbreviations used:
```
X    = Self
SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
PIX  = Connection traversing at most a single PCIe bridge
NV#  = Connection traversing a bonded set of # NVLinks
```

When running a distributed job, we can use `NCCL_P2P_DISABLE=1` to tell NCCL not to use NVLink between GPUs on the same node.

One way to observe this speed difference is to run Nvidia's benchmark [nccl-tests](nccl-tests). A quick way to do so that works well in an offline environment with all dependencies is using [Coreweave's nccl-test container images](https://github.com/coreweave/nccl-tests). We can start the container using the following command. I start the container with `--privileged` and `--net=host` flags which allow the image access to the host network stack and to some system folders that contain the network topology, etc. In this example, I also specify the image to only use the last 4 GPUS, devices 4,5,6 and 7 of the 8x GPU node with the `--gpus` flag.
```
docker run -it --rm  --privileged --net=host \
        --gpus='"device=4,5,6,7"' \
        ghcr.io/coreweave/nccl-tests:11.8.0-cudnn8-devel-ubuntu20.04-nccl2.16.2-1-253a5b1 bash
```

The previous command brings us to a interactive bash shell within the container image. Next we can run the all_reduce benchmark using `nccl-tests`. The flag `-b 1G` and `-e 10G` sets the tests to scan from a minimum of 1GB to a maximum of 10GB. `-f 2` sets the number of steps to 2 and `-g 4` sets to run on 4 GPUs.
```
./build/all_reduce_perf -b 1G -e 10G -f 2 -g 4
```

The results show an average [bus bandwidth](https://github.com/NVIDIA/nccl-tests/blob/master/doc/PERFORMANCE.md#bus-bandwidth) (busbw) of 222GB/s for performing the all_reduce operation across these 4 GPUs. 
```
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
  1073741824     268435456     float     sum      -1   7163.5  149.89  224.84      0   7161.8  149.93  224.89      0
  2147483648     536870912     float     sum      -1    13989  153.51  230.27      0    13997  153.42  230.13      0
  4294967296    1073741824     float     sum      -1    27672  155.21  232.81      0    39252  109.42  164.13      0
  8589934592    2147483648     float     sum      -1    54894  156.48  234.72      0    54890  156.49  234.74      0
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 222.066
```

If we add the environment variable `NCCL_P2P_DISABLE=1`, we can instruct NCCL not to use NVLink between GPUs on the same node.
```
NCCL_P2P_DISABLE=1 ./build/all_reduce_perf -b 1G -e 10G -f 2 -g 4
```

The results show a much worse performance without NVLink between the GPUs for performing the all_reduce operation.
```
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
  1073741824     268435456     float     sum      -1   309766    3.47    5.20      0   309701    3.47    5.20      0
  2147483648     536870912     float     sum      -1   619555    3.47    5.20      0   619608    3.47    5.20      0
  4294967296    1073741824     float     sum      -1  1239398    3.47    5.20      0  1239037    3.47    5.20      0
  8589934592    2147483648     float     sum      -1  2479229    3.46    5.20      0  2478913    3.47    5.20      0
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 5.19883
```

### NVSwitch

[NVSwitch](https://www.nvidia.com/en-sg/data-center/nvlink/) connects multiple NVLinks to provide all-to-all GPU communication at full NVLink speed within a node.  

| Connectivity  | Max GPUs | Bandwidth (GB/s)  | Aggregate Bandwidth (TB/s)  | Supported Architecture   |
|---|---|---|---|---|
| NVSwitch 1.0  | 8 | 300  | 2.4  | Volta  |
| NVSwitch 2.0  | 8 | 600  | 4.8  | Ampere  |
| NVSwitch 3.0  | 8 | 900  | 7.2  | Hopper  |