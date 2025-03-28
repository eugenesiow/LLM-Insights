# LiveCodeBench

LiveCodeBench is a comprehensive and contamination-free benchmark for code, which continuously collects new problems over time from contests across three competition platforms, namely LeetCode, AtCoder, and CodeForces. It was developed by Jain et al from UC Berkeley, MIT and Cornell and published in Mar 2024 with a revision on 6 June 2024. The benchmark focuses on a broader range of code related capabilities, such as self-repair, code execution, and test output prediction, beyond just code generation. 

Since LiveCodeBench is a continuously updated benchmark, there have been multiple releases since the initial release of 400 problems.

| Release Version | Start Date | End Date   | Number of Problems |
|-----------------|------------|------------|--------------------|
| release_v1      | May 2023   | Mar 2024   | 400                |
| release_v2      | May 2023   | May 2024   | 511                |
| release_v3      | May 2023   | Jul 2024   | 612                |
| release_v4      | May 2023   | Sep 2024   | 713                |
| release_v5      | May 2023   | Jan 2025   | 880                |

## Links

* Abstract: https://arxiv.org/abs/2403.07974
* Homepage: https://livecodebench.github.io/
* Code: https://github.com/LiveCodeBench/LiveCodeBench
* Dataset: https://huggingface.co/datasets/livecodebench/code_generation, https://huggingface.co/datasets/livecodebench/execution-v2
* License: [CC](https://huggingface.co/datasets/livecodebench/execution-v2/blob/main/README.md)

## Example Questions

Below are example prompts and questions.

<details>
<summary>Code Execution</summary>

Prompt:
```
You are given a Python function and an assertion containing an input to the function. Complete the assertion with a literal (no unsimplified expressions, no function calls) containing the output when executing the provided code on the given input, even if the function is incorrect or incomplete. Do NOT output any extra information. Provide the full assertion with the correct output in [ANSWER] and [/ANSWER] tags, following the examples.

[PYTHON]
def repeatNumber(number : int) -> int:
    return number
assert repeatNumber(number = 17) == ??
[/PYTHON]
[ANSWER]
assert repeatNumber(number = 17) == 17
[/ANSWER]

[PYTHON]
def addCharacterA(string : str) -> str:
    return string + "a"
assert addCharacterA(string = "x9j") == ??
[/PYTHON]
[ANSWER]
assert addCharacterA(string = "x9j") == "x9ja"
[/ANSWER]

[PYTHON]
def distinctDifferenceArray(a: List[int]) -> List[int]:
  return [len(set(a[:i+1]))-len(set(a[i+1:]))for i in range(len(a))]
assert distinctDifferenceArray(a = [1, 2, 3, 4, 5]) == ??
[/PYTHON]
[ANSWER]
```

Expected Output:
```python
[-3, -1, 1, 3, 5]
```

</details>

## Citation

```
@misc{jain2024livecodebenchholisticcontaminationfree,
      title={LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code}, 
      author={Naman Jain and King Han and Alex Gu and Wen-Ding Li and Fanjia Yan and Tianjun Zhang and Sida Wang and Armando Solar-Lezama and Koushik Sen and Ion Stoica},
      year={2024},
      eprint={2403.07974},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/2403.07974}, 
}
```