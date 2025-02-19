# Tokenization

- [Tokenization](#tokenization)
  - [All Tokenizers Are Not Made Equal](#all-tokenizers-are-not-made-equal)
    - [Tests](#tests)
    - [Results](#results)
  - [Packing](#packing)
  - [Scaling](#scaling)
  - [References](#references)

## All Tokenizers Are Not Made Equal

### Metrics

1. **Fertility** average number of tokens that are required to represent a word or document. Higher fertility scores correspond to weaker compression capabilities of the tokenizer.

2. **Parity** assesses how fairly a tokenizer treats equivalent sentences in different languages. The premium is the ratio $\frac{|T(s_{A})|}{|T(s_{B})|}$, where $T$ is the tokenizer and $s_{A}$ and $s_{B}$ denote the sets of all sentences in the corpora of languages $A$ and $B$. A tokenizer $T$ can be said to achieve parity for language $A$ with respect to language $B$ if $\frac{|T(s_{A})|}{|T(s_{B})|} = 1$.

3. **Proportion of Continued Words** The proportion of pre-tokenized words within the document or corpus that are represented by more than one token [[12]](#12).

4. **Vocabulary Overlap** The divergence between vocabulary distributions of different languages. It is bounded in the range 0 to 1, and a lower value indicates a higher overlap between languages [[13]](#13). 

### Computational Costs

The following formula represents the impact of a tokenizer on the average computational costs of a given model per word during training. This formula is calculating the number of floating point operations based on assumption that this is a transformer language model with $l$ transformer layers [[11]](#11). The computational costs during training for one step including the forward and the backward pass can be estimated by  

$$
C = 96 B s l h^2 \left( 1 + \frac{s}{6h} + \frac{V}{16lh} \right)
$$  

Given batch size $B$, sequence length $s$, $l$ layers, hidden size $h$ and vocabulary size $V$. 

**Deriving costs per token and per word.** The costs per token can be derived by $C_{\text{token}} = C / Bs$ and the average costs per word by $C_{\text{word}} = C_{\text{token}} \times \text{fertility}$.

### Tests

1. **Whitespace** Is whitespace tokenized properly? This is important for programming languages that depend on whitespace like Python. In this test we use the tokenizer to encode the text and decode it without special tokens (`skip_special_tokens=True`) and check for equivalence.
2. **Digits** Are digits tokenized individually? This is important for solving math problems [1]. A series of digits of varying lengths are passed in with encoders set not to encode special tokens (`add_special_tokens=False`). The output list of token ids are compared in length with the input length of digits.
3. **Multi-Lingual** Does the tokenizer support tokens from non-latin languages like mandarin chinese (zh), thai (th)?

### Results

|       Tokenizer       |               Model                |Vocab |Whitespace|Digits| zh  | th  |
|-----------------------|------------------------------------|-----:|----------|------|----:|----:|
|cl100k_base            |gpt-4                               |100277|Pass      |      |     |     |
|cl100k_base            |gpt-3.5-turbo                       |100277|Pass      |      |     |     |
|cl100k_base            |text-embedding-ada-002              |100277|Pass      |      |     |     |
|p50k_base              |text-davinci-002                    |50281 |Pass      |      |     |     |
|p50k_base              |text-davinci-003                    |50281 |Pass      |      |     |     |
|r50k_base              |davinci                             |50257 |Pass      |      |     |     |
|LlamaTokenizerFast     |meta-llama/Llama-2-7b               | 32000|Pass      |Pass  |100.0|100.0|
|LlamaTokenizer         |meta-llama/Llama-2-7b               | 32000|Pass      |Pass  |100.0|100.0|
|T5TokenizerFast        |google/flan-t5-small                | 32100|Fail      |Fail  |  0.0|  0.0|
|T5Tokenizer            |google/flan-t5-small                | 32100|Fail      |Fail  |  0.0|  0.0|
|GPTNeoXTokenizerFast   |EleutherAI/gpt-neox-20b             | 50254|Pass      |Fail  |100.0|100.0|
|PreTrainedTokenizerFast|tiiuae/falcon-7b                    | 65024|Pass      |Fail  |100.0|100.0|
|BertTokenizerFast      |bert-base-uncased                   | 30522|Fail      |Fail  |  1.2| 11.8|
|BertTokenizer          |bert-base-uncased                   | 30522|Fail      |Fail  |  1.2| 11.8|
|GPT2TokenizerFast      |Deci/DeciCoder-1b                   | 49152|Pass      |Pass  |100.0|100.0|
|GPT2Tokenizer          |Deci/DeciCoder-1b                   | 49152|Pass      |Pass  |100.0|100.0|
|QWenTokenizer          |Qwen/Qwen-7B                        |151851|Pass      |Pass  |100.0|100.0|
|GPT2TokenizerFast      |bigcode/starcoder                   | 49152|Pass      |Pass  |100.0|100.0|
|GPT2Tokenizer          |bigcode/starcoder                   | 49152|Pass      |Pass  |100.0|100.0|
|GPT2TokenizerFast      |WizardLM/WizardCoder-15B-V1.0       | 49152|Pass      |Pass  |100.0|100.0|
|GPT2Tokenizer          |WizardLM/WizardCoder-15B-V1.0       | 49152|Pass      |Pass  |100.0|100.0|
|LlamaTokenizerFast     |Phind/Phind-CodeLlama-34B-v2        | 32000|Pass      |Pass  |100.0|100.0|
|LlamaTokenizer         |Phind/Phind-CodeLlama-34B-v2        | 32000|Pass      |Pass  |100.0|100.0|
|LlamaTokenizerFast     |WizardLM/WizardCoder-Python-34B-V1.0| 32000|Pass      |Pass  |100.0|100.0|
|LlamaTokenizer         |WizardLM/WizardCoder-Python-34B-V1.0| 32000|Pass      |Pass  |100.0|100.0|
|GPT2TokenizerFast      |defog/sqlcoder                      | 49152|Pass      |Pass  |100.0|100.0|
|GPT2Tokenizer          |defog/sqlcoder                      | 49152|Pass      |Pass  |100.0|100.0|
|LlamaTokenizerFast     |HuggingFaceM4/idefics-80b-instruct  | 32000|Pass      |Pass  |100.0|100.0|
|LlamaTokenizer         |HuggingFaceM4/idefics-80b-instruct  | 32000|Pass      |Pass  |100.0|100.0|
|ChatGLMTokenizer       |THUDM/chatglm2-6b                   | 64794|Pass      |Pass  |100.0|100.0|
|ChatGLMTokenizer       |THUDM/chatglm-6b                    |130344|Pass      |Pass  |100.0| 99.2|
|BloomTokenizerFast     |bigscience/bloomz                   |250680|Pass      |Fail  |100.0|100.0|

- `LlamaTokenizer` adds a `<s>\s` in front of the text. When using the transformers library's `add_special_tokens=False` parameter, although the `<s>` is removed but the `\s` remains. Hence the number of digits encoded is different from the number of digits in the input sequence.
- `zh` tokenization measures the percentage of [unicode](unicode.md) characters can be successfully encoded and decoded using the tokenizer from `\u4e00` to `\u9ff0`. An example of an unsuccessful decoding would be the `<unk>` token.
- The `th` block has 87 [unicode](unicode.md) filled and another 41 empty [7], but we test with `\u0e00` to `\u0e7f` rather than just the filled ranges, (`\u0e01`, `\u0e3a`), (`\u0e3f`, `\u0e5b`) as we’re using a similar method with the `zh` character set. 
- Tokenizers based on SentencePiece [8] like the `LlamaTokenizer` [9] split all numbers into individual digits, and fallback to bytes to decompose unknown UTF-8 characters. They should pass the whitespace, digits and multi-lingual tests if trained properly.

## Packing

The Multipack sampler [6] is designed for padding-free distributed training of large language models. It utilizes an approximate solution to the identical machine scheduling problem to maximize the efficiency of batch processing. On the OpenChat V1 training set, it achieves >99% theoretical efficiency, while the interleaved sampler only achieves ~75%.

## Scaling

## References

1. [Tiedong Liu, & Bryan Kian Hsiang Low. (2023). Goat: Fine-tuned LLaMA Outperforms GPT-4 on Arithmetic Tasks.](https://arxiv.org/abs/2305.14201)
2. [Anthony, Q., Biderman, S., & Schoelkopf, H.. (2023). Transformer Math 101.](https://blog.eleuther.ai/transformer-math/)
3. https://kipp.ly/transformer-inference-arithmetic/
4. https://medium.com/@dzmitrybahdanau/the-flops-calculus-of-language-model-training-3b19c1f025e4
5. https://huggingface.co/spaces/hf-accelerate/model-memory-usage
6. https://github.com/imoneoi/multipack_sampler
7. https://en.wikipedia.org/wiki/Thai_(Unicode_block)
8. [Taku Kudo, & John Richardson. (2018). SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing.](https://arxiv.org/abs/1808.06226)
9. [Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, & Guillaume Lample. (2023). LLaMA: Open and Efficient Foundation Language Models.](https://arxiv.org/abs/2302.13971)
10. [Ali, Mehdi, et al. “Tokenizer Choice for LLM Training: Negligible or Crucial?” arXiv.org, 12 Oct. 2023.](https://arxiv.org/abs/2310.08754)
11. <a id="11"></a> [D. Narayanan et al., “Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM,” arXiv.org, Aug. 23, 2021.](https://arxiv.org/abs/2104.04473)
12. <a id="12"></a> [P. Rust, J. Pfeiffer, I. Vulić, S. Ruder, and I. Gurevych, “How Good is Your Tokenizer? On the Monolingual Performance of Multilingual Language Models,” arXiv.org, 2020.](https://arxiv.org/abs/2012.15613)
13. <a id="13"></a>[T. Limisiewicz, J. Balhar, and D. Mareček, “Tokenization Impacts Multilingual Language Modeling: Assessing Vocabulary Allocation and Overlap Across Languages,” arXiv.org, 2023.](https://arxiv.org/abs/2305.17179)