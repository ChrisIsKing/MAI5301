Why causal masking is necessary for language models:
Causal masking prevents a token from attending to future tokens during training. This enforces the autoregressive property of language models, ensuring predictions for the next token depend only on past and current tokens, not information that would not be available at inference time.

The purpose of multiple attention heads:
Multiple attention heads allow the model to attend to different types of relationships in parallel (e.g., syntax, long-range dependencies, or local context). Each head learns a different projection of the input, increasing the model’s expressive power without significantly increasing sequence length or depth.

How attention weights reveal the model’s focus:
Attention weights show how strongly each token attends to others in the sequence. By inspecting these weights, we can see which tokens the model considers most relevant when generating representations, offering interpretability into patterns like dependency tracking or positional focus.