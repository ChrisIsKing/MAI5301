### Problem Addressed and Problem Importance

Autoregressive decoding is slow by design. To generate K tokens, a Transformer must run forward passes K times, one after the other. Even if the model is massively parallel inside each step, the steps themselves are sequential (Leviathan et al., 2022). That serial dependency becomes a major bottleneck for large models.

This is important because inference cost now dominates many real-world deployments. Training happens once, but decoding happens millions of times. Any method that speeds up inference without retraining or changing outputs has immediate practical value.

### State of Related Works in This Topic

Prior approaches to speeding up inference generally fell into two categories. Some reduced model size or precision through distillation or quantization. Others used adaptive computation, where the model dynamically chooses how much compute to spend per token (Leviathan et al., 2022).

The issue with many of those methods is that they either require retraining, change the architecture, or modify the output distribution. That makes them harder to deploy in systems that need identical outputs. There were also earlier attempts at decoding multiple tokens in parallel, but most only supported greedy decoding and did not extend cleanly to stochastic sampling.

### Proposed Solution

The authors introduce speculative decoding, inspired by speculative execution in computer processors. The idea is to use a smaller, faster approximation model to “guess” several future tokens, and then have the large target model verify them in parallel (Leviathan et al., 2022). 

If the guesses are consistent with the target model’s distribution, they are accepted. If not, corrections are made using a carefully adjusted sampling method called speculative sampling. The key result is that this process preserves the exact output distribution of the original large model.

Algorithm 1 in Section 2.3 shows how multiple candidate tokens are sampled from the smaller model and then validated by the larger one in parallel. The paper formally proves that the final token distribution remains identical to standard decoding. Empirically, they demonstrate 2×–3× speedups on models like T5-XXL without changing outputs. That is significant because it improves latency without retraining or architectural modification.

### Drawbacks and Limitations

Speculative decoding increases concurrency but can increase the total number of arithmetic operations. The speedup assumes available compute resources and is most beneficial when memory bandwidth is the bottleneck (Leviathan et al., 2022). Its effectiveness also depends on how well the smaller approximation model matches the larger one. If their distributions diverge too much, the acceptance rate drops and the benefit shrinks.

### Future Research

The paper suggests optimizing the choice of the approximation model and dynamically adjusting how many speculative tokens are generated. There is also room to explore hierarchical speculation, where multiple approximation models operate at different levels (Leviathan et al., 2022). More broadly, the idea of stochastic speculative execution could extend beyond language modeling into other probabilistic systems.

### References
Leviathan, Y., Kalman, M., & Matias, Y. (2022, November 30). Fast Inference from Transformers via Speculative Decoding. arXiv.org. https://arxiv.org/abs/2211.17192