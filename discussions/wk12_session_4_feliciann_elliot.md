### Problem Addressed and Problem Importance

Building generally capable embodied agents that continuously explore plan and develop new skills in open ended worlds remains a grand challenge. Classical reinforcement learning and imitation methods operate on primitive actions while existing large language model agents generate plans but lack lifelong learning to acquire update accumulate and transfer knowledge over extended periods.

### State of Related Works in This Topic

Prior Minecraft agents use low level controllers with hierarchical reinforcement learning from demonstrations or high level planners that decompose tasks via fixed recipes. General large language model agents apply chain of thought or self reflection for text tasks but lack mechanisms for open ended exploration skill accumulation or executable code as temporally extended actions.

### Proposed Solution

The authors present Voyager the first large language model powered embodied lifelong learning agent in Minecraft. It comprises three components an automatic curriculum that proposes tasks based on current state and exploration progress a skill library that stores verified executable programs indexed by description embeddings for retrieval and composition and an iterative prompting mechanism that refines code using environment feedback execution errors and self verification until success. Voyager interacts with GPT 4 via black box queries without parameter fine tuning and uses Mineflayer JavaScript APIs for control.

### Drawbacks and Limitations

The GPT 4 API incurs high cost and is 15 times more expensive than GPT 3.5. Despite iteration the agent occasionally gets stuck or generates incorrect skills. The curriculum sometimes proposes unachievable tasks and hallucinations occur during code generation such as invalid function calls or fuel sources. Self verification can miss subtle success signals.

### Future Research

Voyager can be augmented with multimodal perception models to support visual input and more complex 3D construction. Extensions to robotics require additional safety constraints. Improvements in GPT API quality and techniques for fine tuning open source models will address current limitations in accuracy and cost.

### References
Wang, G., Xie, Y., Jiang, Y., Mandlekar, A., Xiao, C., Zhu, Y., Fan, L., & Anandkumar, A. (2023, May 25). Voyager: An Open-Ended Embodied Agent with Large Language Models. arXiv.org. https://arxiv.org/abs/2305.16291