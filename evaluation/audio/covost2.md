# CoVoST2

CoVoST2 or the Common Voice Speech-to-Text 2 translation corpus, is a large-scale multilingual speech translation corpus (dataset) covering translations from 21 languages into English
and from English into 15 languages. The dataset is created using the open-source Common Voice database of crowdsourced voice recordings. There are 2,900 hours of speech represented in the corpus. The dataset was published by Wang et al. from Facebook AI in July 2020 and follows on from the original CoVoST, also published by Wang et al. but in Feb 2020 and with just 11 languages into English. The dataset can be used for Speech-to-text translation (ST) benchmarking. The model is presented with an audio file in one language and asked to transcribe the audio file to written text in another language. The most common evaluation metric is the BLEU score.

## Links

* Abstract: https://arxiv.org/abs/2007.10310
* Code: (Repository) https://github.com/facebookresearch/covost/, (Example) https://github.com/facebookresearch/fairseq/blob/main/examples/speech_to_text/docs/covost_example.md
* Dataset: https://huggingface.co/datasets/facebook/covost2
* License: [CC-BY-NC-4.0](https://github.com/facebookresearch/covost/blob/main/LICENSE)

## Languages

The dataset contains the audio, transcriptions, and translations in the following languages, French, German, Dutch, Russian, Spanish, Italian, Turkish, Persian, Swedish, Mongolian, Chinese, Welsh, Catalan, Slovenian, Estonian, Indonesian, Arabic, Tamil, Portuguese, Latvian, and Japanese. 

### Data Splits

| config   | train  | validation | test  |
|----------|--------|------------|-------|
| en_de    | 289430 | 15531      | 15531 |
| en_tr    | 289430 | 15531      | 15531 |
| en_fa    | 289430 | 15531      | 15531 |
| en_sv-SE | 289430 | 15531      | 15531 |
| en_mn    | 289430 | 15531      | 15531 |
| en_zh-CN | 289430 | 15531      | 15531 |
| en_cy    | 289430 | 15531      | 15531 |
| en_ca    | 289430 | 15531      | 15531 |
| en_sl    | 289430 | 15531      | 15531 |
| en_et    | 289430 | 15531      | 15531 |
| en_id    | 289430 | 15531      | 15531 |
| en_ar    | 289430 | 15531      | 15531 |
| en_ta    | 289430 | 15531      | 15531 |
| en_lv    | 289430 | 15531      | 15531 |
| en_ja    | 289430 | 15531      | 15531 |
| fr_en    | 207374 | 14760      | 14760 |
| de_en    | 127834 | 13511      | 13511 |
| es_en    | 79015  | 13221      | 13221 |
| ca_en    | 95854  | 12730      | 12730 |
| it_en    | 31698  | 8940       | 8951  |
| ru_en    | 12112  | 6110       | 6300  |
| zh-CN_en | 7085   | 4843       | 4898  |
| pt_en    | 9158   | 3318       | 4023  |
| fa_en    | 53949  | 3445       | 3445  |
| et_en    | 1782   | 1576       | 1571  |
| mn_en    | 2067   | 1761       | 1759  |
| nl_en    | 7108   | 1699       | 1699  |
| tr_en    | 3966   | 1624       | 1629  |
| ar_en    | 2283   | 1758       | 1695  |
| sv-SE_en | 2160   | 1349       | 1595  |
| lv_en    | 2337   | 1125       | 1629  |
| sl_en    | 1843   | 509        | 360   |
| ta_en    | 1358   | 384        | 786   |
| ja_en    | 1119   | 635        | 684   |
| id_en    | 1243   | 792        | 844   |
| cy_en    | 1241   | 690        | 690   |

## Example Instances

A typical data point comprises the path to the audio file, usually called `file`, its transcription, called `sentence`, and the translation in target language called `translation`.

```
{'client_id': 'd277a1f3904ae00b09b73122b87674e7c2c78e08120721f37b5577013ead08d1ea0c053ca5b5c2fb948df2c81f27179aef2c741057a17249205d251a8fe0e658',
 'file': '/home/suraj/projects/fairseq_s2t/covst/dataset/en/clips/common_voice_en_18540003.mp3',
 'audio': {'path': '/home/suraj/projects/fairseq_s2t/covst/dataset/en/clips/common_voice_en_18540003.mp3',
		   'array': array([-0.00048828, -0.00018311, -0.00137329, ...,  0.00079346, 0.00091553,  0.00085449], dtype=float32),
		   'sampling_rate': 48000},
 'id': 'common_voice_en_18540003',
 'sentence': 'When water is scarce, avoid wasting it.',
 'translation': 'Wenn Wasser knapp ist, verschwenden Sie es nicht.'}
```

### Data Fields

- file: A path to the downloaded audio file in .mp3 format.

- audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the `"audio"` column, *i.e.* `dataset[0]["audio"]` should **always** be preferred over `dataset["audio"][0]`.

- sentence: The transcription of the audio file in source language.

- translation: The transcription of the audio file in the target language. 

- id: unique id of the data sample.

## Citations

```bibtex
@misc{wang2020covost,
    title={CoVoST 2: A Massively Multilingual Speech-to-Text Translation Corpus},
    author={Changhan Wang and Anne Wu and Juan Pino},
    year={2020},
    eprint={2007.10310},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
```

```bibtex
@misc{wang2020covostdiversemultilingualspeechtotext,
      title={CoVoST: A Diverse Multilingual Speech-To-Text Translation Corpus}, 
      author={Changhan Wang and Juan Pino and Anne Wu and Jiatao Gu},
      year={2020},
      eprint={2002.01320},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2002.01320}, 
}
```