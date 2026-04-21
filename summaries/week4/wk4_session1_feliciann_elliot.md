### Problem Addressed and Problem Importance

There exists many models that are private within companies which have been trained on data that researchers and students are unable to access and review for further research and critique. This case also prevents researchers from fully being able to study the models and/or test their limits (Touvron et al., 2023). For machine learning researchers and students, this a big issue if these models are shaping so much of what people build and use. 

The paper also points out that previous research has shined more light on training big models rather than investing attention to how expensive they are on computer hardware to run after they are trained. 

In practical circumstance, the inference costs of these models matter, especially if researchers expect the model to perform multiple inference requests in parallel (Touvron et al., 2023). The authors argue that a smaller model trained on more data can have a better efficiency application overall. Making these models more open and efficient matters because it lets more people experiment with them and answer questions about the model's bias, safety, and reliability (Touvron et al., 2023).

### State of Related Works in This Topic

Before the advent of LLaMA, the main trend in large language models was basically “bigger is better.” Models like GPT-3, Gopher, and PaLM showed that if you increase the number of parameters, performance usually goes up as well (Touvron et al., 2023). The problem observed by researchers was that most of these models were closed-source, so future researchers were only able to observe the output of its operation and not the full breakdown of the model's structure. There were some open models like OPT, GPT-NeoX, and BLOOM, but they still did not quite reach the same level as the top proprietary ones (Touvron et al., 2023).

What really changes the conversation is the newer work on scaling laws, especially the Chinchilla results. These showed that models were often too big for the amount of data they were trained on, and that training smaller models on more tokens could be more efficient (Touvron et al., 2023). Additionally, instruction tuning became popular since it made the models follow human instructions better, like what was seen with Flan-PaLM and OPT-IML. These developments had later set the stage for the development of LLaMA which took a different balance instead of just chasing size (Touvron et al., 2023).

### Proposed Solution

The solution proposed in the paper is LLaMA, which is a set of models ranging from 7B to 65B parameters, all trained only on publicly available data so that they can be shared with the machine learning research community (Touvron et al., 2023). A notable development within LLaMA was that the researchers had structured it in such a way where instead of making the model huge, they trained it on a massive number of tokens. For example, the 7B model alone was trained on about one trillion tokens, which is significant than may be expected for a model that size (Touvron et al., 2023).

They also made some technical changes to the Transformer setup, like using pre-normalization, SwiGLU activations, and rotary positional embeddings, mostly to improve stability and performance (Touvron et al., 2023). The results show that the 13B LLaMA model outperforms GPT-3 on many benchmarks, while the 65B variant achieves performance comparable to larger models such as Chinchilla and PaLM, indicating the effectiveness of the proposed training strategy (Touvron et al., 2023).

### Drawbacks and Limitations

Even though the results look great, the paper does not pretend the model is perfect. LLaMA still shows the usual problems we see in large language models, especially bias and toxicity (Touvron et al., 2023). In fact, the toxicity scores get worse as the model gets larger, which is not very comforting. Tests like RealToxicityPrompts and WinoGender show biases related to gender, religion, and age, which means the model is still picking up stereotypes from its training data (Touvron et al., 2023).

Another issue within LLaMA the way of its hallucination. Even though LLaMA expresses significant performance and efficient than GPT-3 on TruthfulQA, it still gets a lot of answers wrong, which means you cannot fully trust it without verifying the model's output (Touvron et al., 2023). The model also performs slightly worse than Chinchilla and PaLM on MMLU, and the authors suggest this might be because the training data had fewer books and academic papers (Touvron et al., 2023). So while the model is efficient, there are clear trade-offs.

### Future Research

For future work, the authors plan to focus on reducing bias and toxicity and making the model more robust overall (Touvron et al., 2023). They already tested an instruction-tuned version called LLaMA-I, and it showed better results on some benchmarks like MMLU, which suggests this is a good direction to keep exploring (Touvron et al., 2023).

They also mention scaling even further with more data and possibly larger models, since performance kept improving as they increased scale (Touvron et al., 2023). From a student perspective, I think the most exciting part is the idea of democratizing access. If more strong models are available to researchers and learners, it makes it easier for people like us to experiment, break things, and actually understand how these systems behave instead of just reading about them.

### References

Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M., Lacroix, T., Rozière, B., Goyal, N., Hambro, E., Azhar, F., Rodriguez, A., Joulin, A., Grave, E., & Lample, G. (2023, February 27). LLaMA: Open and efficient foundation language models. arXiv. https://arxiv.org/abs/2302.13971