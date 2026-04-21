TRAIN SHORT, TEST LONG: ATTENTION WITH LINEAR BIASES ENABLES INPUT LENGTH EXTRAPOLATION

Attention with Linear Biases Enables Input Length Extrapolation examines a key limitation of transformer language models: they usually fail to generalize well to longer input sequences than what they were trained on. The authors show that this limitation is mainly caused by the way positional information is added to models, and they set out to find a simpler method that lets a transformer trained on short sequences work well on much longer ones during inference.

Their main contribution is Attention with Linear Biases (ALiBi), which changes how attention scores are computed in the transformer. Instead of adding learned or sinusoidal position embeddings to token inputs, ALiBi adds a bias to the query-key attention scores that increases linearly with distance between tokens. This encourages the model to prefer recent context without needing extra parameters.

Methodology wise, they train large language models with ALiBi on WikiText-103 and compare performance when testing on much longer sequences than those seen in training. The results are strong: a 1.3 billion parameter model trained on 1024 tokens with ALiBi matches the perplexity of a model trained on 2048 tokens using traditional position embeddings, while using less memory and training faster.

Overall, the goals of the paper were accomplished. The method is simple, efficient, and improves length extrapolation, which is an important problem for making transformer models more flexible.