# lm-format-enforcer

[lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer) is a library that enforces the output format of language models by filtering tokens.

It works by combining a [character level parser](https://github.com/noamgat/lm-format-enforcer/blob/main/lmformatenforcer/characterlevelparser.py) with a [tokenizer prefix tree](https://github.com/noamgat/lm-format-enforcer/blob/main/lmformatenforcer/tokenizerprefixtree.py) to allow only the tokens which contains sequences of characters that lead to a potentially valid format.

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
- https://docs.vllm.ai/en/latest/usage/structured_outputs.html