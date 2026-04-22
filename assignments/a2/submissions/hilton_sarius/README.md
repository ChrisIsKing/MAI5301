# Coding Assignments - MAI5301

## Overview

The coding assignments in this course are based on **"Build a Large Language Model (From Scratch)"** by Sebastian Raschka (Manning Publications, September 2024). Through five progressive assignments, you will implement a complete GPT-style language model from the ground up, gaining deep understanding of transformer architecture, training procedures, and fine-tuning techniques.

📚 **Companion Repository**: [github.com/rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)

## Assignment Structure

| Assignment | Chapters | Topic | Due Date | Weight |
|------------|----------|-------|----------|--------|
| [A1](#assignment-1-tokenization-and-data-preparation) | Ch 2 | Tokenization & Data Preparation | Sun, Jan 18, 2026 | 5% |
| [A2](#assignment-2-attention-mechanisms) | Ch 3 | Attention Mechanisms | Sun, Feb 1, 2026 | 5% |
| [A3](#assignment-3-gpt-architecture) | Ch 4 | GPT Model Architecture | Sun, Feb 15, 2026 | 6% |
| [A4](#assignment-4-pretraining) | Ch 5 | Pretraining from Scratch | Sun, Mar 1, 2026 | 7% |
| [A5](#assignment-5-advanced-fine-tuning) | Ch 6/7/AppE | Advanced Fine-tuning (choice) | Sun, Mar 22, 2026 | 7% |

**Total**: 30% of course grade

## General Guidelines

### Submission Requirements

1. **Format**: Submit via pull request to `assignments/<assignment-name>/<your-name>/`
2. **Files Required**:
   - Jupyter notebook(s) with your implementation
   - `README.md` documenting your approach, challenges, and insights
   - Any additional Python scripts if you prefer modular code
3. **Code Quality**:
   - Clear variable names and function documentation
   - Comments explaining non-obvious implementation choices
   - Working code that runs without errors
4. **Documentation**:
   - Brief explanation of each major component
   - Comparison of your outputs with book's expected results
   - Discussion of any deviations or difficulties encountered

### Environment Setup

```bash
# Clone the companion repository
git clone https://github.com/rasbt/LLMs-from-scratch.git

# Install dependencies
pip install torch numpy matplotlib tiktoken

# For assignments requiring training (A4, A5)
pip install tqdm tensorboard
```

**GPU Access**: While not strictly required, GPU access (via Google Colab, Kaggle, or local) is highly recommended for A4 and A5.

### Academic Integrity

- **Implementation from Scratch**: You must implement the core components yourself, not copy-paste from the book repository
- **Book as Reference**: You should use the book code as a reference to understand concepts and verify your implementation
- **Exercise Solutions**: The book's exercise solutions can guide your understanding, but your submission must be your own work
- **AI Assistance**: You may use AI tools (ChatGPT, Copilot) for understanding concepts, debugging, and learning, but all submitted code must reflect your understanding

### Grading Rubric (Applies to All Assignments)

| Component | Points | Description |
|-----------|--------|-------------|
| **Correctness** | 40% | Implementation works correctly, produces expected outputs |
| **Code Quality** | 25% | Clear, well-documented, follows best practices |
| **Understanding** | 25% | README demonstrates deep understanding of concepts |
| **Completeness** | 10% | All required components implemented, exercises attempted |

---

## Assignment 1: Tokenization and Data Preparation

**Based on**: Chapter 2 - Working with Text Data  
**Due**: Sunday, January 18, 2026 (11:59 PM GYD)  
**Weight**: 5%

### Learning Objectives

- Understand how text is converted to numerical representations
- Implement byte-pair encoding (BPE) tokenization
- Create efficient data loaders for language model training
- Handle sliding window context for next-token prediction

### Key Concepts from Chapter 2

- Text tokenization approaches (word-level, character-level, subword)
- Byte-pair encoding (BPE) algorithm
- Special tokens and vocabulary building
- Creating input-target pairs for language modeling
- Efficient batching with PyTorch DataLoader

### Required Implementations

1. **Simple Tokenizer** (Section 2.2-2.3)
   - Build a basic word-level tokenizer
   - Implement encoding and decoding functions
   - Handle unknown tokens

2. **BPE Tokenizer** (Section 2.4-2.5)
   - Implement or use the `tiktoken` library
   - Understand GPT-2's BPE vocabulary
   - Handle special tokens (e.g., `<|endoftext|>`)

3. **Data Sampling** (Section 2.6-2.7)
   - Create sliding window data samples
   - Implement efficient batching
   - Build a PyTorch Dataset and DataLoader

4. **Text Generation Setup** (Section 2.8)
   - Prepare data format for training
   - Create input-target pairs with proper shifting

### Deliverables

1. **Notebook**: `assignment1.ipynb` with:
   - Working tokenizer implementations
   - Data loader that produces batches of token IDs
   - Visualization of how text gets tokenized
   - Tests comparing your tokenizer output with `tiktoken`

2. **README**: Document:
   - How BPE differs from simpler tokenization approaches
   - Why sliding windows are used for language modeling
   - Any challenges you encountered with batching

### Starter Code Hints

Reference the book's:
- `ch02/01_main-chapter-code/ch02.ipynb` - Main implementations
- `ch02/02_bonus_bytepair-encoder/bpe_openai_gpt2.ipynb` - BPE details
- `ch02/03_bonus_embedding-vs-matmul/embeddings-and-linear-layers.ipynb` - Understanding embeddings

### Exercises (Attempt at least 2)

1. **Exercise 2.1**: Implement a character-level tokenizer and compare vocabulary size with BPE
2. **Exercise 2.2**: Modify the data loader to handle variable-length sequences with padding
3. **Exercise 2.3**: Analyze token frequency distribution in your dataset

---

## Assignment 2: Attention Mechanisms

**Based on**: Chapter 3 - Coding Attention Mechanisms  
**Due**: Sunday, February 1, 2026 (11:59 PM GYD)  
**Weight**: 5%

### Learning Objectives

- Implement self-attention from scratch
- Understand causal masking for autoregressive generation
- Build multi-head attention mechanism
- Integrate attention with trainable weights

### Key Concepts from Chapter 3

- Self-attention mechanism (queries, keys, values)
- Scaled dot-product attention
- Causal attention masks for language modeling
- Multi-head attention architecture
- Attention weights visualization

### Required Implementations

1. **Simple Self-Attention** (Section 3.2-3.3)
   - Implement basic self-attention without trainable parameters
   - Calculate attention weights and weighted values
   - Visualize attention patterns

2. **Scaled Dot-Product Attention** (Section 3.4)
   - Add scaling factor to prevent gradient issues
   - Implement causal masking for autoregressive models
   - Handle different sequence lengths

3. **Trainable Attention** (Section 3.5)
   - Add Query, Key, Value weight matrices
   - Implement forward pass with trainable parameters
   - Initialize weights properly

4. **Multi-Head Attention** (Section 3.6)
   - Split embeddings across multiple attention heads
   - Implement parallel attention computation
   - Concatenate and project multi-head outputs

### Deliverables

1. **Notebook**: `assignment2.ipynb` with:
   - Complete attention mechanism implementations
   - Visualizations of attention patterns for sample text
   - Comparison of single-head vs multi-head attention
   - Tests showing correct output shapes

2. **README**: Document:
   - Why causal masking is necessary for language models
   - The purpose of multiple attention heads
   - How attention weights reveal model's focus

### Starter Code Hints

Reference the book's:
- `ch03/01_main-chapter-code/ch03.ipynb` - Core attention implementations
- `ch03/02_bonus_efficient-multihead-attention/mha-implementations.ipynb` - Optimization techniques

### Exercises (Attempt at least 2)

1. **Exercise 3.1**: Implement attention with different numbers of heads (1, 2, 4, 8) and compare
2. **Exercise 3.2**: Visualize attention patterns for different types of text (narrative, code, poetry)
3. **Exercise 3.3**: Implement grouped-query attention (GQA) as an extension

---

## Assignment 3: GPT Architecture

**Based on**: Chapter 4 - Implementing a GPT Model from Scratch  
**Due**: Sunday, February 15, 2026 (11:59 PM GYD)  
**Weight**: 6%

### Learning Objectives

- Build the complete GPT model architecture
- Implement LayerNorm and feed-forward networks
- Integrate all components (embeddings, attention, FFN)
- Generate text with your model (before training)

### Key Concepts from Chapter 4

- LayerNorm for training stability
- GELU activation function
- Feed-forward network in transformers
- TransformerBlock: attention + FFN with residual connections
- Token and positional embeddings
- Complete GPT architecture assembly

### Required Implementations

1. **Layer Normalization** (Section 4.2)
   - Implement LayerNorm from scratch
   - Compare with PyTorch's built-in version
   - Understand pre-norm vs post-norm placement

2. **GELU Activation** (Section 4.3)
   - Implement the GELU activation function
   - Compare with ReLU behavior

3. **Feed-Forward Network** (Section 4.4)
   - Build the two-layer FFN
   - Apply GELU activation
   - Understand expansion ratio (4x hidden size)

4. **TransformerBlock** (Section 4.5-4.6)
   - Combine attention and FFN
   - Add residual connections
   - Apply LayerNorm
   - Implement dropout for regularization

5. **Complete GPT Model** (Section 4.7-4.8)
   - Implement token embeddings
   - Add absolute positional embeddings
   - Stack multiple TransformerBlocks
   - Add final layer norm and output projection
   - Generate text with untrained model

### Deliverables

1. **Notebook**: `assignment3.ipynb` with:
   - All architecture components implemented
   - Forward pass demonstration with sample input
   - Text generation example (will be gibberish before training)
   - Model size calculation (parameters count)

2. **README**: Document:
   - The role of each component in the architecture
   - Why residual connections are critical
   - Parameter count breakdown by component
   - Sample generation behavior before training

### Starter Code Hints

Reference the book's:
- `ch04/01_main-chapter-code/ch04.ipynb` - Full GPT implementation
- `ch04/01_main-chapter-code/gpt.py` - Modular GPT code
- `ch04/02_performance-analysis/gpt-model-memory-analysis.ipynb` - Memory analysis
- `ch04/03_understanding-buffers/understanding-buffers.ipynb` - Understanding PyTorch buffers

### Exercises (Attempt at least 2)

1. **Exercise 4.1**: Implement different GPT sizes (small: 6 layers, medium: 12 layers) and compare
2. **Exercise 4.2**: Add dropout with different rates and observe effects on forward pass
3. **Exercise 4.3**: Implement KV-cache for efficient generation (see `ch04/04_kv-cache/`)
4. **Exercise 4.4**: Analyze memory usage for different model sizes

---

## Assignment 4: Pretraining

**Based on**: Chapter 5 - Pretraining on Unlabeled Data  
**Due**: Sunday, March 1, 2026 (11:59 PM GYD)  
**Weight**: 7%

### Learning Objectives

- Implement the training loop for language models
- Calculate and track training/validation loss
- Generate text during training to monitor progress
- Load pretrained GPT-2 weights and use them

### Key Concepts from Chapter 5

- Next-token prediction loss (cross-entropy)
- Training vs validation split
- Learning rate scheduling
- Text generation during training
- Loading and using pretrained weights
- Model saving and checkpointing

### Required Implementations

1. **Loss Calculation** (Section 5.2)
   - Implement batch loss computation
   - Calculate perplexity from loss
   - Handle loss across different batch sizes

2. **Training Loop** (Section 5.3-5.4)
   - Implement basic training loop
   - Track training and validation loss
   - Add progress monitoring with text generation
   - Implement early stopping criteria

3. **Text Generation** (Section 5.5)
   - Implement greedy decoding
   - Add temperature sampling
   - Implement top-k sampling
   - Compare generation strategies

4. **Loading Pretrained Weights** (Section 5.6)
   - Load GPT-2 weights from OpenAI
   - Adapt weight shapes to your architecture
   - Generate text with pretrained model

### Deliverables

1. **Notebook**: `assignment4.ipynb` with:
   - Training loop implementation
   - Training curves (loss over time)
   - Sample text generated at different training stages
   - Comparison of your trained model with loaded GPT-2 weights
   - At least 2 hours of training on a small dataset (or more if GPU available)

2. **README**: Document:
   - Training hyperparameters chosen and why
   - How loss decreases during training
   - Quality improvement in generated text
   - Challenges with training from scratch vs using pretrained weights
   - Compute resources used

### Starter Code Hints

Reference the book's:
- `ch05/01_main-chapter-code/ch05.ipynb` - Training pipeline
- `ch05/02_alternative_weight_loading/weight-loading-hf-transformers.ipynb` - Alternative loading
- `ch05/03_bonus_pretraining_on_gutenberg/pretraining-on-gutenberg.ipynb` - Full pretraining example
- `ch05/04_learning_rates/learning-rate-schedulers.ipynb` - LR scheduling
- `ch05/05_bonus_hparam_tuning/hparam-tuning.ipynb` - Hyperparameter tuning

### Exercises (Attempt at least 2)

1. **Exercise 5.1**: Implement learning rate warmup and cosine decay
2. **Exercise 5.2**: Compare different sampling strategies (temperature, top-k, nucleus)
3. **Exercise 5.3**: Train on different datasets and compare convergence
4. **Exercise 5.4**: Implement gradient accumulation for larger effective batch size

---

## Assignment 5: Advanced Fine-tuning

**Based on**: Chapters 6, 7, and Appendix E (Choose ONE path)  
**Due**: Sunday, March 22, 2026 (11:59 PM GYD)  
**Weight**: 7%

### Overview

For this assignment, you will choose **one** of three advanced fine-tuning approaches. This flexibility allows you to explore the technique most aligned with your interests while demonstrating mastery of fine-tuning concepts.

---

### Option A: Classification Fine-tuning

**Based on**: Chapter 6 - Finetuning for Classification

#### Learning Objectives
- Adapt a pretrained language model for classification
- Implement task-specific output heads
- Evaluate classification performance
- Compare fine-tuning strategies

#### Key Concepts
- Replacing the LM head with classification head
- Freezing vs fine-tuning all layers
- Handling class imbalance
- Classification metrics (accuracy, F1, etc.)

#### Required Implementations

1. **Model Adaptation** (Section 6.2-6.3)
   - Modify GPT for classification (replace output head)
   - Implement freezing strategies
   - Handle different classification scenarios

2. **Training Loop** (Section 6.4)
   - Adapt training for classification
   - Track accuracy instead of perplexity
   - Implement validation evaluation

3. **Evaluation** (Section 6.5)
   - Calculate classification metrics
   - Analyze model predictions
   - Compare with baseline approaches

4. **Dataset** (Section 6.6)
   - Use spam classification dataset
   - Implement proper train/test splits
   - Handle text preprocessing for classification

#### Deliverables

1. **Notebook**: `assignment5_classification.ipynb` with:
   - Complete classification pipeline
   - Training curves and accuracy metrics
   - Confusion matrix and error analysis
   - Comparison of frozen vs full fine-tuning

2. **README**: Document:
   - Why classification fine-tuning differs from pretraining
   - Impact of freezing strategies on performance
   - Dataset characteristics and challenges
   - Your model's strengths and weaknesses

#### Starter Code Hints
- `ch06/01_main-chapter-code/ch06.ipynb` - Full classification pipeline
- `ch06/01_main-chapter-code/gpt_class_finetune.py` - Standalone script
- `ch06/02_bonus_additional-experiments/imdb-classification.ipynb` - Alternative dataset
- `ch06/03_bonus_imdb-classification/train-gpt-on-imdb.ipynb` - More examples

---

### Option B: Instruction Fine-tuning

**Based on**: Chapter 7 - Finetuning to Follow Instructions

#### Learning Objectives
- Prepare instruction datasets
- Implement instruction-tuning pipeline
- Generate responses to instructions
- Understand prompt formatting

#### Key Concepts
- Instruction-input-response format
- Alpaca-style prompt templates
- Masking for instruction fine-tuning
- Response generation strategies

#### Required Implementations

1. **Dataset Preparation** (Section 7.2)
   - Format instruction datasets (Alpaca format)
   - Implement proper masking (don't compute loss on instructions)
   - Create custom collation functions

2. **Training Pipeline** (Section 7.3-7.4)
   - Adapt training for instruction format
   - Handle variable-length inputs
   - Implement proper batching

3. **Evaluation** (Section 7.5-7.6)
   - Generate responses to new instructions
   - Implement response quality checks
   - Compare instruction-tuned vs base model

4. **Advanced (Optional)** (Section 7.7)
   - Explore preference tuning (DPO)
   - Understand RLHF concepts

#### Deliverables

1. **Notebook**: `assignment5_instruction.ipynb` with:
   - Instruction dataset preparation
   - Training pipeline with proper masking
   - Sample instruction-response generations
   - Comparison with base model behavior

2. **README**: Document:
   - How instruction formatting affects training
   - Why masking is crucial for instruction tuning
   - Quality of your model's instruction-following
   - Differences from classification fine-tuning

#### Starter Code Hints
- `ch07/01_main-chapter-code/ch07.ipynb` - Instruction tuning pipeline
- `ch07/01_main-chapter-code/gpt_instruction_finetuning.py` - Standalone script
- `ch07/02_dataset-utilities/download-prepare-dataset.ipynb` - Dataset prep
- `ch07/03_model-evaluation/llm-instruction-eval-ollama.ipynb` - Evaluation
- `ch07/04_preference-tuning-with-dpo/dpo-from-scratch.ipynb` - DPO (advanced)

---

### Option C: Parameter-Efficient Fine-tuning (LoRA)

**Based on**: Appendix E - Adding LoRA for Parameter-Efficient Finetuning

#### Learning Objectives
- Implement Low-Rank Adaptation (LoRA)
- Understand parameter-efficient fine-tuning
- Compare LoRA with full fine-tuning
- Analyze efficiency trade-offs

#### Key Concepts
- Low-rank decomposition
- Adapter modules
- Freezing base model parameters
- Merging LoRA weights

#### Required Implementations

1. **LoRA Layers** (Appendix E.1-E.2)
   - Implement LoRA linear layers
   - Add adapters to attention mechanism
   - Handle rank and alpha hyperparameters

2. **Model Adaptation** (Appendix E.3)
   - Integrate LoRA into GPT architecture
   - Freeze base model parameters
   - Train only LoRA parameters

3. **Training** (Appendix E.4)
   - Train with LoRA (classification or instruction task)
   - Track parameter count differences
   - Monitor training efficiency

4. **Analysis** (Appendix E.5)
   - Compare LoRA vs full fine-tuning performance
   - Analyze training time and memory usage
   - Experiment with different rank values

#### Deliverables

1. **Notebook**: `assignment5_lora.ipynb` with:
   - LoRA implementation
   - Training on chosen task (classification or instruction)
   - Parameter count comparison
   - Performance vs efficiency analysis

2. **README**: Document:
   - How LoRA reduces trainable parameters
   - Trade-offs between rank and performance
   - When to use LoRA vs full fine-tuning
   - Your experimental results and insights

#### Starter Code Hints
- `appendix-E/01_main-chapter-code/appendix-E.ipynb` - LoRA implementation
- Compare with full fine-tuning from Ch6 or Ch7

---

## Assignment 5: Grading Criteria (All Options)

| Component | Points | Description |
|-----------|--------|-------------|
| **Implementation** | 35% | Correct implementation of chosen approach |
| **Training** | 25% | Successful training with proper monitoring |
| **Analysis** | 25% | Deep analysis of results, comparisons, insights |
| **Documentation** | 15% | Clear explanation of choices and findings |

---

## FAQs

### Can I use Google Colab?
Yes! Google Colab is recommended for assignments requiring GPU (A4, A5). Make sure to:
- Save checkpoints frequently
- Download your trained models
- Be aware of runtime limits

### Do I need to train to convergence?
For A4 and A5, you should train until you see clear improvement, but full convergence is not required given compute constraints. Document what you trained and for how long.

### Can I use the book's code as a starting point?
You should implement from scratch to demonstrate understanding, but you can reference the book code to:
- Understand concepts
- Debug your implementation
- Verify your outputs match expected results

### Can I collaborate with other students?
You may discuss concepts and debug together, but all submitted code must be your own. Do not share notebooks or code directly.

### What if I get stuck?
1. Review the relevant book chapter carefully
2. Check the companion repository for hints
3. Post on GitHub Issues (anonymize your specific code)
4. Attend office hours

### Can I use libraries like Hugging Face Transformers?
For the core implementations (A1-A4), you must implement from scratch using only PyTorch basics. For A5, you may use utility functions but the fine-tuning logic should be your own.

---

## Additional Resources

### Book Repository Structure
```
LLMs-from-scratch/
├── ch02/ - Tokenization
├── ch03/ - Attention
├── ch04/ - GPT Architecture
├── ch05/ - Pretraining
├── ch06/ - Classification Fine-tuning
├── ch07/ - Instruction Fine-tuning
└── appendix-E/ - LoRA
```

Each chapter contains:
- `01_main-chapter-code/` - Core implementations
- `02_bonus_*/` - Additional materials and variations
- `exercise-solutions.ipynb` - Exercise answers

### Recommended Reading Order

1. Read the chapter thoroughly before starting the assignment
2. Work through the main notebook (`chXX.ipynb`) to understand the flow
3. Attempt the exercises to deepen understanding
4. Implement your own version from scratch
5. Compare your outputs with the book's results
6. Explore bonus materials for deeper insights

### Computing Resources

- **Local Development**: Fine for A1-A3, challenging for A4-A5
- **Google Colab Free**: Sufficient for all assignments with careful session management
- **Colab Pro**: Recommended for A4-A5 if you want to train longer
- **Kaggle Notebooks**: Alternative with GPU access
- **University Resources**: Contact instructor if you need access to compute

---

## Submission Checklist

Before submitting each assignment:

- [ ] Code runs without errors from top to bottom
- [ ] All required implementations are complete
- [ ] Outputs match expected results (or deviations are explained)
- [ ] README documents approach, findings, and challenges
- [ ] Code is well-commented and readable
- [ ] Academic integrity guidelines followed
- [ ] Files organized in proper directory structure
- [ ] Pulled latest changes from course repository
- [ ] Created pull request with clear title and description

---

**Questions?** Open a GitHub Issue or attend office hours. Good luck building your LLM! 🚀
