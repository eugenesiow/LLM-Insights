# Common Crawl Index

## Parsing

The following Python code will load and parse an `input_file` containing a CDX shard of the common crawl index for this collection.
```python
import json

with gzip.open(input_file, 'rt', encoding='utf-8') as f:
    for line in f:
        parts = line.split(' ')
        json_string = ' '.join(parts[2:])
        json_content = json.loads(json_string)
```