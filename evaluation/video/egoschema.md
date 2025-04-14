# EgoSchema

EgoSchema is a diagnostic benchmark for assessing very long-form video-language understanding capabilities of modern multimodal systems (vision and language systems). The dataset is derived from Ego4D and consists of over 5000 human curated multiple choice question answer pairs, spanning over 250 hours of real video data, covering a very broad range of natural human activity and behavior. For each question, EgoSchema requires the correct answer to be selected between five given options based on a three-minute-long video clip. In terms of temporal certificate sets, a general notion for capturing the intrinsic temporal understanding length associated with a broad range of video understanding tasks and datasets, EgoSchema has intrinsic temporal lengths over 5.7x longer than the second closest dataset (at the time of publication) and 10x to 100x longer than any other video understanding dataset. It was published with the paper [EgoSchema: A Diagnostic Benchmark for Very Long-form Video Language Understanding](https://arxiv.org/abs/2308.09126) by Mangalam et al. from UC Berkeley in Aug 2023.

Note: EgoSchema is intended for a 0-shot evaluation benchmark, hence the entire correct answer file was not be made public.

## Links

* Abstract: https://arxiv.org/abs/2308.09126
* Code: https://github.com/egoschema/EgoSchema
* Dataset: (Kaggle) https://www.kaggle.com/competitions/egoschema-public/overview, (Google Drive) https://drive.google.com/drive/folders/1SS0VVz8rML1e5gWq7D7VtP1oxE2UtmhQ, (Unofficial) https://huggingface.co/datasets/lmms-lab/egoschema
* License: [Ego4D License](https://ego4ddataset.com/ego4d-license/) (Read and accept, available for public and commercial use)

## Example Questions

<details>
<summary>Question 00000</summary>

Question: Taking into account all the actions performed by c, what can you deduce about the primary objective and focus within the video content?

Option: 
1. C is cooking.
2. C is doing laundry.
3. C is cleaning the kitchen.
4. C is cleaning dishes.
5. C is cleaning the bathroom.

Answer: 3

</details>

<details>
<summary>Question 00001</summary>

Question: What was the primary purpose of the cup of water in this video, and how did it contribute to the overall painting process?

Option: 
1. To provide a source of water for the paintbrush.
2. To provide a place to store the paintbrush.
3. To provide a place to dispose of the paintbrush.
4. To provide a place to rest the paintbrush.
5. To clean the paintbrush.

Answer: 4

</details>

## Citations

```bibtex
@misc{mangalam2023egoschemadiagnosticbenchmarklongform,
      title={EgoSchema: A Diagnostic Benchmark for Very Long-form Video Language Understanding}, 
      author={Karttikeya Mangalam and Raiymbek Akshulakov and Jitendra Malik},
      year={2023},
      eprint={2308.09126},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2308.09126}, 
}
```