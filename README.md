### Assignment #2 Reflections

In Exercise 3.1, we observed that changing the number of attention heads mainly affected how the multi-head attention module divided information internally, while the final output representation remained largely unchanged. 

The results from Exercise 3.2, demonstrated how masking consistently enforced the autoregressive constraint, as attention to future tokens was completely blocked regardless of text type. The attention visualizations also showed that, because the weights were untrained, the model’s focus appeared largely random, highlighting that meaningful attention patterns only emerge after training.