# AI2D

AI2D is the Allen Institute for Artificial Intelligence Diagrams dataset, from the paper [A Diagram Is Worth A Dozen Images](https://arxiv.org/abs/1603.07396) by Kembhavi et al. published in Mar 2016. It consists a collection of diagrams with crowd-sourced descriptions, which was originally developed to support research on automatic diagram understanding and visual question answering. AI2D has annotations of constituents and relationships for over 5,000 diagrams and 15,000 questions and answers.

The 15,000 questions and answers are multiple-choice questions. These questions are carefully designed to probe different aspects of diagram comprehension, ranging from simple identification of elements to more complex tasks requiring an understanding of the relationships depicted and the ability to reason about the underlying scientific concepts. The multiple-choice format offers a standardized and objective method for assessing the performance of VQA (Visual Question Answering) models on this benchmark, allowing for direct comparison between different AI systems. 

The diagrams themselves were initially collected by scraping them from the web, and the initial set of annotations was created through crowd-sourcing efforts.

More recently it has also been included in other datasets like [The Cauldron](https://huggingface.co/datasets/HuggingFaceM4/the_cauldron) used in training the [Idefics2](https://huggingface.co/blog/idefics2) vision-language model.

## Links

* Abstract: https://arxiv.org/abs/1603.07396
* Dataset: https://huggingface.co/datasets/lmms-lab/ai2d, (Original) https://allenai.org/data/diagrams
* License: Unknown

## Example Questions

<details>
<summary>Example 1</summary>

Diagram: A simple food chain diagram depicting phytoplankton being eaten by fish, which are then eaten by seals, which in turn are eaten by whales.

Question: According to the given food chain, what would happen if the phytoplankton population decreases?

Options:

1. Seal population will become extinct.
2. Fish population would decrease.
3. Whale population would decrease.
4. Penguin population would increase.

Answer: 
2. Fish population would decrease.

Reasoning: This question requires understanding the concept of a food chain and the flow of energy within it. Phytoplankton forms the base of this food chain, and a reduction in its population would directly impact the organisms that feed on it, namely the fish.

</details>

<details>
<summary>Example 2</summary>

Diagram: A diagram illustrating the life cycle of a butterfly, showing four stages labeled A, B, C, and D, typically representing egg, larva, pupa, and adult.

Question: What is the order of the insect's life stages, from youngest to oldest?

Options:

1. B-A-C-D
2. C-A-B-D
3. A-B-C-D
4. B-C-A-D

Answer: 

1. B-A-C-D

Reasoning: This question tests the ability to interpret a sequential process depicted visually and to recall the correct order of stages in a butterfly's life cycle.

</details>

<details>
<summary>Example 3</summary>

Diagram: A diagram showing the different phases of the moon, such as new moon, first quarter, full moon, and last quarter, often represented by varying degrees of illumination of a circle.

Question: Which phase describes the point at which the moon appears nearly invisible in the sky?

Options:

1. Third quarter half moon
2. New moon
3. Full moon
4. First quarter half moon

Answer: 

2. New moon.

Reasoning: This question requires knowledge of the lunar phases and the ability to match the description to the corresponding visual representation in the diagram.

</details>

## Citations

```bibtex
@inproceedings{kembhavi2016diagram,
 title={A diagram is worth a dozen images},
 author={Kembhavi, Aniruddha and Salvato, Mike and Kolve, Eric and Seo, Minjoon and Hajishirzi, Hannaneh and Farhadi, Ali},
 booktitle={European conference on computer vision},
 pages={235--251},
 year={2016},
 organization={Springer}
}
```

```bibtex
@article{Hiippala_2020,
   title={AI2D-RST: a multimodal corpus of 1000 primary school science diagrams},
   volume={55},
   ISSN={1574-0218},
   url={http://dx.doi.org/10.1007/s10579-020-09517-1},
   DOI={10.1007/s10579-020-09517-1},
   number={3},
   journal={Language Resources and Evaluation},
   publisher={Springer Science and Business Media LLC},
   author={Hiippala, Tuomo and Alikhani, Malihe and Haverinen, Jonas and Kalliokoski, Timo and Logacheva, Evanfiya and Orekhova, Serafina and Tuomainen, Aino and Stone, Matthew and Bateman, John A.},
   year={2020},
   month=dec, pages={661–688} }
```