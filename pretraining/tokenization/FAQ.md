# FAQ

## Do Deepseek-R1, Deepseek-V3 and Deepseek-V2 use the same tokenizer?

Deepseek-R1 and Deepseek-V3 use the same tokenizer ([LlamaTokenizerFast](https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/tokenization_llama_fast.py#L49)) which has a vocabulary size of 128,000. Deepseek-V2 ([LlamaTokenizerFast](https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/tokenization_llama_fast.py#L49)) uses a vocabulary size of 100,000.

## Do LLaMA-1, LLaMA-2 and LLaMA-3 use the same tokenizer?

No. The 1,2 and 3 versions of LLaMA use different tokenizers. LLaMA-3's tokenizer ([PreTrainedTokenizerFast](https://github.com/huggingface/transformers/blob/main/src/transformers/tokenization_utils_fast.py#L82)) has a vocabulary size of 128,000 while LLaMA-1 ([LlamaTokenizerFast](https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/tokenization_llama_fast.py#L49)) and LLaMA-2 ([LlamaTokenizerFast](https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/tokenization_llama_fast.py#L49)) both have a vocabulary size of 32,000.