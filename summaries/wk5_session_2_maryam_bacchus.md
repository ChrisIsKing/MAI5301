###Longformer: The Long-Document Transformer

####Problem Addressed
The core problem is that self attention is quadratic (O(n²)) in sequence length. When processing a document, standard transformers compute attention scores between every pair of tokens, creating an n×n matrix. This becomes computationally prohibitive for long documents. The original BERT could only handle 512 tokens.
The problem matters because full attention assumes every token influences every other token, but in practice, if you're answering a question about a specific topic, you're attending to lots of tokens that aren't that influential.

####State of Related Works
The baseline was full self attention, which was phased out in modern transformers because it is too computationally expensive. At the time, PyTorch implementation made some optimizations in their transformer models, but hadn't implemented the sparse attention strategies the longformer paper proposed. 

####Proposed Solution and Key Insights
Longformer introduces several attention patterns to reduce complexity
- Sliding Window Local Attention - Instead of attending to all tokens, each token only attends to neighbors within a fixed window size W. This reduces complexity from O(n²) to O(n×W), which is linear since window size is constant
- Dilated Sliding Window - To increase the receptive field without expanding the window, they introduce gaps, stretching the coverage while keeping computation bounded.
- Global + Sliding Attention - Combines sliding window attention with global attention on special tokens, like the classification token. These global tokens attend to every token in the sequence, providing a mechanism for information to flow across the entire document.
The researchers showed that you can achieve linear scaling while maintaining or improving performance by being selective about which tokens attend to which other. This resulted in being more memory efficient than full attention, validated that full self-attention was not the only way to compute attention, and it enabled for larger context windows in transformer models.

####Drawbacks and Limitations
For tasks requiring global understanding like summarization, only looking within a local window (such as in sliding window attention) may cause loss of important information located elsewhere in the document. 

####Future Directions
Combining these sparse attention methods with other innovations, mixture of experts and hardware optimizations for greater gains.



###FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

Problem Addressed
Previous approaches like Longformer focused on reducing FLOPs. FlashAttention argues this misses the real bottleneck which I/O bound, not compute-bound. Standard attention moves the massive n×n attention matrix back and forth between HBM and compute cores, creating an I/O bottleneck. The real bottleneck therefore is the speed at which you can move data from GPU towards computing cores.

####State of Related Works
Longformer and sparse attention methods Focused on reducing operations by computing fewer attention scores and standard libaries like PyTorch didn't optimize for memory hierarchy awareness. These methods were being algorithmically smart and not necessarily being hardware smart.

####Proposed Solution and Key Insights
FlashAttention takes an IO-aware approach with the following proposed solutions
- Tiling which split the Q, K, V matrices into blocks that fit entirely in fast SRAM.
- Softfax scaling using statistics to compute sofmax scores over batches. This allows computing softmax incrementally without holding the entire row in memory.
- For the backward pass, standard approaches store the massive attention matrix. FlashAttention recalculates attention scores on the fly instead. Even though this means doing the computation twice, SRAM is so fast that recalculating is faster than reading from HBM.
These changes resulted in 15% faster training times for BERT models, increased context length, and memory efficiency. 

####Drawbacks and Limitations
Requires specific GPU models with adequate SRAM - which may be expensive.

####Future Directions
Combining IO awareness with sparse attention methods