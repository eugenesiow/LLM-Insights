# Chain-of-Thought (CoT) Prompting

> **Chain-of-Thought Prompting** encourages language models to generate intermediate reasoning steps before arriving at a final answer. This technique helps models break down complex problems into manageable sub-steps, improving performance on tasks that require multi-step reasoning.

Traditional prompting methods often ask models to produce a final answer directly. However, for tasks such as multi-step arithmetic, logical puzzles, or reasoning problems, this direct approach may lead to incomplete or erroneous answers. Chain-of-thought prompting addresses this by explicitly instructing the model to "think aloud" (i.e. "let's think step by step") — that is, to generate a sequence of intermediate steps or thoughts that lead up to the final conclusion.

Wei at al. (Jan 2022) found (while he was at Google Brain) and published in their seminal paper [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903), that chain-of-thought prompting works pretty well in practice and improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks. As Andrej Karpathy put so aptly "models (transformers) need tokens to think". Especially if your tasks require reasoning, you can't expect the transformer to do too much reasoning per token. And so, you have to really spread out the reasoning across more and more tokens.

Additionally, you can elicit this kind of behavior from the transformer by saying, let’s think step by step, because this conditions the transformer into showing its work. Because it kind of snaps into a mode of showing its work, it's going to do less computational work per token and hence is more likely to succeed as a result. It's making slower (or explicit it's) reasoning over time.

The process can be conceptually represented as:

$$
\text{Answer} = f\left(\text{Step}_1, \text{Step}_2, \dots, \text{Step}_m\right)
$$

where each \( \text{Step}_i \) is an intermediate reasoning step generated in sequence, and \( f \) is the function that compiles these steps into a final answer. By laying out the reasoning process, models can arrive at more accurate answers, as errors in one step can be identified and corrected in subsequent steps.

## Methods

### Zero-shot-CoT

Prompt:
```
Q: A juggler can juggle 16 balls. Half of the balls are golf balls, and half of the golf balls are blue. How many blue golf balls are there?

A: Let's think step by step.
```

Output:
```
There are 16 balls in total. Half of the balls are golf balls. That means that there are 8 golf balls. Half of the golf balls are blue. That means that there are 4 blue golf balls.
```

Note: You can see the [n-shot Prompting](nshot.md) for information on zero and few-shot prompting.

### Few-shot-CoT

Prompt:
```
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?

A: Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11.

Q: A juggler can juggle 16 balls. Half of the balls are golf balls, and half of the golf balls are blue. How many blue golf balls are there?

A:
```

Output:
```
The juggler can juggle 16 balls. Half of the balls are golf balls. So there are 16 / 2 = 8 golf balls. Half of the golf balls are blue. So there are 8 / 2 = 4 blue golf balls. The answer is 4.
```

Note: You can see the [n-shot Prompting](nshot.md) for information on zero and few-shot prompting.