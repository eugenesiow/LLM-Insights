# GPQA

GPQA stands for [Graduate-Level Google-Proof Q&A Benchmark](https://arxiv.org/abs/2311.12022), developed by Rein et al. from Cohere, Anthropic and New York University and published in Nov 2023. It's a  challenging dataset of multiple-choice questions written by domain experts in biology, physics, and chemistry. The main set consists of 448 questions while a high-quality subset, the GPQA diamond set has 198 questions.

- **Google-proof argument.** The authors argue the questions are Google-proof as "the ground truth is not available to non-experts using easily-found internet resources". Concretely, they argue that highly skilled non-expert validators only reach 34% accuracy, despite spending on average over 30 minutes with unrestricted access to the web.

## Links

* Abstract: https://arxiv.org/abs/2311.12022
* Homepage: https://github.com/idavidrein/gpqa/tree/main
* Dataset: https://huggingface.co/datasets/Idavidrein/gpqa
* License: [CC-BY-4.0](https://huggingface.co/datasets/Idavidrein/gpqa/blob/main/README.md)

## Example Questions

Below are 6 example questions. 2 from each of the subdomains of chemistry, biology, and physics (respectively).

<details>
<summary>Chemistry (general)</summary>

A reaction of a liquid organic compound, which molecules consist of carbon and hydrogen atoms, is performed at 80 centigrade and 20 bar for 24 hours. In the proton nuclear magnetic resonance spectrum, the signals with the highest chemical shift of the reactant are replaced by a signal of the product that is observed about three to four units downfield.  
Compounds from which position in the periodic system of the elements, which are also used in the corresponding large-scale industrial process, have been mostly likely initially added in small amounts?

- A) A metal compound from the fifth period.  
- B) A metal compound from the fifth period and a non-metal compound from the third period.  
- C) A metal compound from the fourth period.  
- D) A metal compound from the fourth period and a non-metal compound from the second period.  
</details>

<details>
<summary>Organic Chemistry</summary>

Methylcyclopentadiene (which exists as a fluxional mixture of isomers) was allowed to react with methyl isoamyl ketone and a catalytic amount of pyrrolidine. A bright yellow, cross-conjugated polyalkenyl hydrocarbon product formed (as a mixture of isomers), with water as a side product. These products are derivatives of fulvene. This product was then allowed to react with ethyl acrylate in a 1:1 ratio. Upon completion of the reaction, the bright yellow color had disappeared.  
How many chemically distinct isomers make up the final product (not counting stereoisomers)?

- A) 2  
- B) 16  
- C) 8  
- D) 4  
</details>

<details>
<summary>Genetics</summary>

If a sperm from species A is injected into an egg from species B and both species have the same number of chromosomes, what would be the main cause of the resulting zygote mortality?

- A) Species specific zona pellucida proteins on the egg cannot bind sperms from a different species.  
- B) Epistatic interactions between the genes of different species.  
- C) Chromosomal incompatibilities will cause failure of meiosis leading to death of zygote.  
- D) Chromosomal recombination will not occur in different species.  
</details>

<details>
<summary>Molecular Biology</summary>

A scientist studies the stress response of barley to increased temperatures and finds a protein that contributes to heat tolerance through the stabilization of the cell membrane. The scientist is very happy and wants to create a heat-tolerant cultivar of diploid wheat. Using databases, they find a heat tolerance protein homologue and start analyzing its accumulation under heat stress. Soon enough, the scientist discovers this protein is not synthesized in the wheat cultivar they study. There are many possible reasons for such behavior, including:

- A) A miRNA targets the protein, which makes exonucleases cut it immediately after the end of translation and before processing in the ER.  
- B) Trimethylation of lysine of H3 histone in position 27 at the promoter of the gene encoding the target protein.  
- C) A stop-codon occurs in the 5’-UTR region of the gene encoding the target protein.  
- D) The proteolysis process disrupts a quaternary structure of the protein, preserving only a tertiary structure.  
</details>

<details>
<summary>Astrophysics</summary>

