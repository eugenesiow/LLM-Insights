# Word Tokenizer

**Word Tokenization** is the splitting of sequences (e.g. documents, sentences) at a word-level (e.g. on white spaces for latin script languages) and considering each word as a
token. This is different from the GPT or LLaMA type Large Language Models (LLMs) which use sub-word tokenization. In sub-word tokenization, words are decomposed into subwords with multiple tokens. Sub-word tokenization is currently the established tokenization approach upon which LLMs rely.

Different languages belong to different language families and might use different scripts (think of Japanese characters from the Japonic language family for example). Fortunately, SpaCy has word-level tokenizers for most languages which we can leverage.

References:
- https://huggingface.co/spaces/HuggingFaceFW-Dev/lang-word-tokenizers
- https://github.com/huggingface/datatrove/blob/main/src/datatrove/assets/tokenizer_assignment.csv
- https://spacy.io/api/tokenizer