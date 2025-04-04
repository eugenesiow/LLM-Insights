# MM-MT-Bench

MM-MT-Bench (Multi-Modal Multi-Turn-Bench) is a multi-turn LLM-as-a-judge evaluation benchmark similar to the text MT-Bench for testing multimodal instruction-tuned models. It was developed by Mistral AI by Agrawal et al. in Oct 2024 and published with the [Pixtral 12B](https://arxiv.org/abs/2410.07073) paper. While existing benchmarks like MMMU, MathVista, ChartQA and so on are focused on closed-ended questions with short responses, this benchmark evaluates the model's ability to follow user instructions in multi-turn dialogues and answer open-ended questions in a zero-shot manner. 

## Links

* Abstract: https://arxiv.org/abs/2410.07073
* Code: https://github.com/mistralai/mistral-evals/blob/main/eval/tasks/mm_mt_bench.py
* Dataset: https://huggingface.co/datasets/mistralai/MM-MT-Bench
* License: Unknown

## Citations

```bibtex
@misc{agrawal2024pixtral12b,
      title={Pixtral 12B}, 
      author={Pravesh Agrawal and Szymon Antoniak and Emma Bou Hanna and Baptiste Bout and Devendra Chaplot and Jessica Chudnovsky and Diogo Costa and Baudouin De Monicault and Saurabh Garg and Theophile Gervet and Soham Ghosh and Amélie Héliou and Paul Jacob and Albert Q. Jiang and Kartik Khandelwal and Timothée Lacroix and Guillaume Lample and Diego Las Casas and Thibaut Lavril and Teven Le Scao and Andy Lo and William Marshall and Louis Martin and Arthur Mensch and Pavankumar Muddireddy and Valera Nemychnikova and Marie Pellat and Patrick Von Platen and Nikhil Raghuraman and Baptiste Rozière and Alexandre Sablayrolles and Lucile Saulnier and Romain Sauvestre and Wendy Shang and Roman Soletskyi and Lawrence Stewart and Pierre Stock and Joachim Studnia and Sandeep Subramanian and Sagar Vaze and Thomas Wang and Sophia Yang},
      year={2024},
      eprint={2410.07073},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2410.07073}, 
}
```