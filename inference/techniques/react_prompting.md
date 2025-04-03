# ReAct Prompting

Yao et al. in their Oct 2022 paper, [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629), introduced a framework named ReAct (Reason + Act) where LLMs are used to generate both reasoning traces and task-specific actions in an interleaved manner.

Generating reasoning traces allow the model to induce, track, and update action plans, and even handle exceptions. The action step allows to interface with and gather information from external sources such as knowledge bases or environments.

The ReAct framework can allow LLMs to interact with external tools to retrieve additional information that leads to more reliable and factual responses.

Results show that ReAct can outperform several state-of-the-art baselines on language and decision-making tasks. ReAct also leads to improved human interpretability and trustworthiness of LLMs. Overall, the authors found that best approach uses ReAct combined with chain-of-thought (CoT) that allows use of both internal knowledge and external information obtained during reasoning.

## Methodology

ReAct is a general paradigm that combines reasoning (Re) and acting (Act) with LLMs. ReAct prompts LLMs to generate verbal reasoning traces and actions for a task. This allows the system to perform dynamic reasoning to create, maintain, and adjust plans for acting while also enabling interaction to external environments (e.g., Wikipedia) to incorporate additional information into the reasoning.

For example, we pass a question from HotpotQA (for brevity, excluded additional in-context examples in the prompt to teach the model to output the ReAct way):

```
Aside from the Apple Remote, what other devices can control the program Apple Remote was originally designed to interact with?
```

The snippet below shows an example generation from a model using ReAct and the different steps involved to perform question answering.

```
**Thought 1:** I need to search Apple Remote and find the program it was originally designed to interact with.  
**Act 1:** `Search[Apple Remote]`  
**Obs 1:** The Apple Remote is a remote control introduced in October 2005 by Apple … originally designed to control the **Front Row media center** program …  

**Thought 2:** Apple Remote was originally designed to control the Front Row media center program. I need to search **Front Row** next and find what other device can control it.  
**Act 2:** `Search[Front Row]`  
**Obs 2:** Could not find [Front Row]. Similar: ['Front Row Seat to Earth', 'Front Row Motorsports', '**Front Row (software)**', …]  

**Thought 3:** Front Row is not found. I need to search **Front Row (software)**.  
**Act 3:** `Search[Front Row (software)]`  
**Obs 3:** Front Row is a discontinued media center software …  

**Thought 4:** **Front Row (software) is controlled by an Apple Remote or the keyboard function keys.** So the answer is keyboard function keys.  
**Act 4:** `Finish[keyboard function keys]`
```

###  Prompt Exemplars 

```
**Question** What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
**Thought 1** I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
**Action 1** Search[Colorado orogeny]
**Observation 1** The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas.
**Thought 2** It does not mention the eastern sector. So I need to look up eastern sector.
**Action 2** Lookup[eastern sector]
**Observation 2** (Result 1 / 1) The eastern sector extends into the High Plains and is called the Central Plains orogeny.
**Thought 3** The eastern sector of Colorado orogeny extends into the High Plains. So I need to search High Plains and find its elevation range.
**Action 3** Search[High Plains]
**Observation 3** High Plains refers to one of two distinct land regions
**Thought 4** I need to instead search High Plains (United States).
**Action 4** Search[High Plains (United States)]
**Observation 4** The High Plains are a subregion of the Great Plains. From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130m).[3]
**Thought 5** High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
**Action 5** Finish[1,800 to 7,000 ft]
```

## Links

* Abstract: https://arxiv.org/abs/2210.03629
* Homepage: https://react-lm.github.io/