Astronomers are studying a star with a Teff of approximately 6000 K. They are interested in spectroscopically determining the surface gravity of the star using spectral lines (EW < 100 mA) of two chemical elements, El1 and El2. Given the atmospheric temperature of the star, El1 is mostly in the neutral phase, while El2 is mostly ionized. Which lines are the most sensitive to surface gravity for the astronomers to consider?

- A) El2 I (neutral)  
- B) El1 II (singly ionized)  
- C) El2 II (singly ionized)  
- D) El1 I (neutral)  
</details>

<details>
<summary>Quantum Mechanics</summary>

Suppose we have a depolarizing channel operation given by 𝐸(𝜌). The probability, 𝑝, of the depolarization state represents the strength of the noise. If the Kraus operators of the given state are:  
- 𝐴₀ = √(1 − 3𝑝/4)  
- 𝐴₁ = √(𝑝/4)𝑋  
- 𝐴₂ = √(𝑝/4)𝑌  
- 𝐴₃ = √(𝑝/4)𝑍  

What could be the correct Kraus representation of the state 𝐸(𝜌)?  

- A) 𝐸(𝜌) = (1 − 𝑝)𝜌 + (𝑝/3)(𝑋𝜌𝑋 + 𝑌𝜌𝑌 + 𝑍𝜌𝑍)  
- B) 𝐸(𝜌) = (1 − 𝑝)𝜌 + (𝑝/3)(𝑋𝜌²𝑋 + 𝑌𝜌²𝑌 + 𝑍𝜌²𝑍)  
- C) 𝐸(𝜌) = (1 − 𝑝)𝜌 + (𝑝/4)(𝑋𝜌𝑋 + 𝑌𝜌𝑌 + 𝑍𝜌𝑍)  
- D) 𝐸(𝜌) = (1 − 𝑝)𝜌² + (𝑝/3)(𝑋𝜌²𝑋 + 𝑌𝜌²𝑌 + 𝑍𝜌²𝑍)  
</details>

## Implementation

