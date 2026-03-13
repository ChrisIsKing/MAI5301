### Problem Addressed and Problem Importance

Current benchmarks for digital agents are either non-executable (static demonstrations) or confined to narrow domains (web-only, single-app simulations), failing to capture the diversity, long-horizon nature, and cross-application workflows of real-world computer use. A scalable, real-computer environment with execution-based evaluation is essential to measure progress toward generalist agents that can truly assist humans across operating systems and arbitrary software.

### State of Related Works in This Topic

Prior datasets like Mind2Web, WebArena, and MiniWoB++ provide demonstrations or restricted web/mobile environments but lack interactive execution, cross-app support, or reliable functional correctness checks. They penalize valid alternative solutions and offer no support for intermediate initial states or free exploration. Existing agent frameworks (AutoGPT-style) are tested only in toy settings, leaving a gap for realistic, open-domain computer tasks.

### Proposed Solution

The authors present OSWorld, the first executable real-computer environment running on Ubuntu, Windows, and macOS via virtual machines. It supports raw mouse/keyboard actions, screenshots + accessibility trees, task initialization from intermediate states, and custom execution-based evaluation scripts. Built on this, they release a benchmark of 369 Ubuntu tasks (plus 43 Windows) spanning OS basics, office suites, daily apps, professional tools, and multi-app workflows. Each example includes natural-language instructions, reproducible setup configs, and example-specific evaluation functions—134 unique ones in total—for functional correctness rather than surface-form matching.

### Drawbacks and Limitations

Current SOTA agents (GPT-4V, Gemini-Pro-1.5, Claude-3-Opus, etc.) achieve only 0.99–12.24 % success (vs. human 72.36 %), struggling with GUI grounding, repetitive actions, noise from unexpected windows, and basic operational knowledge. Higher-resolution screenshots and longer history help but strain context limits. The benchmark focuses on Ubuntu for scalability; Windows/macOS examples are smaller due to licensing.

### Future Research

Prioritize VLM improvements in high-resolution grounding and coordinate prediction. Integrate memory, reflection, and exploration mechanisms to handle long-horizon multi-app workflows. Expand to more OSes, add dynamic real-time evaluation functions, and explore interactive learning within the environment. The open-sourced code, VMs, and 134 evaluation scripts enable rapid iteration toward capable generalist computer agents.

### References
Xie, T., Zhang, D., Chen, J., Li, X., Zhao, S., Cao, R., Hua, T. J., Cheng, Z., Shin, D., Lei, F., Liu, Y., Xu, Y., Zhou, S., Savarese, S., Xiong, C., Zhong, V., & Yu, T. (2024, April 11). OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments. arXiv.org. https://arxiv.org/abs/2404.07972