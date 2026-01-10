### Problem Addressed and Problem Importance

The core problem addressed in both papers is how to best use a limited compute budget when training large language models. Specifically, researchers wanted to understand how to balance model size and the number of training tokens so that performance improves as much as possible for a fixed amount of FLOPs. This question is important because training large language models is extremely expensive, and for most organizations, models can only be trained once due to cost and resource limits.

Without clear guidance, companies risk wasting compute by either training models that are too large for the amount of data they see or by overtraining smaller models that cannot benefit from additional data. Understanding how to allocate compute efficiently allows researchers and organizations to make better cost-saving decisions while still achieving strong performance.

### State of Related Works in This Topic

At the time these papers were written, several large language models had already shown impressive results across many tasks. However, their training required massive amounts of compute and energy. As models grew larger, training costs increased rapidly, making inefficient training strategies increasingly problematic.

Earlier work explored how model size or data size affected performance, but there was no clear framework explaining how these factors should be balanced together under a fixed compute budget. Researchers lacked a practical rule for deciding whether additional compute should be spent on larger models or more training data. Both papers aim to address this gap by studying scaling behavior and providing guidance on how to allocate resources more effectively.

### Proposed Solution

In Scaling Laws for Neural Language Models, Kaplan et al. (2020) identify a predictable relationship between model size, dataset size, and compute. They show that performance improves smoothly as these factors scale and that, for compute-efficient training, most additional compute should be allocated to increasing model size rather than extending training indefinitely. Their results suggest that once loss stops improving, continuing to train on more data provides little benefit, and training should be stopped.

In contrast, Training Compute-Optimal Large Language Models by Hoffmann et al. (2022) revisits this trade-off and reaches a different conclusion. They argue that optimal training requires scaling model size and training tokens together at roughly the same rate. By mapping model size and token count directly to loss, they show that some earlier models, such as GPT-3, were undertrained. According to their findings, these models were too large for the amount of data they were trained on and would have benefited from seeing more tokens rather than increasing model size alone.

Together, the two papers provide complementary insights. Kaplan et al. emphasize the importance of scaling model size efficiently, while Hoffmann et al. demonstrate that sufficient training data is equally critical for achieving compute-optimal performance.

### Drawbacks and Limitations

One limitation of both approaches is their reliance on cross-entropy loss as the primary measure of success. As noted by Kaplan et al. (2020), it is unclear how much of the observed behavior is specific to natural language and how much applies more generally. Loss alone may not fully reflect performance on downstream tasks or real-world usefulness.

While Hoffmann et al. (2022) provide a more refined analysis by directly linking model size and token count to loss, their method still depends on the assumption that loss is the best indicator of model quality. Additionally, both studies are based on large-scale experiments that may not fully capture practical constraints such as data quality, domain differences, or deployment considerations.

### Future Research

Hoffmann et al. (2022) observe that scaling predictions derived from smaller models can differ from those based on larger ones, raising questions about how reliably scaling laws generalize across scales. Future research should examine whether conclusions drawn from smaller models remain valid as compute budgets grow.

Further work is also needed to explore whether these scaling strategies lead to meaningful improvements in downstream tasks rather than just lower loss values. Investigating alternative evaluation metrics and more efficient training methods could help refine compute-optimal strategies and improve the practical impact of scaling laws.

### References

Hoffmann, J., Borgeaud, S., Mensch, A., Buchatskaya, E., Cai, T., Rutherford, E., De Las Casas, D., Hendricks, L. A., Welbl, J., Clark, A., Hennigan, T., Noland, E., Millican, K., Van Den Driessche, G., Damoc, B., Guy, A., Osindero, S., Simonyan, K., Elsen, E., . . . Sifre, L. (2022, March 29). Training Compute-Optimal large language models. arXiv.org. https://arxiv.org/abs/2203.15556

Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J., & Amodei, D. (2020, January 23). Scaling laws for neural language models. arXiv. https://arxiv.org/abs/2001.08361