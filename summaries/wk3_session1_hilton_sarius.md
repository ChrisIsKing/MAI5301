Summary of Two Papers on LLM Scaling
Kaplan et al. (2020): “Scaling Laws for Neural Language Models”
This paper looks at how the performance of language models change parameters, dataset size, and compute are scaled. It was found that test can be predicted by a power-law relationship with these factors, provided that one of these factors causes a bottleneck. This discovery was very important as it is very expensive to train large models. And establishing scaling laws enables us to better allocate resources and track/ forecast performance. We see that larger models are more sample-efficient, and architecture details (depth vs. width) matter less than overall scale. Therefore, for a fixed compute budget, it may be better to train very large models on reasonable sized data sets and stop before full convergence- stopped before convergence because of diminishing marginal returns is experience after a while.
Hoffmann et al. (2022): “Training Compute-Optimal Large Language Models” (Chinchilla)
This research paper builds on the first paper, it basically asks: Given a fixed compute budget, what is the optimal trade-off between model size and training tokens? It is argued that many large models (e.g., GPT-3) were undertrained relative to their size. Through experiments on 400+ models (70M–16B parameters, 5–500B tokens), they derive a rule: double tokens in similar proportions with parameters. Using this principle, they train Chinchilla (70B) with the same compute as Gopher (280B) but 4× more data, achieving superior performance across benchmarks, including state-of-the-art results on MMLU. This shifts the paradigm from “bigger models” to “balanced scaling” of size and data.

State of Related Work
Kaplan et al. redefined existing scaling laws and influenced the trend toward ever-larger models. This was done by introducing compute-optimal scaling, demonstrating that balanced training beats sheer size. Together, these works underpin modern LLM development strategies.

Key Insights
•	Kaplan et al.: Performance improves predictably with scale; larger models are more sample-efficient; architecture details are secondary.
•	Hoffmann et al.: Compute-optimal training requires scaling parameters and tokens together; smaller but well-trained models outperform larger undertrained ones.

Limitations
Kaplan’s laws rely on cross-entropy loss, which doesn’t fully capture real-world capabilities like reasoning or safety. Hoffmann’s rule assumes abundant high-quality data and applies mainly to dense autoregressive transformers; generality across architectures and objectives remains uncertain.

Future Directions
1.	Incorporate data quality and curriculum design into scaling laws.
2.	Develop capability-aware scaling for reasoning, alignment, and safety.
3.	Extend compute-optimal analysis to MoE, multimodal, and retrieval-augmented models.
4.	Integrate energy and carbon metrics for sustainable scaling.
5.	Study robustness under distribution shifts and domain transfer.

Integrated Takeaway
Kaplan provides a predictive map for scaling; Hoffmann refines it for compute-limited scenarios. Together, they shift practice from “bigger is better” to “balance is better,” emphasizing co-scaling of size, data, and compute for efficiency and performance.

Key observations from the class discussion
•	We revisited the concept of FLOPs – Floating Point Operations per second
•	Emphasized the effect of diminishing returns on Cross entropy loss after a certain threshold because as Maryam indicated in class; “the entropy of natural language is never zero”
•	We also spoke about how the research in AI is a iterative process and the way researchers build on existing work and making seemingly small improvements that then catapult the field into a whole new level of sophistication.



