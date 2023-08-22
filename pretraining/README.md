# Pre-Training

## Tokenization

### Tests

1. **Whitespace** Is whitespace tokenized properly? This is important for programming languages that depend on whitespace like Python. In this test we use the tokenizer to encode the text and decode it without special tokens (`skip_special_tokens=True`) and check for equivalence.
2. **Digits** Are digits tokenized individually? This is important for solving math problems [1]. A series of digits of varying lengths are passed in with encoders set not to encode special tokens (`add_special_tokens=False`). The output list of token ids are compared in length with the input length of digits.
3. **Multi-Lingual** Does the tokenizer support tokens from non-latin languages like mandarin chinese?

### Results

| Tokenizer | Model | Whitespace | Digits |
| --- | --- | --- | --- |
| LlamaTokenizerFast | Llama-2-7b-hf | Pass | Fail |
| T5TokenizerFast | flan-t5-small | Fail | Fail |
| GPTNeoXTokenizerFast | gpt-neox-20b | Pass | Fail |
| PreTrainedTokenizerFast | tiiuae/falcon-7b | Pass | Fail |
| BertTokenizerFast | bert-base-uncased | Fail | Fail |
| GPT2TokenizerFast | DeciCoder-1b | Pass | Pass |
| GPT2TokenizerFast | starcoder | Pass | Pass |
| GPT2TokenizerFast | WizardCoder-15B-V1.0 | Pass | Pass |

- `LlamaTokenizerFast` fails the digits test because the tokenizer usually adds a `<s> ` in front of the text. When using the `add_special_tokens=False` parameter, although the `<s>` is removed but the ` ` remains. Hence the number of digits encoded is different from the number of digits in the input sequence.

### References

1. [Tiedong Liu, & Bryan Kian Hsiang Low. (2023). Goat: Fine-tuned LLaMA Outperforms GPT-4 on Arithmetic Tasks.](https://arxiv.org/abs/2305.14201)