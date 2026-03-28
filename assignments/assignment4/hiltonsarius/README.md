# Assignment #5 - Classification Fine-tuning
### MAI5301: Foundations of Large Language Models
**Student:** Hilton Sarius
**Option chosen:** A - Classification Fine-tuning
**Model:** GPT-2 Small (124M parameters)
**Task:** Binary spam classification (ham vs. spam)

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Dataset Characteristics and Challenges](#2-dataset-characteristics-and-challenges)
3. [Why Classification Fine-tuning Differs from Pretraining](#3-why-classification-fine-tuning-differs-from-pretraining)
4. [Model Architecture and Adaptation](#4-model-architecture-and-adaptation)
5. [Impact of Freezing Strategies on Performance](#5-impact-of-freezing-strategies-on-performance)
6. [Training Setup](#6-training-setup)
7. [Results and Analysis](#7-results-and-analysis)
8. [Model Strengths and Weaknesses](#8-model-strengths-and-weaknesses)
9. [Key Takeaways](#9-key-takeaways)

---

## 1. Project Overview

This assignment implements **binary text classification** by adapting a pretrained GPT-2 language model to distinguish spam SMS messages from legitimate ones (ham). Rather than training a model from scratch, the pretrained weights are reused as a starting point and only the parts of the network necessary for classification are modified or retrained.

The core research question explored in this assignment is: **how much of a pretrained model actually needs to be updated to achieve strong classification performance?** Two strategies are compared selectively freezing most of the model versus updating every parameter to understand the trade-off between training efficiency and accuracy.

---

## 2. Dataset Characteristics and Challenges

### 2.1 Source

The dataset used is the **UCI SMS Spam Collection**, a publicly available benchmark containing **5,572 labelled SMS messages** collected for mobile spam research. Each message is labelled as either `ham` (legitimate) or `spam`.

The dataset can be downloaded from:
`https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip`

### 2.2 Class Imbalance and Balancing Strategy

The original dataset is heavily skewed:

| Class | Count | Proportion |
|-------|-------|------------|
| Ham   | 4,825 | 86.6%      |
| Spam  |   747 | 13.4%      |

Training directly on this imbalanced distribution would encourage the model to default to predicting "ham" for almost every input a strategy that achieves 86.6% accuracy while being completely useless at detecting spam. To prevent this, **random undersampling** was applied to the majority class: 747 ham messages were randomly selected to match the 747 spam messages, yielding a fully balanced dataset of **1,494 examples**.

### 2.3 Dataset Splitting

The balanced dataset was divided into training, validation, and test sets using scikit-learn's `train_test_split` with the `stratify` parameter. Stratified splitting guarantees that the 50/50 class ratio is preserved exactly in every split unlike a manual shuffle-and-slice approach, which only approximates balance by chance and can produce skewed splits with unlucky seeds.

The split was performed in two stages:
1. **Test set (20%)** separated first from the full dataset.
2. **Validation set (12.5% of the remaining 80%)** separated next, yielding approximately 10% of the total.

| Split      | Proportion | Examples (approx.) |
|------------|------------|---------------------|
| Training   | ~70%       | ~1,046              |
| Validation | ~10%       | ~149                |
| Test       | ~20%       | ~299                |

### 2.4 Tokenisation and Preprocessing

All messages were tokenised using **tiktoken** with the GPT-2 encoding (`gpt2`), which uses byte-pair encoding (BPE) and a vocabulary of 50,257 tokens. To allow efficient batching, all sequences were padded or truncated to a **fixed length of 120 tokens**. This value was chosen by inspecting the longest tokenised sequence in the training set. The GPT-2 end-of-text token (`<|endoftext|>`, ID 50256) was used as the padding token, consistent with the approach used in the reference implementation.

### 2.5 Challenges

Working with this dataset presents several non-trivial challenges that affect both model training and real-world applicability:

 **Short message length** The majority of SMS messages are fewer than 30 words. Short inputs give the model minimal context to work with, and the final-token representation used for classification may not be meaningful for very short sequences (2-4 words). The model must make a confident binary decision from very little signal.

 **Informal language** SMS messages frequently contain abbreviations (`u`, `wif`, `lol`, `hor`), slang, missing punctuation, and unconventional capitalisation. GPT-2 was pretrained primarily on formal English web text, so its tokeniser and representations are not optimally suited for this informal register. Some tokens may be split in unexpected ways by the BPE tokeniser, potentially losing semantic meaning.

 **Dataset vintage and distribution shift** The collection dates from the mid-2000s. Spam patterns have evolved significantly since then. Modern spam relies on URL shorteners, impersonation of trusted brands (banks, delivery companies, government agencies), and adversarially crafted phrasing designed to bypass keyword filters none of which are well represented in this dataset. A model trained here may fail on current spam without retraining.

 **Binary label granularity** The ham/spam distinction is binary, but real-world messages exist on a spectrum. Promotional texts from legitimate companies, subscription alerts, and automated notifications may share vocabulary with spam but are not spam. The binary label does not capture this nuance, and the model will inherit that limitation.

 **Small dataset size** After balancing, only 1,494 examples remain a very small dataset by modern NLP standards. This limits how much adaptation is possible before overfitting, and makes the choice of fine-tuning strategy especially important.

---

## 3. Why Classification Fine-tuning Differs from Pretraining

Understanding what changes during fine-tuning requires first understanding what GPT-2 learns during pretraining.

### 3.1 The Pretraining Objective

During pretraining, GPT-2 is trained on **next-token prediction** (also called causal language modelling). Given a sequence of tokens, the model learns to predict the next token at every position in the sequence. The final output layer a linear projection of size `[hidden_dim → vocab_size]` (768 → 50,257 for GPT-2 Small) produces a probability distribution over the entire vocabulary at each position. The training loss is the average cross-entropy across all positions in all sequences, computed over billions of tokens of web text.

This objective forces the model to develop rich, general-purpose representations of language: grammar, syntax, factual knowledge, discourse structure, and stylistic patterns. These representations are encoded in the transformer's attention weights and feedforward layers across all 12 layers and are what make transfer learning possible.

### 3.2 How Classification Fine-tuning Changes the Task

Classification fine-tuning repurposes these pretrained representations for a fundamentally different task. The key differences are:

**1. Output head replacement**
The pretrained language modelling head (50,257 outputs) is discarded entirely and replaced with a new, randomly initialised linear layer with only 2 outputs one logit per class (ham and spam). This new head is small (`[768 → 2]`) and is the only component that begins without any prior knowledge. All transformer weights carry over from pretraining.

**2. Prediction from a single token position**
Rather than computing a prediction at every token position in the sequence, classification uses only the **hidden state at the final token position** (`sequence[:, -1, :]`). This single vector is expected to encode a summary of the entire input message. This is possible because GPT-2 uses causal (left-to-right) attention by the time the model processes the last token, it has already attended to every previous token in the sequence.

**3. Loss computation**
The loss is computed as a cross-entropy between the 2-class logits and the true label (0 for ham, 1 for spam). This is computed once per example on a single token position rather than once per token position across the whole sequence. The gradient signal is therefore sparser but more directly tied to the classification objective.

**4. Preserved representations, new direction**
The pretrained weights are not discarded they are the starting point. Fine-tuning adjusts these weights (partially or fully, depending on the chosen strategy) so that the representation at the final token position becomes more discriminative for the ham/spam task. The model does not need to relearn language from scratch; it only needs to learn to apply what it already knows in a new direction: from generation toward discrimination.

### 3.3 Summary of Key Differences

| Aspect               | Pretraining                          | Classification Fine-tuning           |
|----------------------|--------------------------------------|--------------------------------------|
| Objective            | Next-token prediction                | Binary class prediction              |
| Output head          | Linear → 50,257 vocabulary tokens    | Linear → 2 class logits              |
| Loss computed at     | Every token position                 | Final token position only            |
| Labels               | Next token in the sequence           | Ham (0) or Spam (1)                  |
| Data scale           | Billions of tokens                   | Hundreds to thousands of examples    |
| Weight initialisation| Random                               | From pretrained checkpoint           |
| Goal                 | Learn general language representations | Adapt representations for a specific task |

---

## 4. Model Architecture and Adaptation

### 4.1 Base Model

GPT-2 Small was used as the base model. Its key architectural parameters are:

| Parameter          | Value   |
|--------------------|---------|
| Embedding dim      | 768     |
| Transformer layers | 12      |
| Attention heads    | 12      |
| Context length     | 1,024   |
| Vocabulary size    | 50,257  |
| Total parameters   | 124.4M  |

Pretrained weights were loaded from OpenAI's publicly released checkpoint using the `gpt_download` utility from the *Build a Large Language Model from Scratch* companion repository.

### 4.2 Structural Modification

Only one structural change was made to the model:

```
Original:  out_head = Linear(768, 50257, bias=True)   ← language modelling head
Modified:  out_head = Linear(768, 2,     bias=False)  ← classification head
```

The new head uses no bias term, which is standard practice for classification heads attached to large pretrained models. All other layers remain architecturally identical to the pretrained GPT-2 Small; only their parameter values are modified (or left unchanged) during training depending on the freezing strategy applied.

---

## 5. Impact of Freezing Strategies on Performance

Two distinct fine-tuning strategies were implemented and compared to understand how the number of trainable parameters affects both efficiency and final performance.

### 5.1 Strategy 1 - Selective Freezing

In this strategy, the vast majority of the model's parameters are frozen their gradients are set to zero and they receive no updates during training. Only the following components are left trainable:

- The **last transformer block** (block index 11 of 12)
- The **final layer normalisation** (`final_norm`)
- The new **classification head** (`out_head`)

This results in approximately **7.1 million trainable parameters**, representing just **5.7%** of the full model.

**Rationale:** The lower layers of a pretrained transformer encode general-purpose, low-level linguistic features (tokenisation patterns, syntactic structure) that are unlikely to need updating for a downstream classification task. The upper layers encode more abstract, task-adaptable representations that benefit from fine-tuning. By freezing everything except the top layer and head, training is faster, memory usage is lower, and the risk of **catastrophic forgetting** - where fine-tuning overwrites valuable pretrained knowledge in the lower layers is significantly reduced.

**Learning rate:** `5e-5`
**Training time:** ~1 minute
**Test accuracy:** 95.33%
**Test F1:** ~0.953

### 5.2 Strategy 2 - Full Fine-tuning

In this strategy, all **124.4 million parameters** are updated during training. No layers are frozen. A lower learning rate is used to prevent instability when applying gradients to the entire model simultaneously. Full fine-tuning gives the model maximum flexibility to adapt its representations to the spam classification task, but at the cost of longer training time, higher memory usage, and a greater risk of overfitting on a small dataset.

**Learning rate:** `1e-5` (lower to maintain stability across all 12 layers)
**Training time:** ~2.6 minutes
**Test accuracy:** 95.67%
**Test F1:** ~0.957

### 5.3 Comparison and Impact

| Strategy           | Trainable Params | % of Model | Training Time | Test Accuracy | Test F1 | Relative Speed |
|--------------------|------------------|------------|---------------|---------------|---------|----------------|
| Selective Freezing | ~7.1M            | 5.7%       | ~1 minute     | 95.33%        | ~0.953  | 3x faster      |
| Full Fine-Tuning   | 124.4M           | 100%       | ~2.6 minutes  | 95.67%        | ~0.957  | baseline       |

The accuracy difference between the two strategies is just **0.34 percentage points** - well within the margin of noise for a test set of 299 examples. Despite training on **17x fewer parameters**, selective freezing matches full fine-tuning almost exactly in both accuracy and F1.

This result has a clear practical implication: for small classification tasks built on large pretrained models, the upper layers already contain most of the task-relevant representations. Updating the entire network adds compute cost and overfitting risk without delivering meaningful accuracy gains. Selective freezing is the more efficient and equally effective choice for this dataset and task.

Both strategies produced smooth training curves with no evidence of divergence or overfitting, which is likely a consequence of the balanced dataset and the regularising effect of AdamW weight decay.

---

## 6. Training Setup

| Hyperparameter       | Value              |
|----------------------|--------------------|
| Optimiser            | AdamW              |
| Weight decay         | 0.1                |
| Epochs               | 5                  |
| Batch size           | 8                  |
| Evaluation frequency | Every 50 steps     |
| Random seed          | 123                |
| Hardware             | NVIDIA T4 (Colab)  |

**AdamW** was chosen because it decouples weight decay from the gradient update, which is the standard optimiser for fine-tuning transformer models. The weight decay of 0.1 provides regularisation, which is especially important when training on a small dataset of 1,046 examples. Loss, accuracy, and F1 were evaluated periodically during training on small subsets of the train and validation loaders for efficiency, with full-dataset evaluation performed at the end of training on all three splits.

---

## 7. Results and Analysis

### 7.1 Confusion Matrix and Error Analysis

The confusion matrix on the test set reveals the nature of each model's errors. The key distinction is their practical impact in a deployed filter:

- **False Positives (ham predicted as spam)** - A legitimate message is incorrectly flagged. In a deployed spam filter, this means the user misses a real message. This is typically the more disruptive error type.
- **False Negatives (spam predicted as ham)** - A spam message slips through undetected. Less disruptive but undermines the filter's core purpose.

Examining the actual misclassified messages (displayed in the notebook's error analysis section) reveals that most errors occur on messages with **ambiguous vocabulary** short messages containing promotional language that could plausibly appear in either class, or informal messages that superficially resemble spam trigger patterns without actually being spam.

### 7.2 Metric Discussion

Both accuracy and macro-averaged F1 are reported. Accuracy alone can be misleading even on a balanced dataset if the model has a systematic bias toward one class. F1 penalises that bias more directly by averaging precision and recall across both classes. The close alignment between accuracy and F1 scores for both strategies confirms that neither model developed a class preference during training.

---

## 8. Model Strengths and Weaknesses

### 8.1 Strengths

**Strong performance on clear-cut spam** - The model reliably identifies messages with overt spam signals: prize-winning notifications, urgent account warnings, embedded phone numbers in unusual formats, and explicit calls to action ("Text NOW", "Click here", "Reply to claim"). These patterns are lexically distinctive and GPT-2's pretrained representations, built on a broad corpus of web text, already encode associations between this language and suspicious content.

**Efficiency of selective freezing** - Achieving 95.33% test accuracy while training only 5.7% of the model's parameters demonstrates that pretrained representations are remarkably transferable. For resource-constrained environments, selective freezing provides near-full-model performance at a fraction of the time and memory cost. This is a practically important result for deployment scenarios.

**Balanced training prevents majority-class bias** - By downsampling ham to match spam, the model was prevented from learning the trivial shortcut of predicting "ham" for every input. Both classes are treated with equal importance during training, which is reflected in the high F1 scores a metric that penalises class-skewed predictions more strongly than accuracy alone.

**Stable training dynamics** - The use of AdamW with weight decay and carefully chosen, strategy-appropriate learning rates produced smooth loss curves with no instability or divergence across either strategy or either split.

### 8.2 Weaknesses

**Borderline promotional messages** - Legitimate marketing texts from known companies frequently share vocabulary with spam: "limited time offer", "exclusive deal", "click to redeem". Without sender metadata or historical context which a real spam filter would have access to the model must rely solely on raw message text, and may misclassify these borderline cases as spam.

**Very short messages** - The model uses the final token's hidden state to represent the entire message. For messages of only 2-5 words, the transformer has very little input to aggregate, and the resulting representation may be insufficiently informative for a reliable classification decision. This is a known limitation of the last-token-as-classifier approach.

**Dataset vintage and distribution shift** - The SMS Spam Collection was compiled in the mid-2000s. The spam landscape has changed considerably since: modern attacks use URL shorteners, impersonate trusted institutions, and employ adversarial rephrasing to evade keyword-based filters. A model trained on this dataset may generalise poorly to these newer patterns without retraining on more recent examples.

**No out-of-distribution evaluation** - The model was only evaluated on held-out examples from the same dataset and distribution it was trained on. Its performance on email spam, social media spam, or messaging platform spam is unknown and likely lower, as those domains differ significantly in register, length, and formatting conventions.

**Binary label limitations** - Real-world spam classification is rarely a clean binary problem. Subscription alerts, automated notifications, and marketing messages from companies the user has previously engaged with occupy a grey zone that a strict ham/spam label cannot adequately represent. A model trained with this binary framing inherits its limitations and cannot express uncertainty about ambiguous cases.

---

## 9. Key Takeaways

**1. Pretrained representations are powerful and transferable.**
GPT-2 was never trained to classify spam, yet fine-tuning just 5.7% of its parameters the top transformer block and a new output head is sufficient to achieve 95.33% test accuracy. This demonstrates that the linguistic representations learned during pretraining on general web text encode features directly useful for downstream classification, without any task-specific pretraining.

**2. Selective freezing is the pragmatic choice for small datasets.**
When labelled data is scarce, updating the full model risks overfitting and wastes compute. Selective freezing constrains adaptation to the most task-relevant parts of the model, achieving near-identical performance to full fine-tuning in one-third of the training time and with a significantly smaller memory footprint.

**3. Classification fine-tuning is a fundamentally different paradigm from pretraining.**
Pretraining teaches the model to generate to predict what comes next across a vast vocabulary. Classification fine-tuning redirects that knowledge toward discrimination deciding which category a whole input belongs to. The model moves from being a text producer to a text judge, with a simpler output structure but a more constrained learning signal.

**4. Dataset quality and balance matter as much as model choice.**
The original dataset's 86/14 imbalance would have produced a misleadingly high accuracy on a model that simply predicts "ham" every time. Addressing this through downsampling and stratified splitting ensured that accuracy and F1 reflect genuine classification capability rather than artefacts of class distribution.
