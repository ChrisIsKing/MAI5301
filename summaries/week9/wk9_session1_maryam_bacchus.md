### Flash-Decoding for Long-Context Inference

#### Problem Addressed
During inference, when a language model generates tokens one at a time, each new token must attend to all previous tokens in the sequence. The issue addressed is that this attention step requires reading the entire key value (KV) cache for every single token generated, and as the context length grows, this becomes extremely expensive. The bottneck becomes memory access. Even with KV caching, they still must be read from memory every time because attention requires the full context. The researchers proposed that parallelizing attention computation over past tokens could speed up the decoding in LLMs.

#### State of Related Works
At the time of this blog post, Flash Attention had been developed primarily for training, where you have many queries running at once, making it easy to form large matrix multiplications and fully utilize GPU resources. However, during decoding in inference, you're generating one token at a time, meaning you only have a single query. This meant the GPU was heavily underutilized because the workload was too small to fill up the GPU cores. Alternative methods included PyTorch attention primitives, Flash Attention V2, and FasterTransformer, but all of them slowed down significantly as context length increased because they processed the KV cache sequentially.

#### Proposed Solution and Key Insights
The researchers proposed Flash-Decoding, which parallelizes attention over the sequence of past tokens rather than over batches or query heads. The process works in three steps. First, the existing KV cache is split into chunks, each chunk is just a different view of the same memory, so this step has no GPU cost. Second, the single query computes attention against each chunk independently and in parallel, producing partial attention outputs per chunk. Third, those partial outputs are combined through softmax to produce the final output. This produces the same result as the sequential method, however it is significantly faster because you're now utilizing more GPU resources.

The researchers measured tokens per second during decoding across context lengths from 512 to 64K tokens. Flash-Decoding maintained relatively high tokens per second even as context size grew, while the previous methods like PyTorch primitives, Flash Attention V2, FasterTransformer degraded in performance. The researchers found that Flash-Decoding works 8x faster decoding.

#### Drawbacks and Limitations
Given the way it works, Flash-Decoding is optimized for long prompts and may not give similar performance gains for shorter sequences.



### Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM)

#### Problem Addressed
Serving large language models at high throughput requires batching many requests together at the same time. The issue addressed is that the key-value (KV) cache, which stores the attention keys and values for each request is huge, grows and shrinks dynamically, and its lifetime and length are not known in advance. Existing systems stored KV cache in contiguous memory, meaning they had to pre-allocate a contiguous chunk of memory based on the request's maximum possible length (e.g., 2048 tokens). This led to internal fragmentation because the actual length of a request is often much shorter than the maximum. It also caused external fragmentation because different requests need different sized chunks. The researchers found that only 20–38% of KV cache memory was actually storing useful token states in existing systems. The rest was wasted.

#### State of Related Works
At the time of this paper, the main LLM serving systems were NVIDIA's FasterTransformer and Orca. Orca had introduced iteration level scheduling, which parallelises requests so more can be processed in parallel scheduling. However, the underlying memory management was still inefficient because it relied on contiguous memory allocation for KV cache. Deep learning frameworks like PyTorch and TensorFlow require tensors to be stored in contiguous memory,which did not work optimally for dynamic, variable length nature of KV cache during autoregressiion. Memory compaction had been proposed as a solution to fragmentation, but compaction was impractical due to the massive size of KV caches.

#### Proposed Solution and Key Insights
The researchers proposed PagedAttention, an attention algorithm inspired by virtual memory and paging from operating systems. Instead of storing the KV cache in one contiguous chunk, PagedAttention divides it into fixed size blocks, where each block holds the keys and values for a fixed number of tokens. These blocks do not need to be stored contiguously in memory. A block table tracks the mapping between logical blocks and memory addresses, similar to the page table in operating systems. This design eliminates internal fragmentation, resulting in less than 4% waste in practice. It eliminates external fragmentation also because all blocks are the same size. And it enables memory sharing, when multiple output sequences share the same prompt, they can point to the same physical blocks for the shared portion. This sharing alone reduced memory usage by up to 55% for complex decoding methods like beam search.

In addition to PagedAttention, they built vLLM, an LLM serving engine with a scheduler that has a KV cache manager that handles block- evel allocation, freeing, and sharing. vLLM also supports a type of swap memory, where KV cache blocks can be stored to CPU if GPU VRAM runs out of storage.

vLLM improved throughput by 2 to 4 times compared to FasterTransformer and Orca at the same level of latency. The system also ensured minimal KV cache memory waste, where about 96% of KV cache memory was used for actual token states, without affecting model accuracy or latency.

#### Drawbacks and Limitations
The researchers addressed that using a larger block size increases hardware utilization and reduces latency per block, but also increases internal fragmentation, so there's a tradeoff in choosing block size.

#### Future Directions
The paper established that memory management, not just computation, is a critical bottleneck in serving LLMs. The vLLM system was open sourced, and the swap-memory memory management to GPU workloads could open up further research into more sophisticated scheduling and memory optimizations for LLMs.