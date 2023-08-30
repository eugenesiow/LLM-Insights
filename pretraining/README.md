# Pre-Training

## Tokenization

### Tests

1. **Whitespace** Is whitespace tokenized properly? This is important for programming languages that depend on whitespace like Python. In this test we use the tokenizer to encode the text and decode it without special tokens (`skip_special_tokens=True`) and check for equivalence.
2. **Digits** Are digits tokenized individually? This is important for solving math problems [1]. A series of digits of varying lengths are passed in with encoders set not to encode special tokens (`add_special_tokens=False`). The output list of token ids are compared in length with the input length of digits.
3. **Multi-Lingual** Does the tokenizer support tokens from non-latin languages like mandarin chinese?

### Results

|       Tokenizer       |               Model                |Whitespace|Digits|
|-----------------------|------------------------------------|----------|------|
|LlamaTokenizerFast     |meta-llama/Llama-2-7b               |Pass      |Pass  |
|LlamaTokenizer         |meta-llama/Llama-2-7b               |Pass      |Pass  |
|T5TokenizerFast        |google/flan-t5-small                |Fail      |Fail  |
|T5Tokenizer            |google/flan-t5-small                |Fail      |Fail  |
|GPTNeoXTokenizerFast   |EleutherAI/gpt-neox-20b             |Pass      |Fail  |
|PreTrainedTokenizerFast|tiiuae/falcon-7b                    |Pass      |Fail  |
|PreTrainedTokenizerFast|tiiuae/falcon-7b                    |Pass      |Fail  |
|PreTrainedTokenizerFast|tiiuae/falcon-7b                    |Pass      |Fail  |
|PreTrainedTokenizerFast|tiiuae/falcon-7b                    |Pass      |Fail  |
|BertTokenizerFast      |bert-base-uncased                   |Fail      |Fail  |
|BertTokenizer          |bert-base-uncased                   |Fail      |Fail  |
|GPT2TokenizerFast      |Deci/DeciCoder-1b                   |Pass      |Pass  |
|GPT2Tokenizer          |Deci/DeciCoder-1b                   |Pass      |Pass  |
|QWenTokenizer          |Qwen/Qwen-7B                        |Pass      |Pass  |
|QWenTokenizer          |Qwen/Qwen-7B                        |Pass      |Pass  |
|QWenTokenizer          |Qwen/Qwen-7B                        |Pass      |Pass  |
|QWenTokenizer          |Qwen/Qwen-7B                        |Pass      |Pass  |
|GPT2TokenizerFast      |bigcode/starcoder                   |Pass      |Pass  |
|GPT2Tokenizer          |bigcode/starcoder                   |Pass      |Pass  |
|GPT2TokenizerFast      |WizardLM/WizardCoder-15B-V1.0       |Pass      |Pass  |
|GPT2Tokenizer          |WizardLM/WizardCoder-15B-V1.0       |Pass      |Pass  |
|LlamaTokenizer         |Phind/Phind-CodeLlama-34B-v2        |Pass      |Pass  |
|LlamaTokenizerFast     |WizardLM/WizardCoder-Python-34B-V1.0|Pass      |Pass  |
|LlamaTokenizer         |WizardLM/WizardCoder-Python-34B-V1.0|Pass      |Pass  |
|GPT2TokenizerFast      |defog/sqlcoder                      |Pass      |Pass  |
|GPT2Tokenizer          |defog/sqlcoder                      |Pass      |Pass  |
|LlamaTokenizer         |HuggingFaceM4/idefics-80b-instruct  |Pass      |Pass  |

- `LlamaTokenizerFast` adds a `<s> ` in front of the text. When using the `add_special_tokens=False` parameter, although the `<s>` is removed but the ` ` remains. Hence the number of digits encoded is different from the number of digits in the input sequence.

## Scaling

### References

1. [Tiedong Liu, & Bryan Kian Hsiang Low. (2023). Goat: Fine-tuned LLaMA Outperforms GPT-4 on Arithmetic Tasks.](https://arxiv.org/abs/2305.14201)
2. [Anthony, Q., Biderman, S., & Schoelkopf, H.. (2023). Transformer Math 101.](https://blog.eleuther.ai/transformer-math/)
3. https://kipp.ly/transformer-inference-arithmetic/
4. https://medium.com/@dzmitrybahdanau/the-flops-calculus-of-language-model-training-3b19c1f025e4
5. https://huggingface.co/spaces/hf-accelerate/model-memory-usage