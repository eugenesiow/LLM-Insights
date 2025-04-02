# BFCL

The Berkeley Function-Calling Leaderboard (BFCL) is a benchmark that serves as a standard for evaluating the function-calling, or tool-use, capabilities of Large Language Models' (LLMs). Unlike previous evaluations, BFCL accounts for various forms of function calls, diverse scenarios, and executability.

**BFCL V1** includes 100 Java, 50 JavaScript, 70 REST API, 100 SQL, and 1,680 Python on various simple, parallel, multiple, executable functions calling scenarios as well as function relevance detection.

The dataset within **BFCL V2** comprises 2,251 question-function-answer pairs, where a user's question is paired with a set of available functions and the expected answer. This collection includes a wide variety of function documentations, some featuring an extensive number of function options (more than ten) or intricate functions with numerous nested parameters (also exceeding ten). Furthermore, the user queries within the dataset exhibit significant diversity in tone, originate from multi-turn interactions, cover specialized and varied use cases, and span multiple languages. The benchmark categorizes its entries into several types to comprehensively assess different aspects of function calling: simple calls, multiple function choices, parallel function calls, parallel calls with multiple options, irrelevance detection, and relevance detection. 

Within the BFCL V2 dataset, an average entry presents the LLM with three function choices, with the most complex scenario offering 37 options. On average, each function in the dataset has four parameters, but some can have as many as 28. The benchmark also distinguishes between irrelevance detection, where none of the provided functions are suitable for the user's query and the model should ideally not invoke any function, and relevance detection, where at least one function is relevant, and the model is expected to identify and call a relevant function, although the correctness of the parameters provided is not evaluated in this category.   

The data underpinning the dataset is sourced from real-world user interactions with hosted model endpoints through partnerships and public access on the project's website. Before inclusion in the benchmark, the raw data undergoes a rigorous pre-processing phase that includes deduplication using the ROUGE-L score to ensure the uniqueness of both function documentation and user queries (through text embedding models). Additionally, user-provided function documentation strings are parsed into a standardized JSON format to facilitate evaluation. A data filtering process is also employed to identify and manage low-quality inputs and to isolate irrelevant queries for specific testing purposes. Examples of data considered low-quality include function descriptions that are too generic, such as "go search the web to obtain up-to-date information," or user prompts that lack the necessary information for invoking a specific function. The benchmark places a strong emphasis on the precise definition of function parameters, requiring correct categorization of parameter types, clear indication of which parameters are mandatory, adherence to specific formatting guidelines for dictionary and array-type parameters, and the explicit specification of default values for any optional parameters.   

**BFCL V3** still includes the Expert Curated (Non-live) dataset from BFCL V1 and the User Contributed (Live) dataset from BFCL V2. On top of that, it now tests how well models can handle back-and-forth (multi-turn) and step-by-step (multi-step) interactions.

## Links

* Homepage: 
    - V3 - https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html
    - V2 - https://gorilla.cs.berkeley.edu/blogs/12_bfcl_v2_live.html
    - V1 - https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html
* Leaderboard: https://gorilla.cs.berkeley.edu/leaderboard.html
* Dataset: 
    - V3 - https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard
    - V2 - https://github.com/ShishirPatil/gorilla/tree/v1.1/berkeley-function-call-leaderboard/data
    - V1 - https://github.com/ShishirPatil/gorilla/tree/v1.0/berkeley-function-call-leaderboard/data
* License: [Apache 2.0](https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard)

## Example Questions

<details>
<summary>simple_0</summary>

```json
{
    "id": "simple_0",
    "question": [
        [
            {
                "role": "user",
                "content": "Find the area of a triangle with a base of 10 units and height of 5 units."
            }
        ]
    ],
    "function": [
        {
            "name": "calculate_triangle_area",
            "description": "Calculate the area of a triangle given its base and height.",
            "parameters": {
                "type": "dict",
                "properties": {
                    "base": {
                        "type": "integer",
                        "description": "The base of the triangle."
                    },
                    "height": {
                        "type": "integer",
                        "description": "The height of the triangle."
                    },
                    "unit": {
                        "type": "string",
                        "description": "The unit of measure (defaults to 'units' if not specified)"
                    }
                },
                "required": [
                    "base",
                    "height"
                ]
            }
        }
    ]
}
```

</details>

<details>
<summary>multiple_0</summary>

```json
{
    "id": "multiple_0",
    "question": [
        [
            {
                "role": "user",
                "content": "Can I find the dimensions and properties of a triangle, if I know its three sides are 5 units, 4 units and 3 units long?"
            }
        ]
    ],
    "function": [
        {
            "name": "triangle_properties.get",
            "description": "Retrieve the dimensions, such as area and perimeter, of a triangle if lengths of three sides are given.",
            "parameters": {
                "type": "dict",
                "properties": {
                    "side1": {
                        "type": "integer",
                        "description": "The length of first side of the triangle."
                    },
                    "side2": {
                        "type": "integer",
                        "description": "The length of second side of the triangle."
                    },
                    "side3": {
                        "type": "integer",
                        "description": "The length of third side of the triangle."
                    },
                    "get_area": {
                        "type": "boolean",
                        "description": "A flag to determine whether to calculate the area of triangle. Default is true.",
                        "default": true,
                        "optional": true
                    },
                    "get_perimeter": {
                        "type": "boolean",
                        "description": "A flag to determine whether to calculate the perimeter of triangle. Default is true.",
                        "default": true,
                        "optional": true
                    },
                    "get_angles": {
                        "type": "boolean",
                        "description": "A flag to determine whether to calculate the internal angles of triangle. Default is true.",
                        "default": true,
                        "optional": true
                    }
                },
                "required": [
                    "side1",
                    "side2",
                    "side3"
                ]
            }
        },
        {
            "name": "circle_properties.get",
            "description": "Retrieve the dimensions, such as area and circumference, of a circle if radius is given.",
            "parameters": {
                "type": "dict",
                "properties": {
                    "radius": {
                        "type": "float",
                        "description": "The length of radius of the circle."
                    },
                    "get_area": {
                        "type": "boolean",
                        "description": "A flag to determine whether to calculate the area of circle. Default is true.",
                        "default": true,
                        "optional": true
                    },
                    "get_circumference": {
                        "type": "boolean",
                        "description": "A flag to determine whether to calculate the circumference of circle. Default is true.",
                        "default": true,
                        "optional": true
                    }
                },
                "required": [
                    "radius"
                ]
            }
        }
    ]
}
```

</details>

## Citations

```bibtex
@article{patil2023gorilla,
  title={Gorilla: Large Language Model Connected with Massive APIs},
  author={Shishir G. Patil and Tianjun Zhang and Xin Wang and Joseph E. Gonzalez},
  year={2023},
  journal={arXiv preprint arXiv:2305.15334},
} 
```