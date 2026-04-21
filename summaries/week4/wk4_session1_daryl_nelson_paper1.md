LLaMA: Open and Efficient Foundation Language Models

This paper addresses a very timely problem in large language models how to build powerful foundation models that don’t demand the huge compute and proprietary data typical of many state of the art systems. Rather than just chasing bigger and bigger parameter counts, the authors focus on training models with efficient use of data and compute so that even smaller architectures can perform competitively.

The research introduces a family of transformer-based language models ranging from 7B to 65B parameters, trained on about 1.4 trillion tokens drawn exclusively from publicly available datasets such as CommonCrawl, Wikipedia, GitHub, Books, and ArXiv. This emphasis on open data is one of the key motivations to make high-quality language models accessible to the wider research community without relying on proprietary corpora.

Methodologically, the authors make careful design choices in the transformer architecture like using rotary embeddings, SwiGLU activations, and efficient causal attention and training strategies that balance performance and computational cost. They show that smaller models trained on more data can outperform larger models under a fixed compute budget, which challenges the simple “bigger is better” narrative common in scaling laws.

In terms of results, LLaMA-13B notably outperforms GPT-3 on many benchmarks, while the 65B model is competitive with large models like PaLM and Chinchilla despite being trained only on public data.

Overall, the paper meets its goals: it offers evidence that open, efficient models can rival state-of-the-art systems and importantly, democratizes access by releasing the trained models. The work is highly relevant for researchers and practitioners aiming to build or study large language models without massive proprietary datasets.