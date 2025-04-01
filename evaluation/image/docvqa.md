# DocVQA

DocVQA stands for the Document Visual Question Answering dataset. Document images are taken from the [UCSF Industry Documents Library](https://www.industrydocuments.ucsf.edu/). It consists of a mix of printed, typewritten and handwritten content. A wide variety of document types appears in this dataset including letters, memos, notes, reports etc.

DocVQA comprises 50,000 questions framed on 12,767 images. The data is split randomly in an 80−10−10 ratio to train, validation and test splits.
- Train split: 39,463 questions, 10,194 images.
- Validation split: 5,349 questions and 1,286 images.
- Test split has 5,188 questions and 1,287 images.

## Links

* Abstract: https://arxiv.org/abs/2007.00398
* Homepage: https://www.docvqa.org/
* Dataset: (Unofficial by lmms-lab) https://huggingface.co/datasets/lmms-lab/DocVQA, (Official) https://rrc.cvc.uab.es/?ch=17 in RRC portal ("Downloads" tab)
* License: (Official) Unknown, (Unofficial by lmms-lab) [Apache 2.0](https://huggingface.co/datasets/lmms-lab/DocVQA/blob/main/README.md)

## Citations

```bibtex
@InProceedings{mathew2021docvqa,
  author    = {Mathew, Minesh and Karatzas, Dimosthenis and Jawahar, CV},
  title     = {Docvqa: A dataset for vqa on document images},
  booktitle = {Proceedings of the IEEE/CVF winter conference on applications of computer vision},
  year      = {2021},
  pages     = {2200--2209},
}
```