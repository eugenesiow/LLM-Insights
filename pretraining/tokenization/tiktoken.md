# tiktoken

## Vocabulary

`.tiktoken` files are basically made up of lines of a base64 encoded token, a space, and a rank/index integer value. These are BPE.

The function below will read a `.tiktoken` file for its vocabulary.
```python
import base64


def load_tiktoken_bpe(tiktoken_bpe_file: str, expected_hash: str | None = None) -> dict[bytes, int]:
    with open(tiktoken_bpe_file) as f:
        contents = f.read()
        return {
            base64.b64decode(token): int(rank)
            for token, rank in (line.split() for line in contents.splitlines() if line)
        }
```

## Others

```python
encoding = tiktoken.get_encoding(tokenizer_name)
vocab = encoding._mergeable_ranks
pattern=encoding._pat_str, 
additional_special_tokens=encoding._special_tokens
```

References:
- https://huggingface.co/docs/transformers/main/en/tiktoken
- https://github.com/meta-llama/llama3/blob/main/llama/tokenizer.py
- https://github.com/openai/tiktoken/tree/main#extending-tiktoken
- https://github.com/openai/tiktoken/blob/main/tiktoken_ext/openai_public.py
- https://github.com/huggingface/transformers/blob/main/src/transformers/convert_slow_tokenizer.py#L1474
- https://github.com/huggingface/transformers/blob/main/src/transformers/integrations/tiktoken.py
- https://github.com/huggingface/transformers/issues/34221
- https://gist.github.com/xenova/a452a6474428de0182b17605a98631ee
- https://github.com/huggingface/transformers/issues/31187
- https://huggingface.co/meta-llama/Meta-Llama-3-8B/discussions/12