### Assignment #4 Reflections

This assignment implemented and trained a GPT-style language model from scratch using next-token prediction. The full pipeline included loss computation, training and validation tracking, learning rate scheduling (warmup + cosine decay), text generation with different sampling strategies, checkpointing, and comparison with a pretrained GPT-2 model.

## Training Setup and Hyperparameters

The model was trained with a context length of 128 tokens (CTX_LEN=128). Data loading used BATCH_SIZE=32, and gradient accumulation was enabled with grad_accum_steps=4 to increase the effective batch size without exceeding Tesla T4 GPU memory limits. AdamW was used as the optimizer with a base learning rate of 3e-4. A learning rate schedule combining linear warmup and cosine decay was implemented to stabilize early training and smooth later updates.

Training ran for approximately 47 minutes before stopping at:

- Epoch 2  
- Step 14,000  
- Training Loss: 0.5597  
- Validation Loss: 8.4455  
- Validation Perplexity: 4654.07  

Although the original target was longer training, the recorded run still demonstrates measurable learning progress.

## Loss Behavior

During training, the training loss decreased significantly from its initial high value, indicating that the model learned token-level structure and local dependencies within the dataset.

However, validation loss remained high compared to training loss. This suggests:

- Limited generalization due to small dataset size  
- Overfitting tendencies  
- Insufficient training duration for broader convergence  

Perplexity followed the same trend as validation loss, remaining relatively high, which reflects uncertainty in predictions on unseen data.

## Generated Text Quality

Text generation after training showed clear improvement compared to random initialization. The trained model was able to:

- Produce grammatically structured sentences  
- Reflect stylistic patterns of the training dataset  
- Maintain short-range coherence  

Different decoding strategies showed expected behavior:

- Greedy decoding resulted in repetitive loops.  
- Temperature + top-k sampling improved diversity.  
- Temperature + top-p sampling produced the most balanced outputs.  

This demonstrates that both training and decoding strategy affect output quality.

## Scratch Training vs Pretrained GPT-2

A comparison was conducted using the same prompt and sampling settings for both the scratch-trained model and GPT-2.

The scratch-trained model showed dataset-specific learning but lacked strong long-range coherence and semantic depth. In contrast, GPT-2 produced:

- More consistent narrative flow  
- Stronger contextual understanding  
- Broader vocabulary and general knowledge  

While training from scratch demonstrates model mechanics and optimization behavior, pretrained models significantly outperform small scratch-trained models in fluency and generalization.

## Limitations
A limitation of this implementation is the use of a simple regex-based word/punctuation tokenizer rather than a subword tokenizer (e.g., BPE as used in GPT-2). This can increase vocabulary sparsity and reduce generalization, contributing to higher validation loss and perplexity.

## Compute Resources

- GPU: Tesla T4 (15GB VRAM)  
- Framework: PyTorch  
- Training Duration: ~47 minutes  
- Dataset: Tiny Shakespeare - Retrieved from https://github.com/karpathy/char-rnn/tree/master/data/tinyshakespeare