### Problem Addressed and Problem Importance

Like speculative decoding, Medusa targets the sequential bottleneck of autoregressive generation. Even with large GPUs, decoding still happens token by token, limiting throughput. The challenge is to generate multiple tokens per forward pass without modifying the base model too heavily or retraining from scratch.

### State of Related Works in This Topic

Speculative decoding showed that multiple tokens could be generated per step using a separate approximation model. However, that approach requires maintaining two models and coordinating their interaction. Other acceleration methods either reduce model size or alter architecture in ways that complicate deployment. There was room for a simpler framework that worked directly on a single base model.

### Proposed Solution

Medusa adds multiple decoding heads to a pretrained model. Instead of predicting just the next token, the model predicts several future tokens at different offsets in parallel (Cai et al., 2024). During inference, these extra heads generate candidate token sequences, and a verification mechanism determines which tokens are valid. In effect, Medusa performs multi-token decoding in a way similar to speculative decoding, but without needing a separate approximation model.

A key advantage is simplicity. The base model remains mostly unchanged, and the added heads can be trained efficiently. The framework achieves meaningful speedups while maintaining high output quality.

### Drawbacks and Limitations

Medusa requires additional training to learn the auxiliary decoding heads. Unlike speculative decoding, which can work with off-the-shelf models, Medusa involves modifying and fine-tuning the model. Its gains also depend on how accurately the extra heads predict future tokens. If predictions are frequently rejected, speed improvements diminish.

### Future Research

Future work could explore combining Medusa with other inference optimizations such as KV-cache management or Flash-style attention kernels. There is also room to analyze how multiple decoding heads interact with scaling and whether deeper speculative hierarchies can push speed further (Cai et al., 2024).

Understanding when multi-token decoding works best across tasks and model sizes remains an open question.

### References
Cai, T., Li, Y., Geng, Z., Peng, H., Lee, J. D., Chen, D., & Dao, T. (2024, January 19). Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads. arXiv.org. https://arxiv.org/abs/2401.10774