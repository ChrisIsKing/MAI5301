#### 1. The role of each component in the architecture
- Token Embedding: Convert input into vectors so that the model can process it.
- Transformer Block: Contains Feed-Forward Network and MHA
- Feed-Forward Network: Is a neural network guided by some activation function (and weigths), that maps input to an ouput.
- GELU: Activation function - determines if a neuron in a neural network should activate or not, and by what degree. GELU is preferred over RelU because RELU discards all negative values, while GELU does not.
- Layer Norm: To prevent exploding or vanishing gradients by normalizing inputs to each layer.
- Attention (MultiHeadAttention): Allows each token to attend to all other tokens, thereby calculating how each token relates to each other.

#### 2. Why residual connections are critical
- They allow stacking of many transformer layers without degredation by preventing vanishing gradients. 

#### 3. Parameter count breakdown by component
- Token embedding: 39,383,808 
- FFN: 4,722,432
- Attention: 2,360,064
- Layer Norm: 3,072
- 12 transformer blocks: (FFN + Attention + Layer Norm * 12) = 85,026,816
- Final Layer Norm: 1,536
- Total: (Token embedding 12 Transformer blocks + Final Layer Norm) 124,412,160

#### 4. Sample generation behavior before training
- Prompt:  Hello! How are you?
- Encoded:  [15496, 0, 1374, 389, 345, 30]
- Output:  Hello! How are you?The...) Guys Roche've chase Sag represented 175 veterinarySR Academy MIL Duo Symptoms