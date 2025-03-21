# MMMU

MMMU stands for [Massive Multi-discipline Multimodal Understanding](https://arxiv.org/abs/2311.16502) and was developed by Yue et al. from IN.AI Research, University of Waterloo, The Ohio State University, Carnegie Mellon University, University of Victoria and Princeton University and published between Nov 2023 and Jun 2024.

MMMU includes 11.5K meticulously collected multimodal questions from college exams, quizzes, and textbooks, covering six core disciplines: Art & Design, Business, Science, Health & Medicine, Humanities & Social Science, and Tech & Engineering. These questions span 30 subjects and 183 subfields, comprising 30 highly heterogeneous image types, such as charts, diagrams, maps, tables, music sheets, and chemical structures. MMMU focuses on advanced perception and reasoning with domain-specific knowledge, challenging models to perform tasks akin to those faced by experts.

| Statistics                        | Number         |
|-----------------------------------|----------------|
| Total Questions                   | 11550          |
| Total Disciplines/Subjects/Subfields | 6/30/183       |
| Image Types                       | 30             |
| Dev:Validation:Test               | 150:900:10500  |
| Difficulties (Easy: Medium: Hard) | 28%:45%:27%    |
| Multiple-choice Questions         | 10861 (94.03%) |
| Open Questions                    | 689 (5.97%)    |
| Questions with an Explanation     | 2035 (17.62%)  |
| Image in the Question             | 11264 (97.52%) |
| * Images at the beginning         | 2006 (17.81%)  |
| * Images in the middle            | 4159 (36.92%)  |
| * Images at the end               | 5679 (50.42%)  |
| Image in Options                  | 389 (3.37%)    |
| Example with Multiple Images      | 854 (7.39%)    |
| Average question length           | 59.33          |
| Average option length             | 9.17           |
| Average explanation length        | 107.92         |

## Links

* Abstract: https://arxiv.org/abs/2311.16502
* Homepage: https://github.com/MMMU-Benchmark/MMMU
* Dataset: https://huggingface.co/datasets/MMMU/MMMU
* License: [Apache 2.0](https://huggingface.co/datasets/MMMU/MMMU/blob/main/README.md)

## Subjects

MMMU consists of 30 subjects in total from 6 broad categories like science, health and medicine, etc. The categories, subjects, and some subfields are listed in the table below.

| #     | Category           | Subject             | Subfields                                                              | Number | Percentage |
|-------|--------------------|---------------------|------------------------------------------------------------------------|--------|------------|
| 1     | Art & Design (11%) | Art                 | Drawing, Painting, Photography...                                      | 266    | 2.3%       |
| 2     |                    | Design              | Design History, Graphic Design...                                      | 204    | 1.8%       |
| 3     |                    | Music               |                                                                        | 369    | 3.2%       |
| 4     |                    | Art Theory          | Art History, Art Criticism...                                          | 464    | 4.0%       |
| 5     | Science (23%)      | Biology             | Physiology, Genetics Microbiology, Evolution, Cell Biology, Botany...   | 380    | 3.3%       |
| 6     |                    | Chemistry           | Inorganic Chemistry, Organic Chemistry, Physical Chemistry...         | 638    | 5.5%       |
| 7     |                    | Geography           | Geotechnical Engineering, Human Geography, Physical Geography...      | 600    | 5.2%       |
| 8     |                    | Math                | Calculus, Probability and Statistics, Linear Algebra, Geometry, Logic... | 540    | 4.7%       |
| 9     |                    | Physics             | Classical Mechanics, Optics, Electromagnetism, Nuclear Physics...      | 443    | 3.8%       |
| 10    | Health & Medicine (17%) | Basic Med. Sci.     | Anatomy, Neurosciences...                                             | 361    | 3.1%       |
| 11    |                    | Clinical Med.        | Circulatory, Dental, Respiratory...                                   | 360    | 3.12%      |
| 12    |                    | Diagnostics         | Pathology, Electrocardiography...                                       | 197    | 1.7%       |
| 13    |                    | Pharmacy            | Medicinal Chemistry, Biochemistry...                                    | 465    | 4.0%       |
| 14    |                    | Public Health       | Epidemiology, Biostatistics...                                          | 544    | 4.7%       |
| 15    | Tech & Engineering (26%) | Agriculture        | Plant Pathology, Animal Nutrition, Advanced Animal Genetics...        | 422    | 2.8%       |
| 16    |                    | Architecture Eng.   | Surveying and Mapping, Structural Engineering, Civil Engineering...    | 586    | 5.1%       |
| 17    |                    | Computer Sci.       | Data Structure and Algorithm, Computer Network, Databases...           | 406    | 3.5%       |
| 18    |                    | Electronics         | Electrical Circuit, Signal Processing, Analog Electronics...           | 291    | 2.5%       |
| 19    |                    | Energy Power        | Fluid Mechanics, Heat Transfer...                                      | 467    | 4.0%       |
| 20    |                    | Materials           | Mechanics Materials, Materials Science...                              | 493    | 4.3%       |
| 21    |                    | Mechanical Eng.    | Mechanical Design, Fluid Dynamics, Control Systems...                  | 464    | 4.0%       |
| 22    | Business (14%)     | Accounting          | Financial Accounting, Investment...                                     | 415    | 3.6%       |
| 23    |                    | Economics           | Macroeconomics, Econometrics...                                         | 302    | 2.6%       |
| 24    |                    | Finance             | Financial Marketing, Corporate Finance...                               | 390    | 3.4%       |
| 25    |                    | Manage              | Management Models, Cost Management...                                   | 280    | 2.4%       |
| 26    |                    | Marketing           | Market Research                                                        | 216    | 1.9%       |
| 27    | Humanities & Social Sci. (9%) | History            | World History, Modern History...                                     | 313    | 2.71%      |
| 28    |                    | Literature          | Poetry, Fiction, Children's Literature...                              | 147    | 1.27%      |
| 29    |                    | Psychology          | Social Psychology, Personality Psychology...                           | 340    | 2.94%      |
| 30    |                    | Sociology           | Sociology Theory, Politics...                                          | 287    | 2.48%      |

## Example Questions

Below are 2 example questions. The questions follow a multiple-choice question (MCQ) format.

<details>
<summary>Accounting</summary>

Question: Each of the following situations relates to a different company. 

<img src="mmmu/mmmu_accounting_001.png" width="500"> 

For company B, find the missing amounts.

- a. $63,020
- b. $58,410
- c. $71,320
- d. $77,490

Answer: d
</details>

<details>
<summary>Art</summary>

Question: 

<img src="mmmu/mmmu_art_001.png" width="200"> 

by Mark Gertler can be found in the Touchstones Rochdale museum. Which artist belonging to the Bloomsbury group was Gertler in a relationship with?

- a. Vanessa Bell
- b. Eileen Agar
- c. Dora Carrington
- d. Leonora Carrington

Answer: c
</details>

## Implementation

Below are [configurations](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/mmmu) from [EleutherAI's Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness).

<details>
<summary>Generative - MCQ (Exact Match) and Open Ended (Substring)</summary>

```yaml
dataset_path: MMMU/MMMU
validation_split: validation
output_type: generate_until
doc_to_image: !function utils.doc_to_image
doc_to_text: !function utils.doc_to_text
doc_to_target: "answer"
process_results: !function utils.process_results
generation_kwargs:
  until:
    - "<|endoftext|>"
  temperature: 0.0
  do_sample: false
  max_gen_toks: 512
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
metadata:
  version: 0.0
```

```yaml
group: mmmu_val
task:
  - mmmu_val_art_and_design
  - mmmu_val_business
  - mmmu_val_health_and_medicine
  - mmmu_val_humanities_and_social_science
  - mmmu_val_science
  - mmmu_val_tech_and_engineering
aggregate_metric_list:
  - metric: acc
    aggregation: mean
    weight_by_size: true
metadata:
  version: 0.0
```

```python
def process_results(doc, results):
    if doc["question_type"] == "multiple-choice":
        # multichoice logic
        option_strs = ast.literal_eval(doc["options"])
        option_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

        all_choices = option_letters[: len(option_strs)]
        index2ans = {index: ans for index, ans in zip(option_letters, option_strs)}

        pred = parse_multi_choice_response(results[0], all_choices, index2ans)
        # print(pred, all_choices, index2ans)
        is_correct = eval_multi_choice(doc["answer"], pred)
    else:
        # freeform response handling
        pred = parse_open_response(results[0])
        is_correct = eval_open(doc["answer"], pred)

    return {"acc": float(is_correct)}


def eval_multi_choice(gold_i, pred_i):
    """
    Evaluate a multiple choice instance.
    """
    correct = False
    # only they are exactly the same, we consider it as correct
    if isinstance(gold_i, list):
        for answer in gold_i:
            if answer == pred_i:
                correct = True
                break
    else:  # gold_i is a string
        if gold_i == pred_i:
            correct = True
    return correct


def eval_open(gold_i, pred_i):
    """
    Evaluate an open question instance
    """
    correct = False
    if isinstance(gold_i, list):
        # use float to avoid trivial matches
        norm_answers = []
        for answer in gold_i:
            norm_answers.extend(normalize_str(answer))
    else:
        norm_answers = normalize_str(gold_i)
    for pred in pred_i:  # pred is already normalized in parse response phase
        if isinstance(pred, str):  # if it's a string, then find if ans in the pred_i
            for norm_ans in norm_answers:
                # only see if the string answer in the string pred
                if isinstance(norm_ans, str) and norm_ans in pred:
                    if not correct:
                        correct = True
                    break
        else:  # it's a float number
            if pred in norm_answers:
                if not correct:
                    correct = True
                break
    return correct
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/mmmu
</details>

## Citation

```
@misc{yue2024mmmumassivemultidisciplinemultimodal,
      title={MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI}, 
      author={Xiang Yue and Yuansheng Ni and Kai Zhang and Tianyu Zheng and Ruoqi Liu and Ge Zhang and Samuel Stevens and Dongfu Jiang and Weiming Ren and Yuxuan Sun and Cong Wei and Botao Yu and Ruibin Yuan and Renliang Sun and Ming Yin and Boyuan Zheng and Zhenzhu Yang and Yibo Liu and Wenhao Huang and Huan Sun and Yu Su and Wenhu Chen},
      year={2024},
      eprint={2311.16502},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2311.16502}, 
}
```