# n-shot Prompting

> **n-shot prompting** refers to the method of conditioning a language model with *n* example pairs that demonstrate the desired task, guiding the model to produce outputs consistent with the provided examples. Increasing the number of examples can help clarify task expectations and often leads to better performance. 0-shot prompting is a special case where only instructions are provided, without any examples.

When *n* is more than zero, we also call this **in-context learning**, where models are able to perform tasks based on examples given in the prompt, without any further parameter updates. If *n* is more than 1, we sometimes also call this **few-shot prompting**. This technique was really made famous GPT-3 onwards, when OpenAI published the [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) paper by Brown et al. (May 2020). 

To summarise the prompting strategies are generally categorized as:
- **Zero-shot or 0-shot prompting:** The model is provided with instructions only, without any examples.
- **One-shot prompting:** A single example is included in the prompt to illustrate the task.
- **n-shot prompting:** *n* examples are supplied to better capture the pattern or structure of the task, helping to guide the model's understanding of what is expected.

In few-shot prompting, examples serve as demonstrations from which the model extrapolates the pattern needed to generate a correct or contextually appropriate output. Good base models (like GPT-2 or GPT-3) which haven't been instruction-tuned (vs GPT-3.5 and above) and are trained just to complete sentences can with few-shot prompting also be taught to succeed in tasks like translation, summarization, question answering, and even code generation.

Mathematically, the prompt for an n-shot task can be represented as:

$$
\text{Prompt} = \{ (x_1, y_1), (x_2, y_2), \dots, (x_n, y_n) \} \cup \{ x_{\text{query}} \}
$$

Here, each $ (x_i, y_i) $ is an example pair demonstrating the task, and $ x_{\text{query}} $ is the new input for which the model is expected to generate a corresponding output $ y_{\text{query}} $.

## Implementation

Below is a simple Python example demonstrating how to construct an n-shot prompt for a translation task using a language model API (e.g. GPT-3 `text-davinci-003` is set as the default model to query). This example aggregates several examples into a single prompt that is then sent to the model for completion.

```python
import openai

def generate_response(prompt_examples, query, engine="text-davinci-003"):
    """
    Constructs an n-shot prompt and generates a response from a language model.
    
    :param prompt_examples: A list of dictionaries with 'input' and 'output' keys.
    :param query: The new input prompt for which an output is expected.
    :param engine: The language model engine to use.
    :return: The model-generated output as a string.
    """
    prompt = ""
    for ex in prompt_examples:
        prompt += f"Input: {ex['input']}\nOutput: {ex['output']}\n\n"
    prompt += f"Input: {query}\nOutput:"
    
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Example usage:
examples = [
    {"input": "Translate 'Hello' to Spanish", "output": "Hola"},
    {"input": "Translate 'Goodbye' to Spanish", "output": "Adiós"},
]
query = "Translate 'Thank you' to Spanish"
print(generate_response(examples, query))
```

In this example, the prompt is constructed by concatenating each example pair followed by the new query. The model then generates a response based on the patterns learned from the provided examples.

## Use in Generative Evaluations

n-shot prompting is a powerful tool not only for task execution but also for [evaluating the performance](../../evaluation/) of generative models. By varying the number of examples provided, we can study how models adapt to new tasks and assess the robustness of their in-context learning capabilities.