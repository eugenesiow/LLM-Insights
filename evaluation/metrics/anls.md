# ANLS and ANLS*

For image understanding and reasoning benchmarks, where answers are contained within the text found in the image, accuracy of the answers are dependent on accuracy of the text recognition (e.g. Optical Character Recognition). For example, if the model reasons properly about the answer but makes a mistake of a few characters in the recognition stage, like
the typical accuracy score would be 0. With the Average Normalized Levenshtein Similarity (ANLS) would give an intermediate score between 0.5 and 1 that will softly penalise the text recognition mistakes. 

## ANLS

Formally, the **ANLS** (Average Normalized Levenshtein Similarity) score is defined as:

$$
\text{ANLS} = \frac{1}{N} \sum_{i=0}^{N} \left( \max_j \, s(a_{ij}, o_{q_i}) \right)
\quad (1)
$$

where the similarity function $ s(a_{ij}, o_{q_i}) $ is defined as:

$$
s(a_{ij}, o_{q_i}) = 
\begin{cases}
1 - NL(a_{ij}, o_{q_i}) & \text{if } NL(a_{ij}, o_{q_i}) < \tau \\
0 & \text{if } NL(a_{ij}, o_{q_i}) \geq \tau
\end{cases}
\quad (2)
$$

where:

- $ N $ is the total number of questions in the dataset,  
- $ M $ is the total number of ground truth answers per question,  
- $ a_{ij} $ are the ground truth answers where $ i = \{0, ..., N\} $, $ j = \{0, ..., M\} $,  
- $ o_{q_i} $ is the network’s answer for the $ i^{\text{th}} $ question $ q_i $,  
- $ NL(a_{ij}, o_{q_i}) $ is the **normalized Levenshtein distance** between the strings $a_{ij}$ and $o_{q_i}$ (notice that the normalized Levenshtein distance is a value between 0 and 1),  
- $ \tau $ is a threshold value.

## ANLS*

