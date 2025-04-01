# PopQA 

PopQA is a large-scale open-domain question answering (QA) dataset, consisting of 14k entity-centric QA pairs. Each question is created by converting a knowledge tuple retrieved from Wikidata using a template. Each question comes with the original `subject_entitiey`, `object_entity`and `relationship_type` annotation, as well as Wikipedia monthly page views. The dataset contains samples in English only.

## Links

* Abstract: https://arxiv.org/abs/2212.10511
* Homepage: https://github.com/AlexTMallen/adaptive-retrieval
* Dataset: https://huggingface.co/datasets/akariasai/PopQA
* License: [MIT](https://github.com/AlexTMallen/adaptive-retrieval?tab=MIT-1-ov-file)

## Data Fields

- `id`: question id
- `subj`: subject entity name
- `prop`: relationship type
- `obj`: object entity name
- `subj_id`: Wikidata ID of the subject entity
- `prop_id`: Wikidata relationship type ID
- `obj_id`: Wikidata ID of the object entity
- `s_aliases`: aliases of the subject entity
- `o_aliases`: aliases of the object entity
- `s_uri`: Wikidata URI of the subject entity   
- `o_uri`: Wikidata URI of the object entity
- `s_wiki_title`: Wikipedia page title of the subject entity
- `o_wiki_title`: Wikipedia page title of the object entity
- `s_pop`: Wikipedia monthly pageview of the subject entity
- `o_pop`: Wikipedia monthly pageview of the object entity
- `question`: PopQA question
- `possible_answers`: a list of the gold answers.

## Example Questions

<details>
<summary>Example Sample</summary>

```json
{
    "id": 4222362,
    "subj": "George Rankin",
    "prop": "occupation",
    "obj": "politician",
    "subj_id": 1850297,
    "prop_id": 22,
    "obj_id": 2834605,
    "s_aliases": [
        "George James Rankin"
    ],
    "o_aliases": [
        "political leader",
        "political figure",
        "polit.",
        "pol"
    ],
    "s_uri": "http://www.wikidata.org/entity/Q5543720",
    "o_uri": "http://www.wikidata.org/entity/Q82955",
    "s_wiki_title": "George Rankin",
    "o_wiki_title": "Politician",
    "s_pop": 142,
    "o_pop": 25692,
    "question": "What is George Rankin\"s occupation?",
    "possible_answers": [
        "politician",
        "political leader",
        "political figure",
        "polit.",
        "pol"
    ]
}
```
</details>


## Citation

```bibtex
@article{ mallen2023llm_memorization ,
  title={When Not to Trust Language Models: Investigating Effectiveness and Limitations of Parametric and Non-Parametric Memories },
  author={ Mallen, Alex and Asai,Akari and  Zhong, Victor and Das, Rajarshi and Hajishirzi, Hannaneh and Khashabi, Daniel},
  journal={ arXiv preprint },
  year={ 2022 }
}
```
