# Global-MMLU

Global-MMLU stands for [Global Massive Multitask Language Understanding](https://arxiv.org/abs/2412.03304) and is a multilingual evaluation set spanning 42 languages, including English. This dataset combines machine translations for [MMLU](../general/mmlu.md) questions along with professional translations and crowd-sourced post-edits.
It also includes cultural sensitivity annotations for a subset of the questions (2850 questions per language) and classifies them as *Culturally Sensitive* (CS) or *Culturally Agnostic* (CA). These annotations were collected as part of an open science initiative led by [Cohere For AI](https://cohere.com/research) in collaboration with many external collaborators from both industry and academia.

Global-MMLU also includes a subset called the [Global-MMLU (Lite)](https://huggingface.co/datasets/CohereForAI/Global-MMLU-Lite) version. This dataset is more balanced, containing 200 samples each for CA and CS subsets for each language while only providing coverage for 15 languages with human translations. 

## Statistics

### Global-MMLU

| Type of Annotation | Instances per language | No. of languages | Total instances
|--------------------|------------------------|------------------|----------------|
| Culturally Sensitive | 792 | 42 | 33,264 |
| Culturally Agnostic | 2058 |42 | 86,436 |

| Split | No. of instances | Language Coverage |
|-------|------------------|-------------------|
| test | 589,764 | 42 |
| dev  | 11,970 | 42 |

### Global-MMLU (Lite)

| Type of Annotation | Instances per language | No. of languages | Total instances
|--------------------|------------------------|------------------|----------------|
| Culturally Sensitive | 200 | 15 | 3,000 |
| Culturally Agnostic | 200 |15 | 3,000 |

| Split | No. of instances | Language Coverage |
|-------|------------------|-------------------|
| test | 6,000 | 15 |
| dev  | 4,275 | 15 |

## Languages

The Global-MMLU dataset covers 42 languages: 20 high-resource, 9 mid-resource, and 13 low-resource languages while the Global-MMLU (Lite) dataset covers 15 languages. The following are details about exactly which languages are included in the datasets.

<details>
<summary> Global-MMLU Languages </summary>

| ISO Code | Language | Resources | 
|----------|----------|-----------|
| `am` | Amharic | Low |
| `ar` | Arabic (Standard)| High |
| `bn` | Bengali | Mid |
| `de` | German | High |
| `el` | Greek | Mid |
| `en` | English | High |
| `fil` | Filipino | Mid |
| `fr` | French | High |
| `ha` | Hausa | Low |
| `he` | Hebrew | Mid |
| `hi` | Hindi | High |
| `ig` | Igbo | Low |
| `id` | Indonesian | Mid |
| `it` | Italian | High |
| `ja` | Japanese | High |
| `ky` | Kyrgyz | Low |
| `ko` | Korean | Mid |
| `lt` | Lithuanian | Mid |
| `mg` | Malagasy | Low |
| `ms` | Malay | Mid |
| `ne` | Nepali | Low |
| `nl` | Dutch | High |
| `ny` | Chichewa | Low |
| `fa` | Persian | High |
| `pl` | Polish | High |
| `pt` | Portuguese | High |
| `ru` | Russian | High |
| `si` | Sinhala | Low |
| `sn` | Shona | Low |
| `so` | Somali | Low |
| `es` | Spanish | High |
| `sr` | Serbian | High |
| `sw` | Swahili | Low |
| `sv` | Swedish | High |
| `te` | Telugu | Low |
| `tr` | Turkish | High |
| `uk` | Ukrainian | Mid |
| `vi` | Vietnamese | High |
| `yo` | Yorùbá | Low |
| `zh` | Chinese (Simplified) | High |
</details>

<details>
<summary> Global-MMLU (Lite) Languages </summary>

| ISO Code | Language | Resources | 
|----------|----------|-----------|
| `ar` | Arabic (Standard)| High |
| `bn` | Bengali | Mid |
| `de` | German | High |
| `en` | English | High |
| `fr` | French | High |
| `hi` | Hindi | High |
| `id` | Indonesian | Mid |
| `it` | Italian | High |
| `ja` | Japanese | High |
| `ko` | Korean | Mid |
| `pt` | Portuguese | High |
| `es` | Spanish | High |
| `sw` | Swahili | Low |
| `yo` | Yorùbá | Low |
| `zh` | Chinese (Simplified) | High |
</details>

## Links

### Global-MMLU

* Abstract: https://arxiv.org/abs/2412.03304
* Dataset: https://huggingface.co/datasets/CohereForAI/Global-MMLU
* License: [Apache 2.0](https://huggingface.co/datasets/CohereForAI/Global-MMLU/blob/main/README.md)

### Global-MMLU (Lite)

* Dataset: https://huggingface.co/datasets/CohereForAI/Global-MMLU-Lite
* License: [Apache 2.0](https://huggingface.co/datasets/CohereForAI/Global-MMLU-Lite/blob/main/README.md)

## Implementation

Below are [configurations](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/global_mmlu) from [EleutherAI's Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness).

<details>
<summary>en</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU-Lite
dataset_name: en
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: default
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/en/_en_template_yaml
</details>

<details>
<summary>nl</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: nl
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/nl/_nl_template_yaml
</details>

<details>
<summary>fr</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU-Lite
dataset_name: fr
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: default
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/fr/_fr_template_yaml
</details>

<details>
<summary>vi</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: vi
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/vi/_vi_template_yaml
</details>

<details>
<summary>mg</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: mg
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/mg/_mg_template_yaml
</details>

<details>
<summary>pl</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: pl
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/pl/_pl_template_yaml
</details>

<details>
<summary>fa</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: fa
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/fa/_fa_template_yaml
</details>

<details>
<summary>sv</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: sv
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/sv/_sv_template_yaml
</details>

<details>
<summary>ky</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: ky
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/ky/_ky_template_yaml
</details>

<details>
<summary>ja</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU-Lite
dataset_name: ja
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: default
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/ja/_ja_template_yaml
</details>

<details>
<summary>cs</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: cs
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/cs/_cs_template_yaml
</details>

<details>
<summary>fil</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: fil
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/fil/_fil_template_yaml
</details>

<details>
<summary>hi</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU-Lite
dataset_name: hi
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: default
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/hi/_hi_template_yaml
</details>

<details>
<summary>it</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU-Lite
dataset_name: it
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: default
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/it/_it_template_yaml
</details>

<details>
<summary>yo</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU-Lite
dataset_name: yo
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: default
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/yo/_yo_template_yaml
</details>

<details>
<summary>sn</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: sn
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/sn/_sn_template_yaml
</details>

<details>
<summary>el</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: el
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/el/_el_template_yaml
</details>

<details>
<summary>lt</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: lt
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/lt/_lt_template_yaml
</details>

<details>
<summary>sr</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: sr
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/sr/_sr_template_yaml
</details>

<details>
<summary>so</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: so
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/so/_so_template_yaml
</details>

<details>
<summary>ko</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU-Lite
dataset_name: ko
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: default
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/ko/_ko_template_yaml
</details>

<details>
<summary>ig</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: ig
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/ig/_ig_template_yaml
</details>

<details>
<summary>pt</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU-Lite
dataset_name: pt
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: default
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/pt/_pt_template_yaml
</details>

<details>
<summary>he</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: he
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/he/_he_template_yaml
</details>

<details>
<summary>ru</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: ru
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/ru/_ru_template_yaml
</details>

<details>
<summary>tr</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: tr
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/tr/_tr_template_yaml
</details>

<details>
<summary>am</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: am
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/am/_am_template_yaml
</details>

<details>
<summary>te</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: te
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/te/_te_template_yaml
</details>

<details>
<summary>de</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU-Lite
dataset_name: de
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: default
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/de/_de_template_yaml
</details>

<details>
<summary>ar</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU-Lite
dataset_name: ar
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: default
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/ar/_ar_template_yaml
</details>

<details>
<summary>id</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU-Lite
dataset_name: id
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: default
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/id/_id_template_yaml
</details>

<details>
<summary>ms</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: ms
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/ms/_ms_template_yaml
</details>

<details>
<summary>ne</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: ne
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/ne/_ne_template_yaml
</details>

<details>
<summary>uk</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: uk
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/uk/_uk_template_yaml
</details>

<details>
<summary>sw</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU-Lite
dataset_name: sw
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: default
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/sw/_sw_template_yaml
</details>

<details>
<summary>ro</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: ro
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/ro/_ro_template_yaml
</details>

<details>
<summary>si</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: si
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/si/_si_template_yaml
</details>

<details>
<summary>bn</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU-Lite
dataset_name: bn
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: default
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/bn/_bn_template_yaml
</details>

<details>
<summary>zh</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU-Lite
dataset_name: zh
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: default
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/zh/_zh_template_yaml
</details>

<details>
<summary>ha</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: ha
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/ha/_ha_template_yaml
</details>

<details>
<summary>ny</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU
dataset_name: ny
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/ny/_ny_template_yaml
</details>

<details>
<summary>es</summary>

```yaml
dataset_path: CohereForAI/Global-MMLU-Lite
dataset_name: es
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: default
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{option_a}}\nB. {{option_b}}\nC. {{option_c}}\nD. {{option_d}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0

```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/es/_es_template_yaml
</details>

## Citation

```bibtex
@misc{singh2024globalmmluunderstandingaddressing,
      title={Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation},
      author={Shivalika Singh and Angelika Romanou and Clémentine Fourrier and David I. Adelani and Jian Gang Ngui and Daniel Vila-Suero and Peerat Limkonchotiwat and Kelly Marchisio and Wei Qi Leong and Yosephine Susanto and Raymond Ng and Shayne Longpre and Wei-Yin Ko and Madeline Smith and Antoine Bosselut and Alice Oh and Andre F. T. Martins and Leshem Choshen and Daphne Ippolito and Enzo Ferrante and Marzieh Fadaee and Beyza Ermis and Sara Hooker},
      year={2024},
      eprint={2412.03304},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.03304},
}
```
