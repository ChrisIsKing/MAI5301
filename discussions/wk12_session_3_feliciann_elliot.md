### Problem Addressed and Problem Importance

Language models are deployed in commercial products yet existing benchmarks have become saturated and fail to capture the frontier of what state of the art models can and cannot do. Real world software engineering serves as a rich sustainable and challenging testbed because fixing bugs or implementing features often requires navigating large repositories understanding interplay between functions across files and spotting errors in convoluted code.

### State of Related Works in This Topic

Prior coding benchmarks such as HumanEval focus on self contained problems solvable in a few lines of code. Extensions add languages or variations but still constrain scope to single functions or provide cloze style fill in blanks. Other work explores program repair or commit generation yet none present code context at repository scale with execution based verification on real user submitted issues and pull requests.

### Proposed Solution

The authors introduce SWE bench an evaluation framework with 2294 tasks drawn from real GitHub issues and merged pull requests across 12 popular Python repositories. A model receives an issue description and full codebase snapshot then generates a patch to edit the code. The revised codebase is tested against the repository unit and system tests where success requires all related fail to pass tests to change from fail to pass. They also release SWE bench train with 19000 instances for fine tuning plus two SWE Llama models based on CodeLlama. Evaluation uses BM25 retrieval or oracle files edited in the reference solution and reports percentage of resolved issues.

### Drawbacks and Limitations

Even the strongest model Claude 2 resolves only 1.96 percent of issues with BM25 retrieval. Performance drops with longer context because models struggle to localize problematic code amid irrelevant files. Generated patches are shorter simpler and edit fewer files than gold solutions. Finetuned open models suffer from distribution shift between oracle training context and sparse retrieval at test time.

### Future Research

The framework can be extended to additional programming languages and repositories for continual 
updates. Future work can explore agent based approaches tool augmentation and different retrieval or long context methods to improve repository scale editing.

### References
Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., & Narasimhan, K. (2023, October 10). SWE-Bench: Can language models resolve Real-World GitHub Issues? arXiv.org. https://arxiv.org/abs/2310.06770