# lm-format-enforcer

[lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer) is a library that enforces the output format of language models by filtering tokens.

## How it Works

It works by combining a [character level parser](https://github.com/noamgat/lm-format-enforcer/blob/main/lmformatenforcer/characterlevelparser.py) with a [tokenizer prefix tree](https://github.com/noamgat/lm-format-enforcer/blob/main/lmformatenforcer/tokenizerprefixtree.py) to allow only the tokens which contains sequences of characters that lead to a potentially valid format.

![How lm-format-enforcer works using a character level parser and a tokenizer prefix tree.](./images/lm-format-enforcer-diagram.svg "How lm-format-enforcer works using a character level parser and a tokenizer prefix tree. Source: noamgat/lm-format-enforcer")

The **character level parser** is an abstract data structure that represents the set of allowed next characters as a tree. For example, in the diagram above (on the left) the `JsonSchemaParser` implementation of the character level parser represents the set of allowed next characters after `{"` as a tree structure. Based on the provided JSON schema, this could be `first_name`, `last_name`, `num_seasons_in_nba` or `year_of_birth`. 

The **tokenizer prefix tree** is generated from the vocabulary of a language model tokenizer. If a token is a prefix of another, it will occupy the parent position in a tree and this can be repeated up to the root.

Given a **character level parser** and a **tokenizer prefix tree**, one can filter the tokens that the language model is allowed to generate at the next timestep. Only the characters that are in BOTH the character level parsing node and the tokenizer prefix tree node are traversed. Once the language model has generated a token, the character level parser is advanced according to the new characters, ready to filter the next timestep.

## Usage

With VLLM:
```python
from pydantic import BaseModel
from enum import Enum

class CarType(str, Enum):
    sedan = "sedan"
    suv = "SUV"
    truck = "Truck"
    coupe = "Coupe"


class CarDescription(BaseModel):
    brand: str
    model: str
    car_type: CarType


json_schema = CarDescription.model_json_schema()

completion = client.chat.completions.create(
    model="Qwen/Qwen2.5-3B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "Generate a JSON with the brand, model and car_type of the most iconic car from the 90's",
        }
    ],
    extra_body={"guided_json": json_schema},
)
print(completion.choices[0].message.content)
```

References:
- https://github.com/noamgat/lm-format-enforcer
- https://github.com/noamgat/lm-format-enforcer/tree/main?tab=readme-ov-file#how-does-it-work
- https://docs.vllm.ai/en/latest/usage/structured_outputs.html