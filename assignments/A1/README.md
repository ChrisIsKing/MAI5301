### Assignment Writeup
#### 1. How BPE differs from simpler tokenization approaches
Simplier tokenization approaches use vocabulary lists to create mappings for each word input. If an inputted text doesn't exist in a vocabulary list, BPE breaks the word down into a sequence of subwords or letters, enabling tokenization.

#### 2. Why sliding windows are used for language modeling
Sliding windows handle long sequences of text by chunking them into a manageable size that the model can process.

#### 3. Any challenges you encountered with batching
Unclear