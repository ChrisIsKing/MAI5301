#### 1. Why causal masking is necessary for language models
Casual masking is necessary to ensure that attention on attends to the next token in the sequence and not any token ahead or before.

#### 2. The purpose of multiple attention heads
Multi-head attention allows the model to learn different types of relationships in the input, better than single attention head, because each attention head focuses on different parts of the input. 

#### 3. How attention weights reveal model's focus
Attention weights which words (tokens) are closely related to each other.