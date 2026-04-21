### Problem Addressed and Problem Importance

The papers by Brown et al. (2020) and Wei et al. (2022) focus on understanding what large language models are capable of doing as they grow in size, particularly without task-specific fine-tuning. Both works explore whether a single, general-purpose model can perform many different tasks simply by being prompted with examples or instructions.

This question is important because fine-tuning models for every task is expensive and often impractical. It requires large labeled datasets and additional training for each new use case. If models can instead learn to perform tasks directly from context, organizations can save time, reduce costs, and deploy models more flexibly. Understanding when and how these abilities appear also helps researchers better anticipate the strengths and limitations of large models, which can provide a competitive advantage in real-world applications (Brown et al., 2020; Wei et al., 2022).

### State of Related Works in This Topic

Prior to these research papers, most natural language processing systems relied on task-specific training. Even with the rise of Transformer models, performance still depended heavily on fine-tuning with labeled datasets for each task. While Transformers were more flexible than earlier architectures like RNNs, they were not truly general-purpose in practice.

At the same time, earlier research on scaling laws showed that model performance improved predictably as models became larger. However, these studies focused mainly on gradual improvements in metrics such as loss and accuracy. What remained unclear was whether entirely new capabilities could appear at large scales, rather than simply better versions of existing behavior. Brown et al. (2020) and Wei et al. (2022) address this gap by examining qualitative changes in model behavior as scale increases.

### Proposed Solution

In Language Models Are Few-Shot Learners, Brown et al. (2020) demonstrate that large language models can perform tasks using only information provided in the input prompt. They introduce in-context learning, where the model is given task instructions and a small number of examples directly in text. To test this idea, they evaluate GPT-3, a 175-billion-parameter model, using zero-shot, one-shot, and few-shot settings. The results show that with enough examples in the prompt, the model can recognize patterns and perform tasks reasonably well without any changes to its weights.

Wei et al. (2022) build on this idea by formally studying what they call emergent abilities. They define an ability as emergent if it does not appear in smaller models but suddenly appears in much larger ones. Their analysis shows that for many tasks, performance remains close to random until a certain scale is reached, after which accuracy increases sharply. This behavior cannot be predicted by simply extrapolating from smaller models. Together, the two papers show that scale does not just improve performance gradually, but can unlock entirely new capabilities that were previously absent (Brown et al., 2020; Wei et al., 2022).

### Drawbacks and Limitations

One limitation of in-context learning is that it depends heavily on the model’s context window. The amount of information a model can use is constrained by hardware limits, such as the size of the key-value cache. When prompts become too long or include unrelated examples, model performance can degrade and hallucinations may occur (Brown et al., 2020).

Additionally, despite their strong language abilities, large models like GPT-3 still struggle with certain tasks, such as arithmetic and precise reasoning. Wei et al. (2022) also note that emergent abilities are unpredictable, which makes them difficult to plan for or guarantee. Since these abilities appear suddenly at certain scales, it is hard to know in advance when a new capability will emerge or whether scaling alone is sufficient to achieve it.

### Future Research

Both papers suggest that emergence may not be tied strictly to model size. Wei et al. (2022) argue that improvements in data quality, training methods, or model architecture could allow emergent abilities to appear at smaller scales. Future research should focus on identifying the conditions that trigger these abilities and determining whether they can be made more predictable.

There is also a need to better understand how emergent abilities relate to real-world usefulness. While performance jumps are impressive, future work should examine how these capabilities translate to reliability, reasoning, and safety in deployed systems. Improving our understanding of emergence could help guide the design of more capable and efficient models without relying solely on increasing scale (Brown et al., 2020; Wei et al., 2022).

### References

Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D. M., Wu, J., Winter, C., . . . Amodei, D. (2020, May 28). Language Models are Few-Shot Learners. arXiv.org. https://arxiv.org/abs/2005.14165

Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Borgeaud, S., Yogatama, D., Bosma, M., Zhou, D., Metzler, D., Chi, E. H., Hashimoto, T., Vinyals, O., Liang, P., Dean, J., & Fedus, W. (2022, June 15). Emergent abilities of large language models. arXiv.org. https://arxiv.org/abs/2206.07682

