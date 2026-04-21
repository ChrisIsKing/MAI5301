paper 1
Why might adding a fixed linear bias directly to attention scores help transformers generalize to longer sequences, instead of just encoding position like traditional embeddings?

paper 2
By biasing attention scores proportionally to token distances, the model essentially learns an inductive bias favoring recent context. This bias is functional (embedded in attention mechanics) rather than representational (encoded in vectors), making the model’s scoring behavior extend smoothly beyond training lengths.