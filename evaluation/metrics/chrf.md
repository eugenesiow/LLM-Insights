# ChrF and ChrF++

> **ChrF**, which stands for Character n-gram F-score, is a metric for automatic evaluation of machine translation output. It measures the F-score for character n-gram matches. **ChrF++** extends to word n-grams.

## ChrF

$$
\text{ChrF}_\beta = (1 + \beta^2) \cdot \frac{\text{ChrP} \cdot \text{ChrR}}{\beta^2 \cdot \text{ChrP} + \text{ChrR}}
$$

where $ChrP$ and $ChrR$ stand for character n-gram precision and recall arithmetically averaged over all n-grams:

- $ChrP$, percentage of n-grams in the hypothesis which have a counterpart in the reference;
- $ChrR$, percentage of character n-grams in the reference which are also present in the hypothesis.
- $β$ is a parameter which assigns $β$ times more importance to recall than to precision – if β = 1, they have the same importance.

## ChrF++

$WordF$ is calculated on word n-grams while $ChrF$ is calculated on character n-grams. 

$$
\text{WordF}_\beta = (1 + \beta^2) \cdot \frac{\text{WordP} \cdot \text{WordR}}{\beta^2 \cdot \text{WordP} + \text{WordR}}
$$

$ChrF++$ score is obtained when the word n-grams are added to the character n-grams and averaged together. 

## Citations

```bibtexP
@inproceedings{popovic-2015-chrf,
    title = "chr{F}: character n-gram {F}-score for automatic {MT} evaluation",
    author = "Popovi{\'c}, Maja",
    booktitle = "Proceedings of the Tenth Workshop on Statistical Machine Translation",
    month = sep,
    year = "2015",
    address = "Lisbon, Portugal",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W15-3049",
    doi = "10.18653/v1/W15-3049",
    pages = "392--395",
}
```

```bibtex
@inproceedings{popovic-2017-chrf,
    title = "chr{F}++: words helping character n-grams",
    author = "Popovi{\'c}, Maja",
    booktitle = "Proceedings of the Second Conference on Machine Translation",
    month = sep,
    year = "2017",
    address = "Copenhagen, Denmark",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W17-4770",
    doi = "10.18653/v1/W17-4770",
    pages = "612--618",
}
```