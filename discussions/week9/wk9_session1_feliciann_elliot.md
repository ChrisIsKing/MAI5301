### Problem Addressed and Problem Importance

This paper looks at a simple but important issue: large language models often fail on tasks that require multi-step reasoning, even when they have enough knowledge to solve them. On tasks like math word problems or logical reasoning, models would jump straight to an answer and make mistakes, rather than working through the problem step by step (Wei et al., 2022).

This matters because many real-world applications require reasoning rather than surface-level pattern matching. If models cannot reliably break problems into intermediate steps, their usefulness is limited, regardless of how large they are. Understanding how to elicit reasoning from existing models without retraining opens the door to better performance at almost no additional cost.

### State of Related Works in This Topic

Before this work, prompting techniques focused mostly on providing clearer instructions or examples. While few-shot prompting improved performance, it did not consistently help with tasks that required intermediate reasoning. Models were still expected to implicitly “figure out” the reasoning process internally, which often failed on more complex problems (Wei et al., 2022).

At the same time, scaling studies had shown that larger models performed better overall, but it was unclear whether they were actually reasoning or just memorizing patterns from data.

### Proposed Solution

Wei et al. introduce chain-of-thought prompting, a simple technique where the model is encouraged to generate intermediate reasoning steps before giving a final answer. Instead of showing only input-output examples, prompts include step-by-step explanations demonstrating how a problem is solved (Wei et al., 2022).

The results show that sufficiently large models can follow this structure and produce their own reasoning chains at inference time. This leads to large improvements on arithmetic, symbolic, and commonsense reasoning tasks. Importantly, the model is not retrained. It is simply guided through the prompt to reveal reasoning it already has.

### Drawbacks and Limitations

Chain-of-thought prompting works primarily for large models and provides little benefit for smaller ones. The approach also increases output length, which raises inference cost. Additionally, the reasoning steps are not guaranteed to be correct, and the model may still arrive at a wrong answer through a plausible-looking explanation (Wei et al., 2022).

### Future Research

Future work includes developing better ways to control and verify reasoning steps, as well as understanding why chain-of-thought prompting emerges only at certain model scales. There is also interest in applying the technique beyond text, such as in multimodal or planning tasks (Wei et al., 2022).

### References
Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022, January 28). Chain-of-Thought prompting elicits reasoning in large language models. arXiv.org. https://arxiv.org/abs/2201.11903