A shortcoming of the ANLS metric is that it can only deal with strings and lists, but cannot be used for dictionaries or any combination of types that are often encountered when dealing with information extraction tasks. Additionally, some tasks require to extract information with a list structure such as [line-item extraction](https://arxiv.org/abs/2302.05658), which requires the evaluation of complex output objects.

ANLS* is a metric that can be used to evaluate a wide variety of tasks such as information extraction or classification, even in cases where output values that may contain minor errors.

The **ANLS\*** score is defined as:

$$
\text{ANLS}^*(g, p) = \frac{s(g, p)}{l(g, p)}
\quad (3)
$$

where:

- $ s $ is the score between the ground truth and the prediction,  
- $ l $ is the size of the trees $ g $ and $ p $,  
- $ \text{ANLS}^*(g, p) \in [0, 1] $

Additionally, it is worth noting that each prediction in this tree is given equal weight. This implies that leaf nodes of large sub-trees carry the same weight as leaf nodes that appear at the top level.

The score $s$ is defined recursively to measure the similarity between the ground truth and the prediction. Note that in order to distinguish between the *one-of* semantic of a ground truth list used by the ANLS metric, and the matching semantic implemented in the ANLSL metric, we introduced Tuples for the former and Lists for the latter. The score $s$ is defined as follows:

$$
s(g, p) =
\begin{cases}
    1.0 & \text{if } \text{type}(g) = \text{type}(p) = \text{None} \\
    1.0 - \frac{\text{LD}(g, p)}{\max(|g|, |p|)} & \text{if } \text{type}(g) = \text{type}(p) = \text{String and } s(g, p) \ge \tau \\
    s(g_i, p_i) \text{ with } i = \operatorname{argmax}_j (\text{ANLS}^*(g_j, p)) & \text{if } \text{type}(g) = \text{Tuple} \\
    \frac{1}{|\psi(g, p)|} \sum_{(g_i, p_i) \in \psi(g, p)} s(g_i, p_i) & \text{if } \text{type}(g) = \text{type}(p) = \text{List} \\
    \frac{1}{|\text{keys}(p)|} \sum_{k \in \text{keys}(p)} s(g_k, p_k) & \text{if } \text{type}(g) = \text{type}(p) = \text{Dict and } k \in \text{keys}(p) \\
    0.0 & \text{otherwise}
\end{cases}
\quad (4)
$$

with LD being the Levenshtein distance and $\tau$ being the normalized Levenshtein distance threshold which is set to $\tau = 0.5$. $\psi$ is the Hungarian matching algorithm [9] performed according to the pairwise ANLS* of each ground truth and prediction element. This algorithm returns an optimal matching of elements between two lists w.r.t. a given score. The score for type mismatches (i.e., different subtrees) yields a score of 0.0. The function $\text{keys}(x)$ returns all keys of a dictionary $x$, that are not None. It is important that $\text{keys}(x)$ ignores None values in order to penalize hallucinations correctly.

To normalize $s$, we define the length $l$ of each type as follows:

$$
l(g, p) =
\begin{cases}
    1 & \text{if } \text{type}(x) = \text{type}(p) = \text{None} \\
    1 & \text{if } \text{type}(g) = \text{type}(p) = \text{String} \\
    l(g_i, p_i) \text{ with } i = \operatorname{argmax}_j (\text{ANLS}^*(g_j, p)) & \text{if } \text{type}(g) = \text{Tuple} \\
    \sum_{(g_i, p_i) \in \psi(g, p)} l(g_i, p_i) + \sum_{g_u \in g \setminus \psi(g, p)} l_t(g_u) + \sum_{p_v \in p \setminus \psi(g, p)} l_t(p_v) & \text{if } \text{type}(g) = \text{type}(p) = \text{List} \\
    \sum_{k \in \text{keys}(p) \cap \text{keys}(q)} l(g_k, p_k) + \sum_{k \in \text{keys}(g) \setminus \text{keys}(p)} l_t(g_k) + \sum_{k \in \text{keys}(p) \setminus \text{keys}(g)} l_t(p_k) & \text{if } \text{type}(g) = \text{type}(p) = \text{Dict} \\
    \max(l_t(g), l_t(p)) & \text{otherwise}
\end{cases}
\quad (5)
$$

As can be seen, the length is weighted for all type matches accordingly. Nevertheless, it is not guaranteed that the prediction produced the correct output structure. On the other hand, a partially correct structure should not get a score of 0.0. To this end, we match the subtree and penalize wrong types via another length function $l_t$. It can be seen that the maximum length is used between the ground truth and the prediction - $\max(l_t(g), l_t(p))$ - such that both, missing subtrees, as well as hallucinated subtrees, are penalized equally. The length function $l_t$ is defined as follows:

$$
l_t(x) =
\begin{cases}
    1 & \text{if } \text{type}(x) = \text{None} \\
    1 & \text{if } \text{type}(x) = \text{String} \\
    \max_{x_i \in x} l_t(x_i) & \text{if } \text{type}(x) = \text{Tuple} \\
    \sum_{x_i \in x} l_t(x_i) & \text{if } \text{type}(x) = \text{List} \\
    \sum_{k \in \text{keys}(x)} l_t(x_k) & \text{if } \text{type}(x) = \text{Dict}
\end{cases}
\quad (6)
$$

where $x$ is either a (sub)tree of the prediction $p$ or a (sub)tree of the ground truth $g$.

## Citations

```bibtex
@misc{biten2019scenetextvisualquestion,
      title={Scene Text Visual Question Answering}, 
      author={Ali Furkan Biten and Ruben Tito and Andres Mafla and Lluis Gomez and Marçal Rusiñol and Ernest Valveny and C. V. Jawahar and Dimosthenis Karatzas},
      year={2019},
      eprint={1905.13648},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/1905.13648}, 
}
```

```bibtex
@misc{peer2025anlsuniversaldocument,
      title={ANLS* -- A Universal Document Processing Metric for Generative Large Language Models}, 
      author={David Peer and Philemon Schöpf and Volckmar Nebendahl and Alexander Rietzler and Sebastian Stabinger},
      year={2025},
      eprint={2402.03848},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2402.03848}, 
}
```