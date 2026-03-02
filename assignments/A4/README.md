1. Training hyperparameters chosen and why
- AdamW Optimizer — standard for transformer pretraining
- Batch size of 2 - used due to limited by CPU/memory for 124M parameter model
- 256 tokens sequence length
- 15 eopchs
- Gradient clipping - max_norm=1.0 to prevent exploding gradients

2. How Loss Decreases During Training
- Training loss consistently decreased throughout the training process. Validation loss initially improved from approximately 7.1968 down to 6.1881. After this point, the validation loss began to increase, this may indicate overfitting.

3. Quality Improvement in Generated Text
- Epoch 1: Repeats common tokens "the the the the"
- Epoch 3-4: The model starts to mention character names and story structure from training data
- Epoch 5: Produces somewhat coherent responses
- Pretrained GPT-2: Generates fluent and relevant text on any prompt.

4. Challenges with training from scratch vs using pretrained weights
- Scratch model was trained ofr 1 hour on CPU while GPT-2 was trained on hundreds of GPU-hours
- Overfitting - val loss diverges from train loss quickly
- Scratch model only learns tokens present in training text, which was small and inadequate for any real geneeralization

### Compute Resources
- CPU 
- Google Colab
- 12GB RAM