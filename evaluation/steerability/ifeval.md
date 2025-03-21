# IFEval

IFEval stands for [Instruction-Following Evaluation](https://arxiv.org/abs/2311.07911) for Large Language Models, developed by Zhou et al. from Google and Yale University and published in Nov 2023. IFEval tests the model's ability to follow explicit formatting instructions: Instruction following, Formatting, Generation. It focuses on a set of "verifiable instructions" such as "write in more than 400 words" and "mention the keyword of AI at least 3 times", which makes it a straightforward and easy-to-reproduce evaluation benchmark. It consists of [25 types of verifiable instructions](#types-of-instructions), around 500 prompts, with each prompt containing one or more verifiable instructions (total 541 samples).

## Links

* Abstract: https://arxiv.org/abs/2311.07911
* Homepage: https://github.com/google-research/google-research/tree/master/instruction_following_eval
* Dataset: https://huggingface.co/datasets/google/IFEval
* License: [Apache 2.0](https://huggingface.co/datasets/google/IFEval/blob/main/README.md)

## Types of Instructions

| #  | Instruction Group      | Instruction                           | Description  |
|----|-----------------------|--------------------------------------|--------------|
| 1  | Keywords              | Include Keywords                     | Include keywords {keyword1}, {keyword2} in your response. |
| 2  | Keywords              | Keyword Frequency                    | In your response, the word word should appear {N} times. |
| 3  | Keywords              | Forbidden Words                      | Do not include keywords {forbidden words} in the response. |
| 4  | Keywords              | Letter Frequency                     | In your response, the letter {letter} should appear {N} times. |
| 5  | Language              | Response Language                    | Your ENTIRE response should be in {language}, no other language is allowed. |
| 6  | Length Constraints    | Number Paragraphs                    | Your response should contain {N} paragraphs. You separate paragraphs using the markdown divider: * * *. |
| 7  | Length Constraints    | Number Words                         | Answer with at least / around / at most {N} words. |
| 8  | Length Constraints    | Number Sentences                     | Answer with at least / around / at most {N} sentences. |
| 9  | Length Constraints    | Number Paragraphs + First Word in i-th Paragraph | There should be {N} paragraphs. Paragraphs and only paragraphs are separated with each other by two line breaks. The {i}-th paragraph must start with word {first word}. |
| 10 | Detectable Content    | Postscript                           | At the end of your response, please explicitly add a postscript starting with {postscript marker}. |
| 11 | Detectable Content    | Number Placeholder                   | The response must contain at least {N} placeholders represented by square brackets, such as [address]. |
| 12 | Detectable Format     | Number Bullets                       | Your answer must contain exactly {N} bullet points. Use the markdown bullet points such as: * This is a point. |
| 13 | Detectable Format     | Title                                | Your answer must contain a title, wrapped in double angular brackets, such as <<poem of joy>>. |
| 14 | Detectable Format     | Choose From                          | Answer with one of the following options: {options}. |
| 15 | Detectable Format     | Minimum Number Highlighted Section   | Highlight at least {N} sections in your answer with markdown, i.e. *highlighted section*. |
| 16 | Detectable Format     | Multiple Sections                    | Your response must have {N} sections. Mark the beginning of each section with {section splitter} X. |
| 17 | Detectable Format     | JSON Format                          | Entire output should be wrapped in JSON format. |
| 18 | Combination           | Repeat Prompt                        | First, repeat the request without change, then give your answer (do not say anything before repeating the request; the request you need to repeat does not include this sentence). |
| 19 | Combination           | Two Responses                        | Give two different responses. Responses and only responses should be separated by 6 asterisk symbols: ******. |
| 20 | Change Cases          | All Uppercase                        | Your entire response should be in English, capital letters only. |
| 21 | Change Cases          | All Lowercase                        | Your entire response should be in English, and in all lowercase letters. No capital letters are allowed. |
| 22 | Change Cases          | Frequency of All-capital Words       | In your response, words with all capital letters should appear at least / around / at most {N} times. |
| 23 | Start with / End with | End Checker                          | Finish your response with this exact phrase {end phrase}. No other words should follow this phrase. |
| 24 | Start with / End with | Quotation                            | Wrap your entire response with double quotation marks. |
| 25 | Punctuation           | No Commas                            | In your entire response, refrain from the use of any commas. |

## Example Questions

Below are 3 example questions. Each example has a prompt and a set of verifiable instructions which are used as rules to verify the output/generated text formatting.

<details>
<summary>Prompt 1</summary>

Prompt: Write a 300+ word summary of the wikipedia page "https://en.wikipedia.org/wiki/Raymond_III,_Count_of_Tripoli". Do not use any commas and highlight at least 3 sections that has titles in markdown format, for example *highlighted section part 1*, *highlighted section part 2*, *highlighted section part 3*.

Verifiable Instructions: [ "punctuation:no_comma", "detectable_format:number_highlighted_sections", "length_constraints:number_words" ]
</details>

<details>
<summary>Prompt 2</summary>

Prompt: I am planning a trip to Japan, and I would like thee to write an itinerary for my journey in a Shakespearean style. You are not allowed to use any commas in your response.

Verifiable Instructions: [ "punctuation:no_comma" ]
</details>

<details>
<summary>Prompt 3</summary>

Prompt: Write a resume for a fresh high school graduate who is seeking their first job. Make sure to include at least 12 placeholder represented by square brackets, such as [address], [name].

Verifiable Instructions: [ "detectable_content:number_placeholders" ]
</details>

## Implementation

Below are [configurations](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/ifeval) from [EleutherAI's Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness).

<details>
<summary>Zeroshot</summary>

```yaml
task: ifeval
dataset_path: google/IFEval
dataset_name: null
output_type: generate_until
test_split: train
num_fewshot: 0
doc_to_text: prompt
doc_to_target: 0
generation_kwargs:
  until: []
  do_sample: false
  temperature: 0.0
  max_gen_toks: 1280
process_results: !function utils.process_results
metric_list:
  - metric: prompt_level_strict_acc
    aggregation: mean
    higher_is_better: true
  - metric: inst_level_strict_acc
    aggregation: !function utils.agg_inst_level_acc
    higher_is_better: true
  - metric: prompt_level_loose_acc
    aggregation: mean
    higher_is_better: true
  - metric: inst_level_loose_acc
    aggregation: !function utils.agg_inst_level_acc
    higher_is_better: true
metadata:
  version: 4.0
```

Source: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/ifeval/ifeval.yaml
</details>

## Citation

```
@article{zhou2023instructionfollowing,
  title={Instruction-Following Evaluation for Large Language Models},
  author={Jeffrey Zhou and Tianjian Lu and Swaroop Mishra and Siddhartha Brahma and Sujoy Basu and Yi Luan and Denny Zhou and Le Hou},
  journal={arXiv preprint arXiv:2311.07911},
  year={2023},
}
```