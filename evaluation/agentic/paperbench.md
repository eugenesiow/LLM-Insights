# PaperBench

PaperBench, published by OpenAI in the paper [PaperBench: Evaluating AI's Ability to Replicate AI Research](https://arxiv.org/abs/2504.01848) by Starace et al. in Apr 2025, evaluates the ability of AI agents to replicate state-of-the-art AI research. Agents must replicate 20 ICML 2024 Spotlight and Oral papers from scratch, including understanding paper contributions, developing a codebase, and successfully executing experiments. For objective evaluation, rubrics hierarchically decompose each replication task into smaller
sub-tasks with clear grading criteria. In total, PaperBench contains 8,316 individually gradable 26 tasks.

The following are the papers in the benchmark, their ICML track, topic and the number of rubric nodes.

| Paper                                                                                              | Source    | ICML Topic                             | Nodes |
|----------------------------------------------------------------------------------------------------|-----------|----------------------------------------|-------|
| APT: Adaptive Pruning and Tuning Pretrained Language Models for Efficient Training and Inference | Oral      | Deep Learning: LLMs                    | 172   |
| All-in-one simulation-based inference                                                              | Oral      | Probabilistic Methods                  | 234   |
| Batch and match: black-box variational inference with a score-divergence based objective          | Spotlight | Probabilistic Methods - Variational Inference | 1021  |
| BBox-Adapter: Lightweight Adopting for Black-Box Large Language Models                             | Spotlight | Deep Learning: LLMs                    | 422   |
| Bridging Data Gaps in Diffusion Models with Adversarial Noise-Based Transfer Learning              | Spotlight | Theory: Domain Adapt. & Transfer Learning | 207   |
| Unsupervised Zero-Shot Reinforcement Learning via Functional Reward Encodings                       | Spotlight | Deep RL                                | 636   |
| Fine-tuning Reinforcement Learning Models is Secretly a Forgetting Mitigation Problem               | Spotlight | Reinforcement Learning: Deep RL        | 233   |
| Refined Coreset Selection: Towards Minimal Coreset Size under Model Performance Constraints        | Spotlight | Data-Centric AI                        | 1471  |
| LCA-on-the-Line: Benchmarking Out of Distribution Generalization with Class Taxonomies             | Oral      | Deep Learning: Robustness              | 1048  |
| A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity             | Oral      | Deep Learning: LLMs                    | 128   |
| Challenges in Training PINNs: A Loss Landscape Perspective                                         | Spotlight | Deep Learning                          | 2551  |
| RICE: Breaking Through the Training Bottlenecks of Reinforcement Learning with Explanation        | Spotlight | Deep RL                                | 489   |
| Robust CLIP: Unsupervised Adversarial Fine-tuning of Vision Embeddings for Robust Large Vision-Language Models | Oral      | Deep Learning: Robustness              | 146   |
| Sample-specific Masks for Visual Reprogramming-based Prompting                                    | Spotlight | Misc. Aspects of ML: General ML Techniques | 396   |
| SAPG: Split and Aggregate Policy Gradients                                                          | Oral      | Deep RL                                | 279   |
| Sequential Neural Score Estimation: Likelihood-Free Inference with Conditional Score Based Diffusion Models | Spotlight | Probabilistic Methods                  | 123   |
| Stay on Topic with Classifier-Free Guidance                                                        | Spotlight | Deep Learning: LLMs                    | 186   |
| Stochastic Interpolants with Data-Dependent Couplings                                               | Spotlight | Generative Models                      | 94    |
| Test-Time Model Adaptation with Only Forward Passes                                                | Oral      | Distributions Shift and OOD            | 236   |
| What Will My Model Forget?: Forecasting Forgotten Examples in Language Model Refinement             | Spotlight | Deep Learning: Everything Else         | 1146  |

The counts of the rubric nodes for each of the papers (shorthand for the rubric name refers to the papers from above in order), the leaf nodes and the types of the leaf nodes (Code Dev + Execution + Res Match = Leaf Nodes). 

| Rubric                                              | Total Nodes | Leaf Nodes | Code Dev. | Execution | Res. Match |
|-----------------------------------------------------|-------------|------------|-----------|-----------|------------|
| adaptive-pruning                                    | 172         | 123        | 86        | 10        | 27         |
| all-in-one                                          | 234         | 174        | 92        | 62        | 20         |
| bam                                                 | 1021        | 789        | 255       | 518       | 16         |
| bbox                                                | 122         | 279        | 55        | 16        | 53         |
| bridging-data-gaps                                  | 207         | 172        | 55        | 46        | 71         |
| fre                                                 | 636         | 437        | 306       | 104       | 77         |
| frtl                                                | 233         | 178        | 120       | 20        | 38         |
| lbcs                                                | 1471        | 916        | 418       | 85        | 43         |
| lca-on-the-line                                     | 1048        | 819        | 403       | 370       | 46         |
| mechanistic-understanding                           | 122         | 86         | 56        | 12        | 10         |
| pinn                                                | 2551        | 1963       | 126       | 1815      | 22         |
| rice                                                | 489         | 361        | 72        | 115       | 11         |
| robust-clip                                         | 146         | 106        | 80        | 20        | 13         |
| sample-specific-masks                               | 198         | 331        | 67        | 223       | 21         |
| sapg                                                | 279         | 206        | 77        | 64        | 65         |
| sequential-neural-score-estimation                  | 123         | 92         | 77        | 5         | 0          |
| stay-on-topic-with-classifier-free-guidance         | 186         | 121        | 70        | 35        | 16         |
| stochastic-interplants                              | 94          | 69         | 58        | 7         | 7          |
| test-time-model-adaptation                          | 236         | 163        | 86        | 36        | 41         |
| what-will-my-model-forget                           | 1146        | 921        | 872       | 28        | 21         |

Each leaf node has one of three possible *requirement types*, which determines how it is graded.

1. **Result Match** leaf nodes assess whether the executed submission contains evidence of replicating a particular result from the paper. Result Match nodes are graded by looking at `reproduce.sh` and `reproduce.log`, and any files created or modified in the reproduction step.

2. **Execution** leaf nodes assess whether some particular execution result has occurred when running the `reproduce.sh` script. Given that Result Match nodes are particularly challenging to achieve, having multiple associated Execution nodes allow submissions to receive credit for marking partial progress towards a result even if the corresponding Result Match node isn’t achieved. Execution nodes are assessed by looking at the `reproduce.sh`, the `reproduce.log`, and the source code.

3. **Code Development** leaf nodes assess whether the candidate’s source code appears to contain a correct implementation of some requirement. Code Development nodes award partial credit towards the achievement of Execution nodes; for example, a submission may have written correct code but failed to execute it correctly in the `reproduce.sh`.

## Links

* Abstract: https://arxiv.org/abs/2504.01848
* Blog: https://openai.com/index/paperbench/
* Code: https://github.com/openai/preparedness/blob/main/project/paperbench/README.md
* License: [MIT](https://github.com/openai/preparedness?tab=MIT-1-ov-file#readme)

## Citations

```bibtex
@misc{starace2025paperbenchevaluatingaisability,
      title={PaperBench: Evaluating AI's Ability to Replicate AI Research}, 
      author={Giulio Starace and Oliver Jaffe and Dane Sherburn and James Aung and Jun Shern Chan and Leon Maksin and Rachel Dias and Evan Mays and Benjamin Kinsella and Wyatt Thompson and Johannes Heidecke and Amelia Glaese and Tejal Patwardhan},
      year={2025},
      eprint={2504.01848},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2504.01848}, 
}
```