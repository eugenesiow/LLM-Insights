# MMLU

MMLU stands for [Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300) and MMLU-Pro stands for [Massive Multitask Language Understanding - Professional](https://arxiv.org/abs/2406.01574). MMLU was developed by Hendrycks et al. from UC Berkeley, Columbia University, UChicago and UIUC and published between Sep 2020 and Jan 2021. MMLU-Pro was developed by Wang et al. from University of Waterloo, University of Toronto and Carnegie Mellon University and published between Jun 2024 and Nov 2024.

MMLU is a benchmark that covers 57 tasks including elementary mathematics, US history, computer science, law, and more. To attain high accuracy on this test, models must possess extensive world knowledge and problem solving ability. The format is multiple choice questions and answers with four options (A, B, C, D). There are 15,908 questions in total (few-shot dev set has 5 questions per subject, validation set has 1,540 questions, and the test set has 14,079 questions). Each subject contains 100 test examples at the minimum.

MMLU-Pro is an enhanced dataset designed to extend the mostly knowledge-driven MMLU benchmark by integrating more challenging, reasoning-focused questions and expanding the choice set from four to ten options (3x more distractors than MMLU). There are 12,032 questions in total, while each question has ten options, which the authors argue significantly reduces the probability of a correct guess by chance and boosts the benchmark's difficulty and robustness. The portion of challenging college-level exam problems is also increased which  requires deliberate reasoning in different domains to derive the final answer.

## Links

### MMLU

* Abstract: https://arxiv.org/abs/2009.03300
* Homepage: https://github.com/hendrycks/test
* Dataset: https://huggingface.co/datasets/cais/mmlu
* License: [MIT](https://huggingface.co/datasets/cais/mmlu/blob/main/README.md)

### MMLU-Pro

* Abstract: https://arxiv.org/abs/2406.01574
* Homepage: https://github.com/TIGER-AI-Lab/MMLU-Pro
* Dataset: https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro
* License: [MIT](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/blob/main/README.md)

## Tasks

### MMLU

MMLU consists of 57 tasks in total (trivia: which is also [the number of Atari games](https://arxiv.org/abs/1207.4708)). The tasks, their tested concepts and their supercategories (STEM, the humanities, the social sciences, and more) are listed in the table below.

| # | Task | Tested Concepts | Supercategory |
|---|---|---|---|
| 1 | Abstract Algebra | Groups, rings, fields, vector spaces, ... | STEM |
| 2 | Anatomy | Central nervous system, circulatory system, ... | STEM |
| 3 | Astronomy | Solar system, galaxies, asteroids, ... | STEM |
| 4 | Business Ethics | Corporate responsibility, stakeholders, regulation, ... | Other |
| 5 | Clinical Knowledge | Spot diagnosis, joints, abdominal examination, ... | Other |
| 6 | College Biology | Cellular structure, molecular biology, ecology, ... | STEM |
| 7 | College Chemistry | Analytical, organic, inorganic, physical, ... | STEM |
| 8 | College Computer Science | Algorithms, systems, graphs, recursion, ... | STEM |
| 9 | College Mathematics | Differential equations, real analysis, combinatorics, ... | STEM |
| 10 | College Medicine | Introductory biochemistry, sociology, reasoning, ... | Other |
| 11 | College Physics | Electromagnetism, thermodynamics, special relativity, ... | STEM |
| 12 | Computer Security | Cryptography, malware, side channels, fuzzing, ... | STEM |
| 13 | Conceptual Physics | Newton’s laws, rotational motion, gravity, sound, ... | STEM |
| 14 | Econometrics | Volatility, long-run relationships, forecasting, ... | Social Sciences |
| 15 | Electrical Engineering | Circuits, power systems, electrical drives, ... | STEM |
| 16 | Elementary Mathematics | Word problems, multiplication, remainders, rounding, ... | STEM |
| 17 | Formal Logic | Propositions, predicate logic, first-order logic, ... | Humanities |
| 18 | Global Facts | Extreme poverty, literacy rates, life expectancy, ... | Other |
| 19 | High School Biology | Natural selection, heredity, cell cycle, Krebs cycle, ... | STEM |
| 20 | High School Chemistry | Chemical reactions, ions, acids and bases, ... | STEM |
| 21 | High School Computer Science | Arrays, conditionals, iteration, inheritance, ... | STEM |
| 22 | High School European History | Renaissance, reformation, industrialization, ... | Humanities |
| 23 | High School Geography | Population migration, rural land-use, urban processes, ... | Social Sciences |
| 24 | High School Gov’t and Politics | Branches of government, civil liberties, political ideologies, ... | Social Sciences |
| 25 | High School Macroeconomics | Economic indicators, national income, international trade, ... | Social Sciences |
| 26 | High School Mathematics | Pre-algebra, algebra, trigonometry, calculus, ... | STEM |
| 27 | High School Microeconomics | Supply and demand, imperfect competition, market failure, ... | Social Sciences |
| 28 | High School Physics | Kinematics, energy, torque, fluid pressure, ... | STEM |
| 29 | High School Psychology | Behavior, personality, emotions, learning, ... | Social Sciences |
| 30 | High School Statistics | Random variables, sampling distributions, chi-square tests, ... | STEM |
| 31 | High School US History | Civil War, the Great Depression, The Great Society, ... | Humanities |
| 32 | High School World History | Ottoman empire, economic imperialism, World War I, ... | Humanities |
| 33 | Human Aging | Senescence, dementia, longevity, personality changes, ... | Other |
| 34 | Human Sexuality | Pregnancy, sexual differentiation, sexual orientation, ... | Social Sciences |
| 35 | International Law | Human rights, sovereignty, law of the sea, use of force, ... | Humanities |
| 36 | Jurisprudence | Natural law, classical legal positivism, legal realism, ... | Humanities |
| 37 | Logical Fallacies | No true Scotsman, base rate fallacy, composition fallacy, ... | Humanities |
| 38 | Machine Learning | SVMs, VC dimension, deep learning architectures, ... | STEM |
| 39 | Management | Organizing, communication, organizational structure, ... | Other |
| 40 | Marketing | Segmentation, pricing, market research, ... | Other |
| 41 | Medical Genetics | Genes and cancer, common chromosome disorders, ... | Other |
| 42 | Miscellaneous | Agriculture, Fermi estimation, pop culture, ... | Other |
| 43 | Moral Disputes | Freedom of speech, addiction, the death penalty, ... | Humanities |
| 44 | Moral Scenarios | Detecting physical violence, stealing, externalities, ... | Humanities |
| 45 | Nutrition | Metabolism, water-soluble vitamins, diabetes, ... | Other |
| 46 | Philosophy | Skepticism, phronesis, skepticism, Singer’s Drowning Child, ... | Humanities |
| 47 | Prehistory | Neanderthals, Mesoamerica, extinction, stone tools, ... | Humanities |
| 48 | Professional Accounting | Auditing, reporting, regulation, valuation, ... | Other |
| 49 | Professional Law | Torts, criminal law, contracts, property, evidence, ... | Humanities |
| 50 | Professional Medicine | Diagnosis, pharmacotherapy, disease prevention, ... | Other |
| 51 | Professional Psychology | Diagnosis, biology and behavior, lifespan development, ... | Social Sciences |
| 52 | Public Relations | Media theory, crisis management, intelligence gathering, ... | Social Sciences |
| 53 | Security Studies | Environmental security, terrorism, weapons of mass destruction, ... | Social Sciences |
| 54 | Sociology | Socialization, cities and community, inequality and wealth, ... | Social Sciences |
| 55 | US Foreign Policy | Soft power, Cold War foreign policy, isolationism, ... | Social Sciences |
| 56 | Virology | Epidemiology, coronaviruses, retroviruses, herpesviruses, ... | Other |
| 57 | World Religions | Judaism, Christianity, Islam, Buddhism, Jainism, ... | Humanities |

### MMLU-Pro

MMLU-Pro consists of 14 diverse domains or disciplines (which are roughly what MMLU calls tasks, at a higher granularity). The disciplines and the distribution of question origin across different disciplines are listed in the table below (the percentages in parentheses represent the proportion of each source relative to the total number of questions in that discipline).


| #     | Disciplines       | Total Number | MMLU              | STEM Website      | TheoremQA         | Scibench           |
|-------|-------------------|--------------|-------------------|-------------------|-------------------|--------------------|
| 1     | Math              | 1351         | 846 (62.66%)      | 0                 | 344 (25.46%)      | 161 (11.92%)      |
| 2     | Physics           | 1299         | 411 (31.64%)      | 617 (47.50%)      | 104 (8.01%)       | 167 (12.86%)      |
| 3     | Chemistry         | 1132         | 178 (15.72%)      | 741 (65.46%)      | 0                 | 213 (18.82%)      |
| 4     | Law               | 1101         | 1101 (100%)       | 0                 | 0                 | 0                  |
| 5     | Engineering       | 969          | 67 (6.92%)        | 902 (93.08%)      | 0                 | 0                  |
| 6     | Other             | 924          | 924 (100%)        | 0                 | 0                 | 0                  |
| 7     | Economics         | 844          | 444 (52.61%)      | 400 (47.39%)      | 0                 | 0                  |
| 8     | Health            | 818          | 818 (100%)        | 0                 | 0                 | 0                  |
| 9     | Psychology        | 798          | 493 (61.78%)      | 305 (38.22%)      | 0                 | 0                  |
| 10    | Business          | 789          | 155 (19.65%)      | 560 (70.99%)      | 74 (9.38%)        | 0                  |
| 11    | Biology           | 717          | 219 (30.54%)      | 498 (69.46%)      | 0                 | 0                  |
| 12    | Philosophy        | 499          | 499 (100%)        | 0                 | 0                 | 0                  |
| 13    | Computer Science  | 410          | 274 (66.83%)      | 60 (14.63%)       | 76 (18.54%)       | 0                  |
| 14    | History           | 381          | 381 (100%)        | 0                 | 0                 | 0                  |
|       | **Total**         | 12032        | 6810 (56.60%)     | 4083 (33.93%)     | 598 (4.97%)       | 541 (4.50%)        |

## Example Questions

Below are 4 example questions. 2 from MMLU and 2 from MMLU-Pro. The questions follow a multiple-choice question (MCQ) format.

<details>
<summary>MMLU - Astronomy</summary>

Question: What is true for a type-Ia ("type one-a") supernova?

- a. This type occurs in binary systems.
- b. This type occurs in young galaxies.
- c. This type produces gamma-ray bursts.
- d. This type produces high amounts of X-rays.

Answer: a
</details>

<details>
<summary>MMLU - Philosophy</summary>

Question: Aesthetics deals with objects that are_____.

- a. essential to our existence
- b. unimportant to most people
- c. not essential to our existence
- d. rarely viewed

Answer: c
</details>

<details>
<summary>MMLU-Pro - Business</summary>

Question: There are two main issues associated with _____ sizing. _______ is a key issue as due to the information policy of the corporation it can be argued that employees have a right to know if they are being made redundant. _______ is a second issue, particularly the ________ package that employees receive when laid off.

- a. Down, Autonomy, Remuneration, Benefit
- b. Down, Involvement, Independence, Benefit
- c. Up, Independence, Involvement, Benefit
- d. Down, Privacy, Autonomy, Benefit
- e. Up, Involvement, Autonomy, Compensation
- f. Down, Independence, Autonomy, Compensation
- g. Up, Involvement, Remuneration, Severance
- h. Up, Privacy, Remuneration, Severance
- i. Up, Autonomy, Remuneration, Compensation
- j. Down, Involvement, Remuneration, Compensation

Answer: j
</details>

<details>
<summary>MMLU-Pro - Chemistry</summary>

Question: An unknown substance is found to have a high melting point. In addition, it is a poor conductor of electricity and does not dissolve in water. The substance most likely contains

- a. dipole-dipole bonding
- b. ionic bonding
- c. covalent network bonding
- d. nonpolar covalent bonding
- e. coordinate covalent bonding
- f. London dispersion bonding
- g. van der Waals bonding
- h. metallic bonding
- i. hydrogen bonding
- j. polar covalent bonding

Answer: c
</details>

## Citation

Original **MMLU** Paper: [Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300)

```
@misc{hendrycks2021measuringmassivemultitasklanguage,
      title={Measuring Massive Multitask Language Understanding}, 
      author={Dan Hendrycks and Collin Burns and Steven Basart and Andy Zou and Mantas Mazeika and Dawn Song and Jacob Steinhardt},
      year={2021},
      eprint={2009.03300},
      archivePrefix={arXiv},
      primaryClass={cs.CY},
      url={https://arxiv.org/abs/2009.03300}, 
}
```

**MMLU-Pro** Paper: [MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://arxiv.org/abs/2406.01574)

```
@misc{wang2024mmluprorobustchallengingmultitask,
      title={MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark}, 
      author={Yubo Wang and Xueguang Ma and Ge Zhang and Yuansheng Ni and Abhranil Chandra and Shiguang Guo and Weiming Ren and Aaran Arulraj and Xuan He and Ziyan Jiang and Tianle Li and Max Ku and Kai Wang and Alex Zhuang and Rongqi Fan and Xiang Yue and Wenhu Chen},
      year={2024},
      eprint={2406.01574},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2406.01574}, 
}
```