Below we show [configurations](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/gpqa) from [EleutherAI's Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness).

<details>
<summary>Zeroshot</summary>

```yaml
dataset_path: Idavidrein/gpqa
tag: gpqa
output_type: multiple_choice
process_docs: !function utils.process_docs
training_split: train
# Because huggingface dataset only has train split
validation_split: train
test_split: null
doc_to_text: "What is the correct answer to this question:{{Question}}\nChoices:\n(A) {{choice1}}\n(B) {{choice2}}\n(C) {{choice3}}\n(D) {{choice4}}\nAnswer:"
doc_to_target: answer
doc_to_choice: ["(A)", "(B)", "(C)", "(D)"]
num_fewshot: 0
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
  - metric: acc_norm
    aggregation: mean
    higher_is_better: true
metadata:
  version: 1.0
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/gpqa/zeroshot/_gpqa_zeroshot_yaml
</details>


<details>
<summary>n-shot</summary>

```yaml
dataset_path: Idavidrein/gpqa
tag: gpqa
output_type: multiple_choice
process_docs: !function utils.process_docs
training_split: train
# Because huggingface dataset only has train split
validation_split: train
test_split: null
description: "Here are some example questions from experts. Answer the final question yourself, following the format of the previous questions exactly.\n"
doc_to_text: "Question: {{Question}}\nChoices:\n(A) {{choice1}}\n(B) {{choice2}}\n(C) {{choice3}}\n(D) {{choice4}}\nAnswer:"
doc_to_target: answer
doc_to_choice: ["(A)", "(B)", "(C)", "(D)"]
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
  - metric: acc_norm
    aggregation: mean
    higher_is_better: true
metadata:
  version: 2.0
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/gpqa/n_shot/_gpqa_n_shot_yaml
</details>


<details>
<summary>CoT Zeroshot</summary>

```yaml
dataset_path: Idavidrein/gpqa
tag: gpqa
output_type: generate_until
process_docs: !function utils.process_docs
training_split: train
# Because huggingface dataset only has train split
validation_split: train
test_split: null
doc_to_text: "What is the correct answer to this question:{{Question}}\nChoices:\n(A) {{choice1}}\n(B) {{choice2}}\n(C) {{choice3}}\n(D) {{choice4}}\nLet's think step by step: "
doc_to_target: answer
filter_list:
  - name: "strict-match"
    filter:
      - function: "regex"
        regex_pattern: "(?<=The answer is )(.*)(?=.)"
      - function: "take_first"
  - name: "flexible-extract"
    filter:
      - function: "multi_choice_regex"
        group_select: -1
        ignore_case: true
        ignore_punctuation: true
        regex_pattern: "(\\([A-Z]\\))"
      - function: "take_first"
generation_kwargs:
  until:
    - "</s>"
  do_sample: false
  temperature: 0.0
num_fewshot: 0
metric_list:
  - metric: exact_match
    aggregation: mean
    higher_is_better: true
    ignore_case: true
    ignore_punctuation: true
metadata:
  version: 1.0
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/gpqa/cot_zeroshot/_gpqa_cot_zeroshot_yaml
</details>

<details>
<summary>CoT n-shot</summary>

```yaml
dataset_path: Idavidrein/gpqa
tag: gpqa
output_type: generate_until
process_docs: !function utils.process_docs
training_split: train
# Because huggingface dataset only has train split
validation_split: train
test_split: null
description: "Here are some example questions from experts. Answer the final question yourself, following the format of the previous questions exactly.\n"
doc_to_text: "Question: {{Question}}\nChoices:\n(A) {{choice1}}\n(B) {{choice2}}\n(C) {{choice3}}\n(D) {{choice4}}\nLet's think step by step: "
doc_to_target: answer
filter_list:
  - name: "strict-match"
    filter:
      - function: "regex"
        regex_pattern: "(?<=The answer is )(.*)(?=.)"
      - function: "take_first"
  - name: "flexible-extract"
    filter:
      - function: "multi_choice_regex"
        group_select: -1
        ignore_case: true
        ignore_punctuation: true
        regex_pattern: "(\\([A-Z]\\))"
      - function: "take_first"
generation_kwargs:
  until:
    - "</s>"
  do_sample: false
  temperature: 0.0
metric_list:
  - metric: exact_match
    aggregation: mean
    higher_is_better: true
    ignore_case: true
    ignore_punctuation: true
metadata:
  version: 2.0
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/gpqa/cot_n_shot/_gpqa_cot_n_shot_yaml
</details>

<details>
<summary>Generative n-shot</summary>

```yaml
dataset_path: Idavidrein/gpqa
tag: gpqa
output_type: generate_until
process_docs: !function utils.process_docs
training_split: train
# Because huggingface dataset only has train split
validation_split: train
test_split: null
description: "Here are some example questions from experts. Answer the final question yourself, following the format of the previous questions exactly.\n"
doc_to_text: "Question: {{Question}}\nChoices:\n(A) {{choice1}}\n(B) {{choice2}}\n(C) {{choice3}}\n(D) {{choice4}}\nAnswer:"
doc_to_target: answer
filter_list:
  - name: "strict-match"
    filter:
      - function: "regex"
        regex_pattern: "(?<=The answer is )(.*)(?=.)"
      - function: "take_first"
  - name: "flexible-extract"
    filter:
      - function: "multi_choice_regex"
        group_select: -1
        ignore_case: true
        ignore_punctuation: true
        regex_pattern: "(\\([A-Z]\\))"
      - function: "take_first"
generation_kwargs:
  until:
    - "</s>"
    - "Question:"
    - "<|im_end|>"
  temperature: 0.0
metric_list:
  - metric: exact_match
    aggregation: mean
    higher_is_better: true
    ignore_case: true
    ignore_punctuation: true
metadata:
  version: 2.0
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/gpqa/generative/_gpqa_generative_n_shot_yaml
</details>


## Citation

```
@misc{rein2023gpqa,
      title={GPQA: A Graduate-Level Google-Proof Q&A Benchmark},
      author={David Rein and Betty Li Hou and Asa Cooper Stickland and Jackson Petty and Richard Yuanzhe Pang and Julien Dirani and Julian Michael and Samuel R. Bowman},
      year={2023},
      eprint={2311.12022},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```