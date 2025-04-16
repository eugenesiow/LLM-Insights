# SWE-Bench

**SWE-bench** is a benchmark for evaluating large language models on real world software issues collected from GitHub. Given a codebase and an issue, a language model is tasked with generating a patch that resolves the described problem. The original benchmark in the paper [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) was developed by Jimenez el al. from Princeton University and the University of Chicago and published at [ICLR 2024](https://iclr.cc/Conferences/2024) in May 2024. The dataset collects 2,294 Issue-Pull Request pairs from 12 popular Python repositories. Evaluation is performed by unit test verification using post-PR behavior as the reference solution.

> These unit tests fail before the solution code in the PR is added, but pass afterwards, and are therefore called `FAIL_TO_PASS` tests. Each sample also has associated `PASS_TO_PASS` tests, which pass both before and after the PR is merged, and are used to check that existing unrelated functionality in the codebase has not been broken by the PR. A proposed edit is evaluated by running both the `FAIL_TO_PASS` and `PASS_TO_PASS` tests. If the `FAIL_TO_PASS` tests pass, this means the edit solves the issue. If the `PASS_TO_PASS` tests pass, then the edit has not inadvertently broken unrelated sections of the codebase. Both sets of tests are required to pass for the edit to fully resolve the original GitHub issue.

**SWE-bench Verified** is a subset of 500 samples from the SWE-bench test set, which have been human-validated for quality. A human annotation campaign was conducted with 93 professional Python developers to review test samples. The goal was to ensure appropriately scoped unit tests and well-specified issue descriptions. 

1. 1,699 random samples from SWE-bench were manually screened.
2. Issues were categorized by severity (0-3 scale), with 2+ indicating problematic samples. Annotators also assessed difficulty based on estimated fix time. Annotations enable dataset slicing by difficulty, with 196 easy (<15-min fixes) and 45 hard (>1-hour fixes) samples.
3. Samples with severe issues (problematic descriptions or invalid unit tests) were removed. A conservative ensembling approach was used—if any of the three annotators flagged an issue, the sample was discarded.
4. A final set of 500 high-quality samples was selected for SWE-bench Verified.

![SWE-Bench Verified Results on Frontier Models](https://raw.githubusercontent.com/eugenesiow/llm-benchmark-graphs/refs/heads/master/graphs/swe-bench-verified/swe-bench-verified-dark.png#gh-dark-mode-only)
![SWE-Bench Verified Results on Frontier Models](https://raw.githubusercontent.com/eugenesiow/llm-benchmark-graphs/refs/heads/master/graphs/swe-bench-verified/swe-bench-verified-light.png#gh-light-mode-only)

**SWE-bench Lite** is a canonical subset (from the paper's authors) of SWE-bench called SWE-bench Lite that comprises 300 instances from SWE-bench that have been sampled to be more self-contained, with a focus on evaluating functional bug fixes. The benchmark can be run much faster than the original. SWE-bench Lite covers 11 of the original 12 repositories in SWE-bench, with a similar diversity and distribution of repositories as the original. 

The general criteria used to select SWE-bench Lite instances is as follows:

1. Remove instances with images, external hyperlinks, references to specific commit SHAs and references to other pull requests or issues.
2. Remove instances that have fewer than 40 words in the problem statement.
3. Remove instances that edit more than 1 file.
4. Remove instances where the gold patch has more than 3 edit hunks (see patch).
5. Remove instances that create or remove files.
6. Remove instances that contain tests with error message checks.
7. Sampled 300 test instances and 23 development instances from the remaining instances.

**SWE-bench Multimodal** is a dataset for evaluating AI systems on visual software engineering tasks. It contains 619 task instances from 17 popular JavaScript repositories, each featuring images crucial to problem-solving. The dataset covers a range of challenges including UI glitches, map rendering problems, or data visualization bugs. SWE-bench Multimodal challenges AI systems to tackle the diverse, multimodal nature of modern software development.

## Links

### SWE-Bench

* Abstract: https://arxiv.org/abs/2310.06770
* Homepage: https://www.swebench.com/
* Dataset: https://huggingface.co/datasets/princeton-nlp/SWE-bench
* License: [MIT](https://github.com/swe-bench/SWE-bench?tab=MIT-1-ov-file#readme)

### SWE-Bench (Verified)

* Homepage: https://openai.com/index/introducing-swe-bench-verified/
* Annotation Rubric: https://cdn.openai.com/introducing-swe-bench-verified/swe-b-annotation-instructions.pdf
* Dataset: https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified

### SWE-Bench Lite

* Homepage: https://www.swebench.com/lite.html
* Code: https://github.com/swe-bench/SWE-bench/tree/main/swebench/collect/make_lite
* Dataset: https://huggingface.co/datasets/princeton-nlp/SWE-bench_Lite

### SWE-Bench Multimodal

* Abstract: https://arxiv.org/abs/2410.03859
* Homepage: https://www.swebench.com/multimodal.html
* Dataset: https://huggingface.co/datasets/princeton-nlp/SWE-bench_Multimodal
* License: [MIT](https://github.com/swe-bench/SWE-bench?tab=MIT-1-ov-file#readme)

## Citation

```
@inproceedings{
    jimenez2024swebench,
    title={{SWE}-bench: Can Language Models Resolve Real-world Github Issues?},
    author={Carlos E Jimenez and John Yang and Alexander Wettig and Shunyu Yao and Kexin Pei and Ofir Press and Karthik R Narasimhan},
    booktitle={The Twelfth International Conference on Learning Representations},
    year={2024},
    url={https://openreview.net/forum?id=VTF8yNQM66}
}
```

```
@inproceedings{
    yang2024swebenchmultimodal,
    title={{SWE}-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?},
    author={John Yang and Carlos E. Jimenez and Alex L. Zhang and Kilian Lieret and Joyce Yang and Xindi Wu and Ori Press and Niklas Muennighoff and Gabriel Synnaeve and Karthik R. Narasimhan and Diyi Yang and Sida I. Wang and Ofir Press},
    booktitle={The Thirteenth International Conference on Learning Representations},
    year={2025},
    url={https://openreview.net/forum?id=riTiq3i21b}
}
```