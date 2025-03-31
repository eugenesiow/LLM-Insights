# MRCR

MRCR (Multi-Round Coreference Resolution) is a task for long-context evaluation within Google's internal suite of benchmarks. It was introduced in the [Gemini 1.5](https://arxiv.org/abs/2403.05530) paper and expanded on in the [Michelangelo: Long Context Evaluations Beyond Haystacks via Latent Structure Queries](https://arxiv.org/abs/2409.12640v2) paper by Google (Deepmind). Gemini 2.0 and Gemini 2.5 (128K and 1M context lengths) also benchmarked on MRCR.

In the benchmark, the model sees a long conversation between a user and a model, in which the user requests writing (e.g. poems, riddles, essays) on different topics proceeded by the model responses. In each conversation, two user requests containing topics and writing formats distinct from the rest of the conversation are randomly placed in the context. Given the conversation, the model must reproduce the model's output (the needle) resulting from one of the two requests (the key). Either the formats, the topics, or both, overlap in order to create a single key that is adversarially similar to the query key. For instance, the request `Reproduce the poem about penguins.` requires the model to distinguish the poem about penguins from the poem about flamingos, and `Reproduce the first poem about penguins.` requires the model to reason about ordering. MRCR is scored via a string-similarity measure between the model output and the correct response ([SequenceMatcher ratio](https://docs.python.org/3/library/difflib.html)).

The Google authors feel that MRCR is harder than needle-in-a-haystack benchmarks (test of the model's recall ability) as it requires stronger reasoning and disambiguation skills.

Gemini 1.5 benchmarked on a MRCR test with 2000 samples.

## Links

* Abstract: [Gemini 1.5](https://arxiv.org/abs/2403.05530), [Michelangelo](https://arxiv.org/abs/2409.12640v2)
* License: Unknown

## Example Questions

Below is an example of the prompt format from the Gemini 1.5 paper.

<details>
<summary>Prompt Format</summary>

```
Here are some examples of conversations succeeded by a follow-up question answered
correctly:
======== EXAMPLE 1 ========
User: {user_query11}
Model: {model_output11}
User: {user_query12}
Model: {model_output12}
User: Add the sentence {random_string} to the {key1}.
Model: {random_string} {correct_model_output1}
======== EXAMPLE 2 ========
User: {user_query21}
Model: {model_output21}
User: {user_query22}
Model: {model_output22}
User: Add the sentence {random_string} to the {key2}.
Model: {random_string} {correct_model_output2}
======== EXAMPLE 3 ========
User: ...
Model: ...
...
User: {user_query31}
Model: {model_output31}
...
User: ...
Model: ...
...
User: {user_query32}
Model: {model_output32}
...
User: ...
Model: ...
User: Add the sentence {random_string} to the {key3}.
Model:
```
</details>

<details>
<summary>MRCR Task Example: Complexity 2</summary>

```
Here are some examples of conversations...
======== Relevant Operation ========
User: Write a poem about penguins.
Model: Ode to Penguins...

======== Irrelevant Operations ========
User: Write an essay about complexity theory.
Model: Complexity theory is a challenging subject...
:
User: Write an email about basketball.
Model: Hello! Hope this email finds you well. Basketball is...

======== Relevant Operation ========
User: Write a poem about penguins.
Model: O Fowl of the Frozen Seas! Warm and cuddly...

======== Irrelevant Operations ========
User: Write a riddle about ducks.
Model: What waddles on two feet and quacks?...
:
User: Write a play about Star Wars.
Model: [Enter stage right.] Narrator: Long, long ago...

======== View Operation ========
User: Add the string "AKJSs89sal" to the 2nd poem about penguins.
Model: 
```
</details>

## Citation

```bibtex
@misc{geminiteam2024gemini15unlockingmultimodal,
      title={Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context}, 
      author={Google Team},
      year={2024},
      eprint={2403.05530},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2403.05530}, 
}
```

```bibtex
@misc{vodrahalli2024michelangelolongcontextevaluations,
      title={Michelangelo: Long Context Evaluations Beyond Haystacks via Latent Structure Queries}, 
      author={Kiran Vodrahalli and Santiago Ontanon and Nilesh Tripuraneni and Kelvin Xu and Sanil Jain and Rakesh Shivanna and Jeffrey Hui and Nishanth Dikkala and Mehran Kazemi and Bahare Fatemi and Rohan Anil and Ethan Dyer and Siamak Shakeri and Roopali Vij and Harsh Mehta and Vinay Ramasesh and Quoc Le and Ed Chi and Yifeng Lu and Orhan Firat and Angeliki Lazaridou and Jean-Baptiste Lespiau and Nithya Attaluri and Kate Olszewska},
      year={2024},
      eprint={2409.12640},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2409.12640}, 
}
```