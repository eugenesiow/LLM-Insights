# Scheduler

Learning rate is a critical hyperparameter for pre-training LLMs. The cosine learning rate scheduler is the most commonly used strategy like [Llama 3](https://arxiv.org/abs/2407.21783) and [Gopher](https://arxiv.org/abs/2112.11446).

## Cosine Scheduler

Llama 3 405B was pre-trained using a cosine learning rate schedule with a learning rate of 8 × 10−5 and decayed to 8 × 10−7 over 1,200,000 training steps. Training started with smaller batches to improve training stability and was increased subsequently to improve efficiency. Initial batch size of 4M tokens and sequence length of 4096 tokens. The batch size becomes 8M and a sequence of 8192 tokens after pre-training 252M tokens. Finally batch size was increased to 16M tokens after pre-training 2.87T tokens. 

- Pre-defined training steps to achieve the optimal loss. 
    - the intermediate training checkpoints are suboptimal.
    - continued pre-training (CPT) of an existing language model is  more complicated.

## Warmup-Stable-Decary (WSD) Scheduler

Warmup-Stable-Decay (WSD) is a strategy proposed in [MiniCPM](https://arxiv.org/abs/2404.06395) as an alternative  learning rate scheduler. 

The WSD learning rate schedule is divided into three phases: 
1. warmup phase, linearly increase the learning rate from 0 to peak; 
2. stable phase, maintain the learning rate at peak value and training the model for most of the time; 
3. decay phase, annealing the learning rate to 0 in a relatively short period. 

The main advantage of this schedule is that specifying the number of training steps in advance is not required. This is particularly convenient for large runs, as the decay can be applied at any time to observe model performance and decide whether to stop. It also allows for continual learning by default, as training can be resumed from a stable phase checkpoint. Moreover, the data mixture can be changed during the decay phase to increase the ratio of high-quality data (e.g. annealing on high quality data).