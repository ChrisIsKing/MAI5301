### Problem Addressed and Problem Importance

Chollet challenges how artificial intelligence is defined and measured. The paper argues that current benchmarks often reward memorization and narrow skill rather than general intelligence. The central problem is that AI systems are evaluated based on task performance without considering how much prior knowledge was embedded during training (Chollet, 2019).

This matters because intelligence should reflect the ability to adapt to new problems efficiently. If a system only performs well because it has seen similar data before, it may not truly be intelligent in a general sense.

### State of Related Works in This Topic

AI evaluation traditionally relied on task-specific benchmarks. Success was measured by outperforming humans on predefined datasets. However, as models grew larger and were trained on massive corpora, they began performing well simply because of scale.

Chollet argues that this blurs the distinction between skill and intelligence. A system can achieve high performance by absorbing large amounts of data, but that does not necessarily mean it can generalize efficiently to novel situations.

### Proposed Solution

Chollet proposes a formal definition of intelligence based on skill-acquisition efficiency. Intelligence is defined as the ability to solve new tasks using limited prior knowledge and limited experience (Chollet, 2019). The more efficiently a system can generalize, the more intelligent it is.

To operationalize this idea, the paper introduces the ARC (Abstraction and Reasoning Corpus) benchmark. ARC tasks are designed to test abstract reasoning rather than pattern memorization. Each task provides a few input-output examples, and the system must infer the transformation rule.

The key insight is that intelligence should be measured relative to the amount of prior information available. Systems that require enormous training data to succeed should not automatically be considered more intelligent than systems that learn efficiently from small examples.

### Drawbacks and Limitations

One limitation is that defining and quantifying “prior knowledge” precisely is difficult. Measuring intelligence as skill-acquisition efficiency requires assumptions about what the system has already seen (Chollet, 2019).

Additionally, ARC tasks are intentionally abstract and may not reflect practical real-world tasks. High performance on ARC does not automatically translate into broad usability.

### Future Research

Future work includes refining definitions of general intelligence and designing benchmarks that better isolate reasoning ability from memorization. The broader contribution of the paper is conceptual rather than empirical. It pushes the field to rethink what intelligence means in the era of large-scale pretraining.