# ZeroSCROLLS

ZeroSCROLLS is a suite of datasets that require synthesizing information over **long texts**. The benchmark includes ten natural language tasks across multiple domains, including summarization, question answering, aggregated sentiment classification and information reordering.

| Dataset       | Paper                                       | Description                                             |
|--------------|--------------------------------------------|---------------------------------------------------------|
| GovReport    | [Huang et al., 2021](https://arxiv.org/abs/2104.02112) | Summarization of long reports.                         |
| SummScreenFD | [Chen et al., 2021](https://arxiv.org/abs/2104.07091) | Summarization of TV shows episodes scripts.            |
| QMSum        | [Zhong et al., 2021](https://arxiv.org/abs/2104.05938) | Query-based summarization over meeting transcripts.    |
| SQuALITY     | [Wang et al., 2022](https://aclanthology.org/2022.emnlp-main.75/) | Question-focused summarization over stories.           |
| Qasper       | [Dasigi et al., 2021](https://arxiv.org/abs/2105.03011) | Question answering over research papers.               |
| NarrativeQA  | [Kočiský et al., 2018](https://arxiv.org/abs/1712.07040) | Question answering about entire books and movie scripts. |
| QuALITY      | [Pang et al., 2021](https://arxiv.org/abs/2112.08608) | Multiple-choice questions over long articles and stories. |
| MuSiQue      | [Trivedi et al., 2022](https://transacl.org/index.php/tacl/article/view/3639) | Multi-hop question answering over Wikipedia.           |
| SpaceDigest  | [Angelidis et al., 2021](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00366/98621/Extractive-Opinion-Summarization-in-Quantized) | Aggregated sentiment classification over 50 hotel reviews from Space. |
| BookSumSort  | [Kryściński et al., 2021](https://arxiv.org/abs/2105.08209) | Reordering of summaries of parts of novels in BOOKSUM. |

## Links

* Abstract: https://arxiv.org/abs/2305.14196
* Homepage: https://www.zero.scrolls-benchmark.com/
* Dataset: https://huggingface.co/datasets/tau/zero_scrolls, (Original) https://www.zero.scrolls-benchmark.com/tasks
* License: Unknown

## Tasks
ZeroSCROLLS contains the following tasks. Expand for more details of each dataset.

<details>
<summary>GovReport</summary>

GovReport is a summarization dataset of reports addressing various national policy issues published by the 
Congressional Research Service and the U.S. Government Accountability Office, where each document is paired with a hand-written executive summary.
The reports and their summaries are longer than their equivalents in other popular long-document summarization datasets; 
for example, GovReport's documents are approximately 1.5 and 2.5 times longer than the documents in Arxiv and PubMed, respectively.

</details>

<details>
<summary>SummScreenFD</summary>

SummScreenFD is a summarization dataset in the domain of TV shows (e.g. Friends, Game of Thrones).
Given a transcript of a specific episode, the goal is to produce the episode's recap.
The original dataset is divided into two complementary subsets, based on the source of its community contributed transcripts. 
For SCROLLS, we use the ForeverDreaming (FD) subset, as it incorporates 88 different shows, 
making it a more diverse alternative to the TV MegaSite (TMS) subset, which has only 10 shows. 
Community-authored recaps for the ForeverDreaming transcripts were collected from English Wikipedia and TVMaze.

</details>

<details>
<summary>QMSum</summary>

QMSum is a query-based summarization dataset, consisting of 232 meetings transcripts from multiple domains. 
The corpus covers academic group meetings at the International Computer Science Institute and their summaries, industrial product meetings for designing a remote control, 
and committee meetings of the Welsh and Canadian Parliaments, dealing with a variety of public policy issues.
Annotators were tasked with writing queries about the broad contents of the meetings, as well as specific questions about certain topics or decisions, 
while ensuring that the relevant text for answering each query spans at least 200 words or 10 turns.

</details>

<details>
<summary>SQuALITY</summary>

SQuALITY (Wang et al., 2022) is a question-focused summarization dataset, where given a story from Project Gutenberg, 
the task is to produce a summary of the story or aspects of it based on a guiding question.
The questions and summaries are original and crowdsourced; experienced writers were guided to design questions that require reading significant parts of the story to answer correctly.

</details>

<details>
<summary>Qasper</summary>

Qasper is a question answering dataset over NLP papers filtered from the Semantic Scholar Open Research Corpus (S2ORC).
Questions were written by NLP practitioners after reading only the title and abstract of the papers, 
while another set of NLP practitioners annotated the answers given the entire document.
Qasper contains abstractive, extractive, and yes/no questions, as well as unanswerable ones.

</details>

<details>
<summary>NarrativeQA</summary>

NarrativeQA (Kočiský et al., 2021) is an established question answering dataset over entire books from Project Gutenberg and movie scripts from different websites.
Annotators were given summaries of the books and scripts obtained from Wikipedia, and asked to generate question-answer pairs, 
resulting in about 30 questions and answers for each of the 1,567 books and scripts.
They were encouraged to use their own words rather then copying, and avoid asking yes/no questions or ones about the cast.
Each question was then answered by an additional annotator, providing each question with two reference answers (unless both answers are identical).

</details>

<details>
<summary>QuALITY</summary>

QuALITY is a multiple-choice question answering dataset over articles and stories sourced from Project Gutenberg, 
the Open American National Corpus, and more.
Experienced writers wrote questions and distractors, and were incentivized to write answerable, unambiguous questions such that in order to correctly answer them, 
human annotators must read large portions of the given document. 
Reference answers were then calculated using the majority vote between of the annotators and writer's answers.
To measure the difficulty of their questions, Pang et al. conducted a speed validation process, 
where another set of annotators were asked to answer questions given only a short period of time to skim through the document.
As a result, 50% of the questions in QuALITY are labeled as hard, i.e. the majority of the annotators in the speed validation setting chose the wrong answer.

</details>

<details>
<summary>MuSiQue</summary>

MuSiQue is a multi-hop question answering dataset, where the inputs are 20 Wikipedia paragraphs and a question that requires multiple hops between different paragraphs.
In the original dataset, each question also has an unanswerable twin question, where the correct answer is not present in the paragraphs.

</details>

<details>
<summary>SpaceDigest (New)</summary>

SpaceDigest is a new sentiment aggregation task. Given 50 hotel reviews (without their ratings) from the Space dataset (Angelidis et al., 2021), the task is to determine the percentage of positive reviews.

</details>

<details>
<summary>BookSumSort (New)</summary>

BookSumSort is a new task based on the BookSum dataset (Kry ́sci ́nski et al., 2022), which contains summaries of chapters (or parts) of novels, plays, and long poems from various sources. 
Given a shuffled list of chapter summaries, the task is to reorder them according to the original order of summaries in BookSum.

</details>

## Data Fields

Most datasets in the benchmark are in the same input-output format

- `input`: a `string` feature. The input document.
- `output`: this feature is always None, as ZeroSCROLLS contains only test sets.
- `id`: a `string` feature. Unique per input.
- `pid`: a `string` feature, identical to 'id`. Facilitates evaluating tasks with multiple refrences per input.
- `document_start_index`: an `int32` feature. Character index that enables easy parsing of the context document.
- `document_end_index`: an `int32` feature. Character index that enables easy parsing of the context document.
- `query_start_index`: an `int32` feature. Character index that enables easy parsing of the query, if exists.
- `query_end_index`: an `int32` feature. Character index that enables easy parsing of the query, if exists.
- `truncation_seperator`: a `string` feature. The string used to append to a trimmed context document, mentioning the context was trimmed.

Datasets containing multiple documents inside the `input` feature are MuSiQue, SpaceDigest, and BookSumSort. They also have the following feature:

- `inner_docs_start_indices`: a sequence of `int32` feature. Character indexes that enables easy parsing of the the inner documents, e.g. Reviews, of Summaries.

## Citations

```
@inproceedings{shaham-etal-2023-zeroscrolls,
    title = "{Z}ero{SCROLLS}: A Zero-Shot Benchmark for Long Text Understanding",
    author = "Shaham, Uri  and
      Ivgi, Maor  and
      Efrat, Avia  and
      Berant, Jonathan  and
      Levy, Omer",
    editor = "Bouamor, Houda  and
      Pino, Juan  and
      Bali, Kalika",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2023",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.findings-emnlp.536",
    doi = "10.18653/v1/2023.findings-emnlp.536",
    pages = "7977--7989"
}
```