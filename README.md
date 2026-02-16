### Assignment #3 Reflections

This project implements a complete GPT-style transformer in PyTorch from scratch. All major components were built manually: Layer Normalization, GELU activation, Feed-Forward Networks, multi-head self-attention with causal masking, stacked Transformer blocks with residual connections, and full GPT model assembly. Exercises 4.1 (small and medium GPT variants) and 4.4 (parameter counts and memory usage) were completed.

**Core Architecture**
Token embeddings convert discrete tokens into dense vectors. Positional embeddings inject sequence order information—without them, the model couldn't distinguish different orderings of the same words.
Multi-head self-attention lets each token attend to previous tokens through causal masking, preserving autoregressive behavior. Multiple heads capture different patterns in parallel—some syntactic, some semantic.

**Implementation Details**
Custom Layer Normalization matched PyTorch's implementation within ~1.2×10⁻⁷, confirming correctness. Pre-norm placement improves gradient flow in deep networks.
GELU activation was implemented using standard approximation (max difference ~0.00047 vs PyTorch). Compared to ReLU's sharp cutoff, GELU allows small negative contributions for smoother behavior.
The FFN expands hidden dimensions 4×, applies GELU, then projects back. Residual connections preserve gradient flow, enabling scaling from 6 to 12 layers without instability.

**Model Configurations**
Small model: 6 layers, 384 hidden size, 6 heads → 11.4M parameters (~45.8 MB)
Medium model: 12 layers, 768 hidden size, 12 heads → 86.6M parameters (~346.6 MB)
Training with Adam requires ~4× parameter memory due to gradients and optimizer states, meaning the medium model needs ~1.38 GB during training.
Untrained text generation produced incoherent output as expected, but confirmed the forward pass, causal masking, and autoregressive generation were working correctly.