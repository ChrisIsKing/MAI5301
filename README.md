### Assignment #5 Reflections

## 1. Dataset

The **UCI SMS Spam Collection** contains 5,572 labelled messages, but the original dataset is heavily imbalanced at 86.6% ham and 13.4% spam. To fix this, the dataset was downsampled to a balanced **1,494 examples** (747 spam / 747 ham).

The balanced dataset was then split as follows:

| Split      | Proportion | Examples (approx.) |
|------------|------------|---------------------|
| Training   | ~70%       | ~1,046              |
| Validation | ~10%       | ~149                |
| Test       | ~20%       | ~299                |

All messages were tokenized using **tiktoken** and padded or truncated to a fixed length of **120 tokens**.

---

## 2. Approach

GPT-2's language modelling head was swapped out for a **2-class linear output layer** to turn it into a binary classifier. Two fine-tuning strategies were then compared.

### 2.1 Selective Freezing

With selective freezing, most of the model was left unchanged. Only the **last transformer block**, the **final layer norm**, and the **classification head** were trained, which comes to roughly **7.1 million parameters** or about **5.7%** of the full model. This finished training in about **1 minute** and reached a test accuracy of **95.33%**.

### 2.2 Full Fine-Tuning

Full fine-tuning updated all **124.4 million parameters**. A lower learning rate was used to keep training stable across the whole model. It took around **2.6 minutes** and achieved a slightly higher test accuracy of **95.67%**.

---

## 3. Results Summary

| Strategy           | Parameters Updated | Training Time | Test Accuracy |
|--------------------|-------------------|---------------|---------------|
| Selective Freezing | ~7.1M (5.7%)      | ~1 minute     | 95.33%        |
| Full Fine-Tuning   | 124.4M (100%)     | ~2.6 minutes  | 95.67%        |

---

## 4. Key Takeaway

Both approaches ended up at almost the same accuracy, with only a **0.34 percentage point** difference. Selective freezing is about **3x faster**, uses less memory, and is less likely to overfit on a small dataset like this one. Full fine-tuning did not offer any meaningful improvement to justify the extra time and compute.

For small classification tasks using a large pre-trained model, selective freezing is the more practical choice.