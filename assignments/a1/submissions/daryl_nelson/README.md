## How BPE Differs from Simpler Tokenization Approaches
Byte Pair Encoding (BPE) used in tiktoken creates subword tokens by merging frequent byte pairs, allowing it to handle out-of-vocabulary words and maintain efficiency. In contrast, simpler approaches like word-level tokenization (as in SimpleTokenizer) split on whitespace and punctuation, leading to larger vocabularies and unknown tokens for unseen words.

## Why Sliding Windows Are Used for Language Modeling
Sliding windows enable training on sequential data by creating overlapping context-target pairs from the token sequence. This allows the model to learn dependencies across the entire text while fitting data into fixed-size batches, essential for autoregressive tasks like next-token prediction.

## Challenges with Batching
Implementing batching required careful handling of stride, context length, and tensor shapes. Using LLMs to generate initial code, I iterated through the book section by section, debugging by printing tensor shapes and values to understand how batches form from sliding windows. Key issues included ensuring consistent sequence lengths and avoiding index errors when mixing different tokenizers.