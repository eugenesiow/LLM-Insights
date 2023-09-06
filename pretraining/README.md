# Pre-Training

## Tokenization

### Tests

1. **Whitespace** Is whitespace tokenized properly? This is important for programming languages that depend on whitespace like Python. In this test we use the tokenizer to encode the text and decode it without special tokens (`skip_special_tokens=True`) and check for equivalence.
2. **Digits** Are digits tokenized individually? This is important for solving math problems [1]. A series of digits of varying lengths are passed in with encoders set not to encode special tokens (`add_special_tokens=False`). The output list of token ids are compared in length with the input length of digits.
3. **Multi-Lingual** Does the tokenizer support tokens from non-latin languages like mandarin chinese (zh)?

### Results

|       Tokenizer       |               Model                |Vocab |Whitespace|Digits| zh  |
|-----------------------|------------------------------------|-----:|----------|------|----:|
|LlamaTokenizerFast     |meta-llama/Llama-2-7b               | 32000|Pass      |Pass  |100.0|
|LlamaTokenizer         |meta-llama/Llama-2-7b               | 32000|Pass      |Pass  |100.0|
|T5TokenizerFast        |google/flan-t5-small                | 32100|Fail      |Fail  |  0.0|
|T5Tokenizer            |google/flan-t5-small                | 32100|Fail      |Fail  |  0.0|
|GPTNeoXTokenizerFast   |EleutherAI/gpt-neox-20b             | 50254|Pass      |Fail  |100.0|
|PreTrainedTokenizerFast|tiiuae/falcon-7b                    | 65024|Pass      |Fail  |100.0|
|BertTokenizerFast      |bert-base-uncased                   | 30522|Fail      |Fail  |  1.2|
|BertTokenizer          |bert-base-uncased                   | 30522|Fail      |Fail  |  1.2|
|GPT2TokenizerFast      |Deci/DeciCoder-1b                   | 49152|Pass      |Pass  |100.0|
|GPT2Tokenizer          |Deci/DeciCoder-1b                   | 49152|Pass      |Pass  |100.0|
|QWenTokenizer          |Qwen/Qwen-7B                        |151851|Pass      |Pass  |100.0|
|GPT2TokenizerFast      |bigcode/starcoder                   | 49152|Pass      |Pass  |100.0|
|GPT2Tokenizer          |bigcode/starcoder                   | 49152|Pass      |Pass  |100.0|
|GPT2TokenizerFast      |WizardLM/WizardCoder-15B-V1.0       | 49152|Pass      |Pass  |100.0|
|GPT2Tokenizer          |WizardLM/WizardCoder-15B-V1.0       | 49152|Pass      |Pass  |100.0|
|LlamaTokenizer         |Phind/Phind-CodeLlama-34B-v2        | 32000|Pass      |Pass  |100.0|
|LlamaTokenizerFast     |WizardLM/WizardCoder-Python-34B-V1.0| 32000|Pass      |Pass  |100.0|
|LlamaTokenizer         |WizardLM/WizardCoder-Python-34B-V1.0| 32000|Pass      |Pass  |100.0|
|GPT2TokenizerFast      |defog/sqlcoder                      | 49152|Pass      |Pass  |100.0|
|GPT2Tokenizer          |defog/sqlcoder                      | 49152|Pass      |Pass  |100.0|
|LlamaTokenizer         |HuggingFaceM4/idefics-80b-instruct  | 32000|Pass      |Pass  |100.0|

- `LlamaTokenizerFast` adds a `<s>\s` in front of the text. When using the transformers library's `add_special_tokens=False` parameter, although the `<s>` is removed but the `\s` remains. Hence the number of digits encoded is different from the number of digits in the input sequence.
- `zh` tokenization measures the percentage of characters can be successfully encoded and decoded using the tokenizer from `\u4e00` to `\u9ff0`. An example of an unsuccessful decoding would be the `<unk>` token.

## Scaling

### References

1. [Tiedong Liu, & Bryan Kian Hsiang Low. (2023). Goat: Fine-tuned LLaMA Outperforms GPT-4 on Arithmetic Tasks.](https://arxiv.org/abs/2305.14201)
2. [Anthony, Q., Biderman, S., & Schoelkopf, H.. (2023). Transformer Math 101.](https://blog.eleuther.ai/transformer-math/)
3. https://kipp.ly/transformer-inference-arithmetic/
4. https://medium.com/@dzmitrybahdanau/the-flops-calculus-of-language-model-training-3b19c1f025e4
5. https://huggingface.co/spaces/hf-accelerate/model-memory-usage