# AlpacaEval

Evaluation of instruction-following models typically requires human interactions (e.g. to evaluate the steerability of an instruction-following model). This is time-consuming, expensive, and hard to replicate. AlpacaEval in an LLM-based automatic evaluation method that has been validated against 20K human annotations.

AlpacaEval 2.0 is a new version of AlpacaEval that uses the `gpt4_turbo` model that gives a better reflection of the state of the art. The prompt has been changed such that the model outputs a single token, which further reduced cost and speed. Finally, instead of using a binary preference, 2.0 uses the logprobs to compute a continuous preference, which gives the final weighted win-rate. The latter two changes had the surprising effect of decreasing the annotators' length bias (i.e. tending to prefer longer outputs).

## Links

* Abstract: https://arxiv.org/abs/2404.04475
* Homepage: https://github.com/tatsu-lab/alpaca_eval
* Dataset: https://huggingface.co/datasets/tatsu-lab/alpaca_eval, https://huggingface.co/datasets/tatsu-lab/alpaca_farm
* License: [CC-BY-NC-4.0](https://github.com/tatsu-lab/alpaca_farm/blob/main/DATA_LICENSE)

## Citation

AlpacaEval
```
@misc{alpaca_eval,
  author = {Xuechen Li and Tianyi Zhang and Yann Dubois and Rohan Taori and Ishaan Gulrajani and Carlos Guestrin and Percy Liang and Tatsunori B. Hashimoto },
  title = {AlpacaEval: An Automatic Evaluator of Instruction-following Models},
  year = {2023},
  month = {5},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/tatsu-lab/alpaca_eval}}
}
```

AlpacaEval v2
```
@article{dubois2024length,
  title={Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators},
  author={Dubois, Yann and Galambosi, Bal{\'a}zs and Liang, Percy and Hashimoto, Tatsunori B},
  journal={arXiv preprint arXiv:2404.04475},
  year={2024}
}
```

AlpacaFarm
```
@misc{dubois2023alpacafarm,
  title={AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback}, 
  author={Yann Dubois and Xuechen Li and Rohan Taori and Tianyi Zhang and Ishaan Gulrajani and Jimmy Ba and Carlos Guestrin and Percy Liang and Tatsunori B. Hashimoto},
  year={2023},
  eprint={2305.14387},
  archivePrefix={arXiv},
  primaryClass={cs.LG}
}
```
