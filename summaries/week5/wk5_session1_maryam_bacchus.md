####Problem Addressed and Problem Importance
The main question asked was: How can we scale up language models while lowering computational intensity? This was an important question because larger and dense models consistently showed better performance however, they were extermely expensive and required more memory and processing power. Companies wanted a way to achieve the benefits of dense models with large parameter counts while making deployment and usage practical and profitable. This is where the switch transformer architecture and mixture of experts concept tries to solve.

####State of Related Works in This Topic
At the time these papers were published, the approach was scaling up dense transformer models by increasing model size and computational budget. Models like GPT-3, T5 had proven that bigger models performed better. The Mixture of Experts concept dated back to the early 1990s, but MoE had some challenges including algorithmic complexity in routing mechanisms, high communication costs between experts distributed across devices, and training instabilities. These made them difficult to work with at very large scale.

####Proposed Solution
In "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity", researchers at Google improved the MoE architecture by proposing a simplified routing mechanism that sends each input token to just a single expert (k=1) rather than combining multiple experts. This approach reduced routing computation.

In "Mixtral of Experts", Mistral AI built upon sparse MoE concepts but took a different routing mechanism approach than Switch Transformers. They used top-2 routing (k=2) instead of top-1 (k=1) approach. This routed each token to two experts instead of one. The mistral model outperformed Llama 2 70B while using only 13B active parameters per token out of 47B total.

####Drawbacks and Limitations
For Switch Transformers, the largest models, Switch-XXL experienced training instabilities requiring special handling. For all MoE models, it requires all expert parameters to be loaded in memory for deployment. This uses a significant amount of VRAM and is still computationally expensive.

####Future Research
From Switch Transformers, researchers suggested further research into stabilization for large models, exploring distillation of large sparse models into smaller dense models, and investigating model sparsity in new modalities. From Mixtral, the researchers mentioned exploring more elaborate gating strategies for expert selection as future work.
