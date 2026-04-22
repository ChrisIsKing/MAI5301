### Toolformer: Language Models Can Teach Themselves to Use Tools

#### Problem Addressed
Large language models are capable of complex reasoning but fail at basic, deterministic tasks that much smaller, specialized systems can eaily handle, things like arithmetic, real-time date lookup, factual retrieval, and translation. The issue addressed is that these are not reasoning failures, they are capability gaps that cannot be closed by scaling the model, because they require access to information or computation that the model does not have at inference time. The researchers proposed that instead of hard-coding tool usage through human annotation, you could have the model teach itself when and how to use tools by generating its own training data, filtering for only the API calls that actually improve prediction of future tokens.

#### State of Related Works
At the time of this paper, tool use in language models was handled through task specific prompting or supervised fine-tuning, both of which required human annotated examples, showing the model when to call a tool and what arguments to pass. TALM explored a similar self-supervised model design for a calculator and a search engine, but only in settings where the model was fine-tuned for specific tasks. It wasn't designed to generalize across many tools at once. ReAct had shown that you could interleave reasoning and actions in a prompting framework, but it still depended on task specific demonstrations. None of these approaches scaled to teaching a model to autonomously decide when tool use is beneficial across arbitrary tasks in a zero-shot setting.

#### Proposed Solution and Key Insights
The researchers proposed a self-supervised pipeline for generating training data for tool use. The process works in three stages:
- The model uses few-shot prompting with just a few of human annotated examples per tool with API calls.
- Those API calls are actually executed and the results are inserted into the text.
- A perplexity-based filter checks the API call and its returned result. If it doesn't reduce perplexity, it gets thrown out.

The model is then fine-tuned only on API calls that passed the filter. Consequently, it only learns to call tools in relevant situations. The tools incorporated include a calculator, a Wikipedia search engine, a Q&A system, a translation system, and a calendar. Toolformer achieved substantially improved zero-shot performance across a variety of tasks, and was comparbale to models a few times its size.

#### Drawbacks and Limitations
The tool calling behavior is fed into the model's weights through fine-tuning, which means the API calling instructions are embedded in the training data. If an API changes its interface or gets deprecated, the model has no way of knowing and will continue generating API calls in the format it was trained on, which may result in incorrect or broken pipelines.

#### Future Directions
Future work should explore how to decouple tool knowledge from model weights, moving toward retrieval based or prompt based tool descriptions that can be updated at inference time without retraining. 

### Gorilla: Large Language Model Connected with Massive APIs

#### Problem Addressed
As the ecosystem of ML APIs has grown to massive scale, across platforms like HuggingFace, TorchHub, and TensorFlow Hub, selecting the right API and generating a correct call has become extremely difficult even for state-of-the-art models like GPT-4. The issue addressed is that firstly, models hallucinate API calls that don't exist, and even when they identify the right API, they frequently get the arguments, constraints, or usage patterns wrong. Secondly, the fact that APIs change - where they get updated, versioned, or deprecated, and a model with static training data has no mechanism for adapting to those changes at inference time. The researchers proposed fine-tuning a model specifically for API calling and integrating a retrieval system directly into both training and inference, so the model learns to use live documentation rather than memorize static API use.

#### State of Related Works
At the time of this paper, the main approach to getting LLMs to call APIs was few shot prompting, providing the model with a handful of API examples in the context window and hoping it generalized correctly. This worked for simple, well known APIs that were likely in the pretraining data, but broke down at scale. When the set of available APIs is large and overlapping, with many tools offering similar functionality but with nuanced differences, a model relying on its pretrained data has no way to distinguish between them or reason about constraints. Toolformer had approached this from a self-supervised fine-tuning angle, but embedded API knowledge into the model's weights, making it blind to documentation changes. There was also no benchmark that evaluated API calling at this scale, making it difficult to measure progress systematically.

#### Proposed Solution and Key Insights
The researchers proposed Gorilla, which is a LLaMA model fine-tuned using Retriever Aware Training (RAT). The key insight is that instead of training the model to memorize API signatures, you train it to use retrieved documentation. The pipeline has two modes:
- A document retriever fetches the up to date API documentation at inference time and passes it into the model's context, allowing Gorilla to adapt to API changes without retraining.
- The model relies on what it learned during fine-tuning without retrieval.

The reseaarchers also introduced APIBENCH to support evaluation efforts. APIBench is a dataset of 1,600+ API entries from HuggingFace, TorchHub, and TensorFlow Hub, alongside an AST tree matching evaluation metric that directly checks whether the generated API call matches a valid entry in the database. Gorilla outperforms GPT-4 on API call accuracy across all three hubs and substantially reduces hallucination.

#### Drawbacks and Limitations
The retrieval component introduces latency at inference time since the system needs to query a document store before the model can generate a response. The retrieved documentation is also injected directly into the context window, and for complex APIs with detailed documentation, this can fill up a large portion of the available context quickly, leaving less room for the actual task.

#### Future Directions
Future work should explore how to compress or summarize API documentation before inserting it into the context.