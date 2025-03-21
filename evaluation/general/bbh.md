# BBH

[Beyond the Imitation Game Benchmark (BIG-bench)](https://github.com/google/BIG-bench) is a diverse evaluation suite with [214 tasks](https://github.com/google/BIG-bench/blob/main/bigbench/benchmark_tasks/README.md) for language models (e.g. answering multiple-choice questions distinguishing [cause and effect](https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/cause_and_effect)). The benchmark is intended to probe large language models for their capabilities. 

[BIG-Bench Hard (BBH)](https://github.com/suzgunmirac/BIG-Bench-Hard) focuses on a suite of only 23 challenging BIG-Bench tasks. They were selected in this subset as they were the tasks for which prior language model evaluations did not outperform the average human-rater (circa 2022), e.g. [causal judgment](https://github.com/suzgunmirac/BIG-Bench-Hard/blob/main/bbh/causal_judgement.json) or [multi-step arithmetic](https://github.com/suzgunmirac/BIG-Bench-Hard/blob/main/bbh/multistep_arithmetic_two.json).

## Links

* Abstract: https://arxiv.org/abs/2210.09261
* Homepage: https://github.com/suzgunmirac/BIG-Bench-Hard/
* Dataset: https://github.com/suzgunmirac/BIG-Bench-Hard/tree/main/bbh
* License: [MIT](https://github.com/suzgunmirac/BIG-Bench-Hard?tab=MIT-1-ov-file#readme)

## Example Questions

Below are 3 example tasks. For each example task, 3 samples are listed. They are listed in a JSON object with an `input` key that represents the question and a `target` key that represents the answer.

<details>
<summary>Boolean Expressions</summary>

{"input": "not ( True ) and ( True ) is", "target": "False"}

{"input": "True and not not ( not False ) is", "target": "True"}

{"input": "not True or False or ( False ) is", "target": "False"}
</details>

<details>
<summary>Causal Judgement</summary>
 
{"input": "How would a typical person answer each of the following questions about causation?\nA machine is set up in such a way that it will short circuit if both the black wire and the red wire touch the battery at the same time. The machine will not short circuit if just one of these wires touches the battery. The black wire is designated as the one that is supposed to touch the battery, while the red wire is supposed to remain in some other part of the machine. One day, the black wire and the red wire both end up touching the battery at the same time. There is a short circuit. Did the black wire cause the short circuit?\nOptions:\n- Yes\n- No", "target": "No"}

{"input": "How would a typical person answer each of the following questions about causation?\nLong ago, when John was only 17 years old, he got a job working for a large manufacturing company. He started out working on an assembly line for minimum wage, but after a few years at the company, he was given a choice between two line manager positions. He could stay in the woodwork division, which is where he was currently working. Or he could move to the plastics division. John was unsure what to do because he liked working in the woodwork division, but he also thought it might be worth trying something different. He finally decided to switch to the plastics division and try something new. For the last 30 years, John has worked as a production line supervisor in the plastics division. After the first year there, the plastics division was moved to a different building with more space. Unfortunately, through the many years he worked there, John was exposed to asbestos, a highly carcinogenic substance. Most of the plastics division was quite safe, but the small part in which John worked was exposed to asbestos fibers. And now, although John has never smoked a cigarette in his life and otherwise lives a healthy lifestyle, he has a highly progressed and incurable case of lung cancer at the age of 50. John had seen three cancer specialists, all of whom confirmed the worst: that, except for pain, John's cancer was untreatable and he was absolutely certain to die from it very soon (the doctors estimated no more than 2 months). Yesterday, while John was in the hospital for a routine medical appointment, a new nurse accidentally administered the wrong medication to him. John was allergic to the drug and he immediately went into shock and experienced cardiac arrest (a heart attack). Doctors attempted to resuscitate him but he died minutes after the medication was administered. Did John's job cause his premature death?\nOptions:\n- Yes\n- No", "target": "No"}

{"input": "How would a typical person answer each of the following questions about causation?\nMr. Wallace is highly influential in the organized crime scene. Although he commands the respect of many, there are also a number of people who stand to benefit from his death. Today, he was having lunch with one of his associates, Mr. Vincent. At one point during their meeting, Mr. Wallace left the table to go to the toilet. While he was gone, Mr. Vincent managed to slip a lethal dose of poison into his martini. The poison is known to take one hour (give or take 10 minutes, depending on the victim's body weight) to kill and would go unnoticed for the first half hour after consumption. When Mr. Wallace returned to the table, he finished his lunch and then drank the rest of his martini. The two men concluded their meeting a few minutes later. Mr. Wallace paid the bill and they both left the restaurant going in different directions. Mr. Wallace had another important business meeting about 15 minutes away in a remote part of the countryside. On an isolated stretch of road, he noticed that he was suddenly being followed by a van that had pulled out from the roadside. The van accelerated and began hitting his car from behind. Mr. Wallace recognized that the driver was Mr. Bruce, an associate of one of Mr. Wallace's rivals. He tried to evade the van but there was no time. The van relentlessly hit his car and pushed it off the side where it fell into a ravine and exploded. The remains of Mr. Wallace's body were discovered later that day. The chief coroner's report later revealed that Mr. Wallace had received fatal burns in the car explosion. The report also indicated, however, that a lethal dose of poison was found in Mr. Wallace's blood. Did the crime life cause Mr. Wallace's death?\nOptions:\n- Yes\n- No", "target": "No"}
</details>

<details>
<summary>Date Understanding</summary>

{"input": "Today is Christmas Eve of 1937. What is the date tomorrow in MM/DD/YYYY?\nOptions:\n(A) 12/11/1937\n(B) 12/25/1937\n(C) 01/04/1938\n(D) 12/04/1937\n(E) 12/25/2006\n(F) 07/25/1937", "target": "(B)"}

{"input": "In the UK, people usually put the day before the month when formatting the date. Therefore, today is 02/01/1987 to them. What is the date a month ago in MM/DD/YYYY?\nOptions:\n(A) 12/02/1986\n(B) 12/01/1986\n(C) 03/02/1986\n(D) 12/02/2032\n(E) 12/02/2062\n(F) 02/06/1987", "target": "(A)"}

{"input": "Today's meeting is rescheduled to 11 am tomorrow, 10/16/1924. What is the date one week from today in MM/DD/YYYY?\nOptions:\n(A) 10/22/1944\n(B) 10/22/1924\n(C) 10/07/1924\n(D) 10/21/1924\n(E) 08/22/1925\n(F) 11/21/1924", "target": "(B)"}
</details>

## Implementation

Below are [configurations](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/bbh) from [EleutherAI's Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness).


<details>
<summary>Zeroshot - Boolean Expressions</summary>

```yaml
"dataset_name": "boolean_expressions"
"description": "Evaluate the result of a random Boolean expression.\n\n"
"doc_to_text": "Q: {{input}}\nA:"
"include": "_zeroshot_template_yaml"
"task": "bbh_zeroshot_boolean_expressions"

filter_list:
  - name: "strict-match"
    filter:
      - function: "take_first"
  - name: "flexible-extract"
    filter:
      - function: "regex"
        group_select: 0
        regex_pattern: "\\b(True|False)\\b"
      - function: "take_first"
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/bbh/zeroshot/boolean_expressions.yaml
</details>

<details>
<summary>n-shot - Boolean Expressions</summary>

```yaml
dataset_name: boolean_expressions
description: 'Evaluate the result of a random Boolean expression.


  '
doc_to_text: 'Q: {{input}}

  A:'
fewshot_config:
  sampler: first_n
  samples:
  - input: not ( ( not not True ) ) is
    target: 'False'
  - input: True and False and not True and True is
    target: 'False'
  - input: not not ( not ( False ) ) is
    target: 'True'
include: _fewshot_template_yaml
task: bbh_fewshot_boolean_expressions
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/bbh/fewshot/boolean_expressions.yaml
</details>

<details>
<summary>CoT Zeroshot - Boolean Expressions</summary>

```yaml
"dataset_name": "boolean_expressions"
"description": "Evaluate the result of a random Boolean expression.\n\n"
"doc_to_text": "Q: {{input}}\nA: Let's think step by step."
"include": "_cot_zeroshot_template_yaml"
"task": "bbh_cot_zeroshot_boolean_expressions"

filter_list:
  - name: "flexible-extract"
    filter:
      - function: "regex"
        group_select: -1
        regex_pattern: "\\b(True|False)\\b"
      - function: "take_first"
  - name: "strict-match"
    filter:
      - function: "regex"
        regex_pattern: "((?<=The answer is )(.*)(?=.)|(?<=the answer is )(.*)(?=.)|(?<=The answer: )(.*)(?=.)|(?<=The final answer: )(.*)(?=.))"
      - function: "take_first"
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/bbh/cot_zeroshot/boolean_expressions.yaml
</details>

<details>
<summary>CoT n-shot - Boolean Expressions</summary>

```yaml
dataset_name: "boolean_expressions"
description: "Evaluate the result of a random Boolean expression.\n\n"
doc_to_text: "Q: {{input}}\nA: Let's think step by step.\n"
include: "_cot_fewshot_template_yaml"
task: "bbh_cot_fewshot_boolean_expressions"
fewshot_config:
  sampler: first_n
  samples: [
    {
      "input": "not ( ( not not True ) ) is",
      "target": "Remember that (i) expressions inside brackets are always evaluated first and that (ii) the order of operations from highest priority to lowest priority is \"not\", \"and\", \"or\", respectively.\nWe first simplify this expression \"Z\" as follows: \"Z = not ( ( not not True ) ) = not ( ( A ) )\" where \"A = not not True\".\nLet's evaluate A: A = not not True = not (not True) = not False = True.\nPlugging in A, we get: Z = not ( ( A ) ) = not ( ( True ) ) = not True = False. So the answer is False."
    },
    {
      "input": "True and False and not True and True is",
      "target": "Remember that (i) expressions inside brackets are always evaluated first and that (ii) the order of operations from highest priority to lowest priority is \"not\", \"and\", \"or\", respectively.\nWe first simplify this expression \"Z\" as follows: \"Z = True and False and not True and True = A and B\" where \"A = True and False\" and \"B = not True and True\".\nLet's evaluate A: A = True and False = False.\nLet's evaluate B: B = not True and True = not (True and True) = not (True) = False.\nPlugging in A and B, we get: Z = A and B = False and False = False. So the answer is False."
    },
    {
      "input": "not not ( not ( False ) ) is",
      "target": "Remember that (i) expressions inside brackets are always evaluated first and that (ii) the order of operations from highest priority to lowest priority is \"not\", \"and\", \"or\", respectively.\nWe first simplify this expression \"Z\" as follows: \"Z = not not ( not ( False ) ) = not not ( A )\" where \"A = not ( False )\".\nLet's evaluate A: A = not ( False ) = not False = True.\nPlugging in A, we get: Z = not not ( A ) = not not (True) = not not False = True. So the answer is True."
    }
  ]
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/bbh/cot_fewshot/boolean_expressions.yaml
</details>


## Citation

Original **BIG Bench** Paper: [Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models](https://arxiv.org/abs/2206.04615)

```
@article{srivastava2022beyond,
  title={Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models},
  author={Srivastava, Aarohi and Rastogi, Abhinav and Rao, Abhishek and Shoeb, Abu Awal Md and Abid, Abubakar and Fisch, Adam and Brown, Adam R and Santoro, Adam and Gupta, Aditya and Garriga-Alonso, Adri{\`a} and others},
  journal={arXiv preprint arXiv:2206.04615},
  year={2022}
}
```

**BIG-Bench Hard** Paper: [Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them](https://arxiv.org/abs/2210.09261)

```
@article{suzgun2022challenging,
  title={Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them},
  author={Suzgun, Mirac and Scales, Nathan and Sch{\"a}rli, Nathanael and Gehrmann, Sebastian and Tay, Yi and Chung, Hyung Won and Chowdhery, Aakanksha and Le, Quoc V and Chi, Ed H and Zhou, Denny and and Wei, Jason},
  journal={arXiv preprint arXiv:2210.09261},
  year={2022}
}
```