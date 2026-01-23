### GLU Variants Improve Transformer (SwiGLU)

#### Problem Addressed
Standard transformers use simple activation functions, like ReLU, in their feed forward layers. The issue addressed is that simple activations don't provide nuanced control over what information passes through the network; They act as basic on/off switches. The researchers proposed that a more sophisticated gating mechanism could help the model learn to select which information to pass through and which information to suppress. 

#### State of Related Works
At the time of this paper, standard activation functions were used. These activation functions were not dynamic. ReLU (Rectified Linear Unit) is simple, but has a very steep gradient - acting as a basic on/off switch (fire or don't fire the neuron). GELU (Gaussian Error Linear Unit) is smoother than ReLU, but it is computationally more expensive. It multiplies the input by a probability, scaling the input by how much it exceeds a random treshold. The issue with this is for very small input values, it does not fire. Swish is very similar to GELU, but it multiplies the input by sigmoid function. Gated Linear units (GLU) also existed, but it wasn't used in the transformer model network as yet.

#### 3. Proposed Solution and Key Insights
The researchers proposed using the Gated Linear Units (GLU) in transformer models. Instead of the standard single projection FFN, GLU introduced a two path system with content path and a gate path. The content part represents the information being processed, while the gate path controls how much of that information can flow through to other layers. The gate path produces values between zero and one, allowing parts of the information from the content path to "feed forward". When the gate outputs 0, the content is blocked. When the gate has a value of one, it is passes the entire content forward. This algorithm allowed you to control the flow amount in the network. The gate acts almost like a pipe.

The researchers found that Gated variants of ReLU, GeLU, and Gated Swish yielded improved performance on language modeling tasks. 

#### Drawbacks and Limitations
The authors addressed directly that they're not sure why using gated variants of of the activated functions yield better results. There is no clear mathematical proof as to why this happen. This optimization with performance increase probably breaks under other conditions, not yet explored. 

#### Future Directions
The researchers mentioned that " These architectures are simple to implement, and have no apparent computational drawbacks". It should be tested under other conditions, if any, that these performance increases do not occur. 


### GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints

#### Problem Addressed
The main problem addressed in this paper is the memory bandwidth bottleneck during transformer inference, caused by loading key value (KV) pairs in multi-head attention. 
Due to how autoregressive generation models work, by using all previous tokens to compute the next token, Multi Head Attention (MHA) caused memory to run out quickly. Meanwhile, Multi Query Attention (MQA) caused a drop in quality. In large inferences, memory constraints, specifically in the KV Cache was a concern.
Companies worried about user experience, latency and computational costs in production systems.

#### State of Related Works
The researchers considered the two approaches used at the time MQA and MHA. In MHA, each attention head has its own query, key and value - this contributed to a high quality model, however, it is slow as it needs to calculate each attention score and store that in the KV Cache. MQA solves this problem by sharing key, value heads with all the query heads. The advantage of this is that is optimized calculation thus performed computations quickly, the downside is that there was a drop in quality due to some generalization from sharing key value heads.

#### Proposed Solution and Key Insights
The researchers proposed GQA as the middle ground between MQA and MHA. Firstly, they proposed the idea of uptraining. This is where the model is already trained with MHA and is producing good outputs. You can make this model faster at infernce time by utilizing GQA. Grouped Query Attention (GQA) is a mix between MHA and MQA. GQA groups query heads to share KV heads. The key insight is finding the right balance, by adjusting the number of groups based on the quality/speed tradeoff requirements of your own model. You can train the model on GQA for just a little longer and acheive the same quality, or close to it, while benefitting from the speed of MQA.

#### Drawbacks and Limitations
The researchers mentioned that they do not know the relative performance of uptraining vs training from scratch, meaning that it's possible that you could not train a model effectively with GQA. 