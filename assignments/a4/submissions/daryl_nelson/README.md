Assignment 4: Pretraining a GPT-style LLM from Scratch

The notebook ran on cuda and printed GPU: NVIDIA GeForce RTX 3080 with GPU Memory: 10.74 GB. It printed the GPT configuration as vocab_size: 50257, context_length: 256, emb_dim: 768, n_heads: 12, n_layers: 12, drop_rate: 0.0, and qkv_bias: False. It also reported the model architecture as Total parameters: 162,419,712 with a float32 size of ~649.7 MB.

For the dataset and dataloaders, the notebook loaded text from the-verdict.txt and printed Total characters: 20,479 (training: 18,431, validation: 2,048) along with token counts (Training tokens: 4,612, Validation tokens: 534). The dataloader configuration printed Batch size: 2, Max length (context): 256 tokens, Stride: 256 tokens, Training batches: 9, and Validation batches: 1, and it printed sample batch shapes of torch.Size([2, 256]) for both input and target.

For loss and training-related outputs, the notebook’s loss sanity-check printed Sample batch loss: 11.0076 and Sample batch perplexity: 60328.95, together with (Random model should have loss ~10.82). After training, the notebook printed a loss analysis summary showing Initial training loss: 9.9715 decreasing to Final training loss: 0.1991, and Initial validation loss: 9.8264 decreasing to Final validation loss: 6.6397. It printed Best validation loss: 6.1058 (step 9), stated Model generalization is stable, and printed Final perplexity: 1.22. The checkpoint save/load test printed that the model was saved to trained_gpt_model.pt, then loaded again, and the verification losses matched exactly (Original model loss: 6.647982 and Loaded model loss: 6.647982, with Difference: 0.0000000000).

For text generation, the notebook’s text-generation test starting from Every effort printed a greedy sample and a temperature+top-k sample. The printed greedy output was: Every effort saves Bringing pasture incoriol hosted ._ corporations279 Burn issuer Kits Mortgage TTarianFree fair ACA BuiltIDES. The printed temperature + top-k output was: Every effortonent citizens victim Pau Taprir strandsalkingFriend famous breweriesvironaccoDev ethassed negatives MarrieduateSTD.

Finally, in Section 5.6 (pretrained weights), the notebook printed a GPT-2 124M Pretrained Config including context_length: 1024 and qkv_bias: True, then printed Loading GPT-2 via Hugging Face Transformers... followed by ✓ Pretrained GPT-2 loaded successfully!.

Files in this folder: assignment_4.ipynb, README.md, the-verdict.txt, trained_gpt_model.pt, training_loss_curves.png, lr_schedule.png
