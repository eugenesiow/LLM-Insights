# Hardware

- [Hardware](#hardware)
  - [GPUs](#gpus)
    - [What Temperature Should My GPUs Run At?](#what-temperature-should-my-gpus-run-at)

## GPUs

### What Temperature Should My GPUs Run At?

Inference workloads vary, so GPU utilization varies quite widely as well. Pre-training on the other hand will definitely run close to full load and put your GPU utilization close to 100% all-the-time. 

GPU temperatures on my team's pre-training workload varies in the **66-72C** range on A100s and slightly hotter at **70-75C** on H100s. This is assuming your DC is run at around 24C. All these are good signs that we aren't shortening the life of your GPUs by running them too hot. 

Nvidia GPUs supposedly can run up to 100C but I think you really only want to run them up to 80C max. GPUs will **start to throttle past 80C**, specifically about 83C for A100s and H100s. Usually **thermal shutdown occurs at about 90-92C** and this can be considered the maximum operating temperature (T_limit) for the GPU. 

We usually get idle temperatures for A100s and H100s in DGX/HGX setups around 25-32C. Idle power for H100s is slightly higher. These temperatures are quite dependent on the fan speed/air inlet temperatures, which trigger at a threshold (can be set). There's not much point cooling something under 40C so these temperatures are probably just good for general awareness.