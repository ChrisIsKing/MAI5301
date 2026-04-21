### Fast Inference from Transformers via Speculative Decoding

#### Problem Addressed
The issue addressed is that during generation, an LLM produces tokens one at a time in a loop, due to its autoregressive nature. This process is slow and causes a bottleneck at inference time. The researchers observed that while inference is bottlenecked on memory bandwidth, and slow data movement to and from processors to memory, there is also processing power in the GPUs that aren't being used. The question asked was how could you use this power to speed up generation from the LLM at inference without changing its output.

#### State of Related Works
At the time of this paper, several approaches existed to make inference faster. These included distillation (training smaller models to mimic larger ones), sparsification (reducing unnecessary computations), quantization (using lower precision numbers), and other architecture modifications. These approaches all came with limitations where they typically required changing the model architecture, changing the training procedure or retraining the models. These approaches tended to also produce different outputs. The researchers wanted something that could be applied to any existing model without changing its distribution output.

#### Proposed Solution and Key Insights
The researchers proposed speculative decoding. The core idea was to utilize two models: a large target model and a smaller, faster approximation model. They argued that the small model generates outputs much faster than the large model would because you would be doing the serial generation on a model requiring less processing power. The small model samples the next next γ of tokens in the sequence and passes it on to the larger model. The target model would then do speculative decoding where it accepts batches of outputs from the smaller model and processes those outputs. This is similar to parallel processing, where you can compute inference on batches of inputs simultaneously. The target model assigns probabilities to all of these sequences in parallel and then compare those probabilities to its. If the larger model agrees without the probability, you accept the token, otherwise the larger models rejects the token and resamples the output.

The researchers tested this method on T5-XXL (11B parameters) for English-to-German translation and summarization, and on LaMDA (137B parameters) for dialog. They found that approximation models that are roughly 2x smaller than the target model produced 2x–3x speedup in inference.

#### Drawbacks and Limitations
The speedup gains in this implementation depends heavily on how well the small model approximates the large model. As discussed in the lecture, as you increase gamma and generate longer speculative sequences, the divergence between the small and large models grows, especially for harder tasks like reasoning. So this methos works best when gamm is <= 5, as showed in the paper and also when the approximation model is similar in quality to the target model for a given task.

#### Future Directions
The researchers suggest a dynamic gamma variable, where instead of explicitly stating a fixed gamma value, you could dynamically predict and adjust gamma during inference.



### Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads

#### Problem Addressed
Large language models use autoregressive decoding, which is a sequential process where each token depends on the previous one's output. While speculative decoding was proposed to address this, it was difficulty to deploy and maintain a separate smaller model along with the target model. The researchers proposed that instead of using a smaller version of the target model you could use the existing target model and just add more decoding heads.

#### State of Related Works
At the time of this paper, speculative decoding was the common approach for speeding up inference time. While this was effective, it led to a more complicated than needed system of managing two separate models. Earlier work by Stern et al. (2018) had explored the idea of using multiple decoding heads on top of a backbone model, but it had not been refined or widely adopted for modern LLM inference.

#### Proposed Solution and Key Insights
The researchers proposed Medusa, which builds on an existing LLM by adding extra decoding heads on top of the model. Medusa proposes additional heads, typically three to five, where each head is responsible for predicting a token at a different future position. These predictions are used to generate a tree structure where all the possible outputs across the different head positions are mapped out. A tree based attention mechanism then processes all of these "candidate" nodes simultaneously in one forward pass to verify which branch is the best fit.

The researchers introduced two variants of Medusa. Medusa-1, a fine-tuned frozen backbone LLM, where the original model stays completely untouched and only the new heads are trained. and Medusa-2, fine-tuned together with the backbone LLM.

Medusa-1 achieved roughly 2.2x speedup without compromising generation quality while Medusa-2 achieved roughly 2.3 - 3.6x speedup depending on the task and model size.

#### Drawbacks and Limitations
Medusa-2 requires fine-tuning the decoding heads on data representative of the target use case, which may not always be available.

#### Future Directions
The multiple decoding heads approach demonstrated that you don't necessarily need a separate smaller model to achieve inference speedups, and that you can build speculation capability directly into the existing model architecture, making it significantly easier to deploy in practice. However, variation in tasks speedup could be further explored. As discussed in lecture, humanities tasks had lower speedups than math and coding because of the open ended nature of those tasks. Future work could look at whether head architectures or training strategies could be adapted per task type to close that gap. 