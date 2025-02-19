# Synthetic Data


## Fineweb-edu

[Fineweb](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) used created [a set](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu-llama3-annotations) of 450,000 samples (from the web) with scores from 0 to 5 of educational value, judged by Llama3, to train a [classifier](https://huggingface.co/HuggingFaceFW/fineweb-edu-classifier) to produce the [fineweb-edu corpus](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu).

The prompt used with Llama3 to get the educational value score is shown below:

```
Below is an extract from a web page. Evaluate whether the page has a high educational value and could be useful in an educational setting for teaching from primary school to grade school levels using the additive 5-point scoring system described below. Points are accumulated based on the satisfaction of each criterion:

- Add 1 point if the extract provides some basic information relevant to educational topics, even if it includes some irrelevant or non-academic content like advertisements and promotional material.
- Add another point if the extract addresses certain elements pertinent to education but does not align closely with educational standards. It might mix educational content with non-educational material, offering a superficial overview of potentially useful topics, or presenting information in a disorganized manner and incoherent writing style.
- Award a third point if the extract is appropriate for educational use and introduces key concepts relevant to school curricula. It is coherent though it may not be comprehensive or could include some extraneous information. It may resemble an introductory section of a textbook or a basic tutorial that is suitable for learning but has notable limitations like treating concepts that are too complex for grade school students. 
- Grant a fourth point if the extract highly relevant and beneficial for educational purposes for a level not higher than grade school, exhibiting a clear and consistent writing style. It could be similar to a chapter from a textbook or a tutorial, offering substantial educational content, including exercises and solutions, with minimal irrelevant information, and the concepts aren't too advanced for grade school students. The content is coherent, focused, and valuable for structured learning.
- Bestow a fifth point if the extract is outstanding in its educational value, perfectly suited for teaching either at primary school or grade school. It follows detailed reasoning, the writing style is easy to follow and offers profound and thorough insights into the subject matter, devoid of any non-educational or complex content.

The extract:
<EXAMPLE>.

After examining the extract: 
- Briefly justify your total score, up to 100 words.
- Conclude with the score using the format: "Educational score:  <total points>"
```