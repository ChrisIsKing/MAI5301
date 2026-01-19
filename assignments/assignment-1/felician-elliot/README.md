### How BPE differs from simpler tokenization approaches

A simple word-level tokenizer splits text into full words and punctuation. This is easy to implement, but it struggles with unseen or rare words, which must be replaced with an <unk> token. As a result, some information is lost when the model encounters new vocabulary.

BPE tokenization works at the subword level. Instead of relying on full words, it breaks text into smaller pieces that can be recombined to represent almost any word. In my comparison, BPE produced more granular tokens than the simple tokenizer, but it avoided unknown tokens entirely. This makes BPE more flexible and better suited for real-world language modeling.

### Why sliding windows are used for language modeling

Language models cannot process very long text sequences at once. Sliding windows solve this by breaking a long token stream into many fixed-length input sequences. Each input window is paired with a target sequence that is shifted by one token, allowing the model to learn next-token prediction.

This approach makes training manageable in terms of memory while still allowing the model to learn from long text through overlapping contexts.

### Challenges encountered with batching

Batching requires all sequences to have the same length, which is not naturally the case with text data. Using sliding windows ensured consistent sequence lengths so batching could work correctly.

Another challenge was managing execution order in the notebook. Some cells depended on variables, such as the tokenizer, being defined earlier. Making key cells self-contained helped prevent runtime errors and ensured the notebook could be run from top to bottom without issues.