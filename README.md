# MAI5301: Foundations of Large Language Models @UG

* Course Code: MAI5301
* Course Name: Foundations of Large Language Models
* Credits: 4
* Sessions: Tuesday & Thursday 5:00 pm – 6:30 pm (PDT) / 9:00 pm – 10:30 pm (GYD)
* Duration: 15 weeks
* Teaching Modality: Online

### Team

| Member | Role | Office Hours |
| :------ | :--- | :----------- |
| Dr. Christopher Clarke | Faculty | [**Book Appointment**](https://calendar.app.google/qXCTEfyjZ2utKQDg8) |

📌 **Presentation Review Sessions**: All students must submit their presentation slides and schedule a review session with the instructor **before** presenting. Use the booking link above to schedule your review.

### Communication
**ALL** communication regarding this course must be via GitHub Issues and email.
This includes questions, discussions, announcements, as well as private messages.

Presentation slides and paper summaries will be submitted via a pull request to this repository.

## Course Description
This course provides students with an in-depth understanding of generative AI through state-of-the-art language models, focusing on transformers and models like ChatGPT. Through comprehensive technical study, students will delve into algorithmic, systems-level, and theoretical aspects of these models, while gaining hands-on experience building LLM components from scratch.

We will start with foundational concepts of language models and transformers, then take a deep dive into the technical aspects of large language models. Our topics will include: transformer architecture, attention mechanisms, pre-training objectives, scaling laws, fine-tuning methods, alignment techniques, and safety considerations. We will cover LLM topics primarily from top conferences in machine learning and natural language processing.

Note that this course **focuses on both AI methods and implementation**. Students will gain theoretical understanding while building practical skills through progressive coding assignments that implement LLM components from scratch.

### Prerequisites
Students are expected to have:
* Strong programming background (Python preferred)
* Linear algebra and probability theory
* Basic understanding of neural networks
Having prior experience with deep learning frameworks (PyTorch/TensorFlow) is helpful but not required.

### Textbook
This course has no required textbook.
We will read recent papers from top venues including ACL, EMNLP, NAACL, ICML, NeurIPS, ICLR, and other conferences to understand current trends in large language models.

## Tentative Schedule and Reading List

*This is an evolving list and subject to changes due to the rapid pace of LLM developments.*

| Date | Topics/Readings | Presenter |
| :---- | :---- | :---- |
| Week 1 | **Introduction to Language Models and Transformers** | Dr. Clarke |
|  | [How to Read a Paper](http://svr-sk818-web.cl.cam.ac.uk/keshav/papers/07/paper-reading.pdf) (Required) |  |
|  | [Attention is All You Need](https://arxiv.org/abs/1706.03762) (Required) |  |
|  | [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) (Required) |  |
| Week 2 | **Fundamentals of Transformers and Research Paper Reading** | Dr. Clarke |
|  | [How to Give a Bad Talk](http://www.cs.berkeley.edu/~pattrsn/talks/BadTalk.pdf) (Required) |  |
|  | [Writing Reviews for Systems Conferences](http://people.inf.ethz.ch/troscoe/pubs/review-writing.pdf) (Required) |  |
|  | **Pre-training & Scaling** |  |
| Week 3 (Tue) | [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) (Required) | Daryl Nelson |
|  | [Training Compute-Optimal Large Language Models (Chinchilla)](https://arxiv.org/abs/2203.15556) (Required) |  |
| Week 3 (Thu) | [Emergent Abilities of Large Language Models](https://arxiv.org/abs/2206.07682) (Required) | Hilton Sarius |
|  | [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) (Required) |  |
| Week 4 (Tue) | [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) (Required) | Maryam Bacchus |
|  | [Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM](https://arxiv.org/abs/2104.04473) (Required) |  |
| Week 4 (Thu) | [Dolma: An Open Corpus of Three Trillion Tokens for LLM Pretraining Research](https://arxiv.org/abs/2402.00159) (Required) | Feliciann Elliot |
|  | [The Pile: An 800GB Dataset of Diverse Text for Language Modeling](https://arxiv.org/abs/2101.00027) (Required) |  |
|  | **Model Architectures** |  |
| Week 5 (Tue) | [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961) (Required) | Daryl Nelson |
|  | [Mixtral of Experts](https://arxiv.org/abs/2401.04088) (Required) |  |
| Week 5 (Thu) | [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135) (Required) | Hilton Sarius |
|  | [Longformer: The Long-Document Transformer](https://arxiv.org/abs/2004.05150) (Required) |  |
| Week 6 (Tue) | [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864) (Required) | Maryam Bacchus |
|  | [Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation (ALiBi)](https://arxiv.org/abs/2108.12409) (Required) |  |
| Week 6 (Thu) | [GLU Variants Improve Transformer (SwiGLU)](https://arxiv.org/abs/2002.05202) (Required) | Feliciann Elliot |
|  | [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245) (Required) |  |
|  | **Alignment & Instruction Tuning** |  |
| Week 7 (Tue) | [Training language models to follow instructions with human feedback (InstructGPT)](https://arxiv.org/abs/2203.02155) (Required) | Daryl Nelson |
|  | [Scaling Instruction-Finetuned Language Models (FLAN)](https://arxiv.org/abs/2210.11416) (Required) |  |
| Week 7 (Thu) | [Direct Preference Optimization: Your Language Model is Secretly a Reward Model (DPO)](https://arxiv.org/abs/2305.18290) (Required) | Hilton Sarius |
|  | [KTO: Model Alignment as Prospect Theoretic Optimization](https://arxiv.org/abs/2402.01306) (Required) |  |
|  | **Reasoning & "System 2" Thinking** |  |
| Week 8 (Tue) | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) (Required) | Maryam Bacchus |
|  | [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171) (Required) |  |
| Week 8 (Thu) | [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) (Required) | Feliciann Elliot |
|  | [Let's Verify Step by Step (Process Reward Models)](https://arxiv.org/abs/2305.20050) (Required) |  |
|  | **Inference Economics** |  |
| Week 9 (Tue) | [Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM)](https://arxiv.org/abs/2309.06180) (Required) | Daryl Nelson |
|  | [Flash-Decoding: Faster Attention for Long Context Inference](https://crfm.stanford.edu/2023/10/12/flashdecoding.html) (Required) |  |
| Week 9 (Thu) | [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192) (Required) | Hilton Sarius |
|  | [Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads](https://arxiv.org/abs/2401.10774) (Required) |  |
|  | **Evaluation & Benchmarks** |  |
| Week 10 (Tue) | [Measuring Massive Multitask Language Understanding (MMLU)](https://arxiv.org/abs/2009.03300) (Required) | Maryam Bacchus |
|  | [Holistic Evaluation of Language Models (HELM)](https://arxiv.org/abs/2211.09110) (Required) |  |
| Week 10 (Thu) | [Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference](https://arxiv.org/abs/2403.04132) (Required) | Feliciann Elliot |
|  | [AlpacaEval: An Automatic Evaluator of Instruction-following Models](https://github.com/tatsu-lab/alpaca_eval) (Required) |  |
|  | **Agents & Agentic Systems** |  |
| Week 11 (Tue) | [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) (Required) | Daryl Nelson |
|  | [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) (Required) |  |
| Week 11 (Thu) | [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) (Required) | Hilton Sarius |
|  | [Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334) (Required) |  |
| Week 12 (Tue) | [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) (Required) | Maryam Bacchus |
|  | [CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Society](https://arxiv.org/abs/2303.17760) (Required) |  |
| Week 12 (Thu) | [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) (Required) | Feliciann Elliot |
|  | [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) (Required) |  |
| Week 13 (Tue) | [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) (Required) | Daryl Nelson |
|  | [Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070) (Required) |  |
| Week 13 (Thu) | [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks](https://arxiv.org/abs/2404.07972) (Required) | Hilton Sarius |
|  | [AppAgent: Multimodal Agents as Smartphone Users](https://arxiv.org/abs/2312.13771) (Required) |  |
|  | **Safety, Risks & The Future** |  |
| Week 14 (Tue) | [Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566) (Required) | Maryam Bacchus |
|  | [Goal Misgeneralization in Deep Reinforcement Learning](https://arxiv.org/abs/2105.14111) (Required) |  |
| Week 14 (Thu) | [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) (Required) | Feliciann Elliot |
|  | [Red Teaming Language Models to Reduce Harms](https://arxiv.org/abs/2209.07858) (Required) |  |
| Week 15 (Tue) | [GPTs are GPTs: An Early Look at the Labor Market Impact Potential](https://arxiv.org/abs/2303.10130) (Required) | Daryl Nelson |
|  | [Future of Work with AI Agents: Auditing Automation and Augmentation Potential](https://arxiv.org/abs/2506.06576) (Required) | Maryam Bacchus |
| Week 15 (Thu) | [Levels of Autonomy for AI Agents](https://arxiv.org/abs/2506.12469) (Required) | Hilton Sarius |
|  | [Sparks of Artificial General Intelligence: Early experiments with GPT-4](https://arxiv.org/abs/2303.12712) (Required) | Feliciann Elliot |

## Policies

### Honor Code
Academic integrity applies to all activities related to this course.

### Groups
All activities of this course will be performed **individually** due to small class size (4 students).

### Required Reading
Each lecture will have **required readings that everyone must read**.
There will be *optional related readings* that presenters should be familiar with.
They are optional for the rest of the class.

### Student Lectures
The course will be conducted as a seminar starting from Week 3.
Each student will present multiple papers over the course of the semester.
Presentations should cover all required papers for that lecture.
The duration of the presentation should be **at most 45 minutes** with **15 minutes for discussion**.
Presenters should expect questions and interruptions throughout.

In the presentation, you should:

* Provide necessary background and motivate the problem.
* Present the high level idea, approach, and/or insight (using examples, whenever appropriate) in the required reading as well as the additional reading.
* Discuss technical details so that one can understand key details without carefully reading.
* Explain the differences between related works.
* Identify strengths and weaknesses of the required reading and propose directions of future research.

*The slides for a presentation must be submitted via a pull request at least 24 hours prior to the corresponding class.*

### Lecture Summaries
Each student will be assigned to **write summaries for lectures they do not present**.
The student will write a summary for all presented papers (required readings) for that lecture.

A paper summary must address the following questions in sufficient details (1-2 pages):

* What is the problem addressed in the lecture, and why is this problem important?
* What is the state of related works in this topic?
* What is the proposed solution, and what key insight guides their solution?
* What is one (or more) drawback or limitation of the proposal?
* What are potential directions for future research?

*The paper summary must be submitted via a pull request within 24 hours after the presentation.*
**Late reviews will not be counted.**

*Allocate enough time for your reading, write the summary carefully, and include key observations from the class discussion.*

### Post-Presentation Panel Discussion
To foster a deeper understanding of the papers and encourage critical thinking, each lecture will be followed by a panel discussion.
This discussion will involve rotating roles among the students, simulating an interactive and dynamic scholarly exchange.

#### Roles and Responsibilities

1. **The Author**
   - Assignment: The presenting student acts as the paper's author
   - Responsibility: Defend the paper against critiques, answer questions, and discuss potential improvements or extensions, similar to writing a rebuttal during peer review

2. **The Reviewers**
   - Assignment: The other students serve as reviewers
   - Responsibility: Critically assess the papers, pose challenging questions, highlight potential weaknesses, and engage in constructive critique simulating peer review

3. **Audience Participation**
   - Responsibility: All students must submit **one insightful question** for each presented paper before each class and actively participate in the discussion

### Participation
Given the discussion-based nature of this course, participation is required both for your own understanding and to improve the overall quality of the course.
You are expected to attend **all** lectures and participate in class discussions.

### Coding Assignments

This course includes **5 progressive coding assignments** (30% of grade) based on Sebastian Raschka's book **"Build a Large Language Model (From Scratch)"**.

**[View Complete Assignment Details →](assignments/README.md)**

📚 **Book**: [Build a Large Language Model (From Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch) by Sebastian Raschka  
🔗 **Code Repository**: [github.com/rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)

#### Assignment Schedule

| Assignment | Topic | Chapters | Due Date | Weight |
|------------|-------|----------|----------|--------|
| **A1** | Tokenization & Data Preparation | Ch 2 | Sun, Jan 18, 2026 | 5% |
| **A2** | Attention Mechanisms | Ch 3 | Sun, Feb 1, 2026 | 5% |
| **A3** | GPT Model Architecture | Ch 4 | Sun, Feb 15, 2026 | 6% |
| **A4** | Pretraining from Scratch | Ch 5 | Sun, Mar 1, 2026 | 7% |
| **A5** | Advanced Fine-tuning (choice: Classification, Instruction, or LoRA) | Ch 6/7/AppE | Sun, Mar 22, 2026 | 7% |

📌 **Learning Progression**: Starting from tokenization, you'll progressively build up to a complete GPT-style model, train it from scratch, and fine-tune it for specific tasks.

📌 **Implementation Requirements**: All assignments must be implemented from scratch using PyTorch, with clear documentation and explanations. You may reference the book's code but must demonstrate your own understanding.

📌 **Late Policy**: Coding assignments cannot be turned in late unless an extension is granted at least 24 hours before the submission deadline.

📌 **Office Hours**: Make use of office hours for debugging and conceptual questions about the assignments.

## Tentative Grading

| Component | Weight |
| --------- | ------:|
| Paper Presentations | 40% |
| Paper Summaries | 20% |
| Participation | 10% |
| Coding Assignments | 30% |

## Grading System

| Grade | Percentage |
|-------|------------|
| A | 80% - 100% |
| B | 70% - 79% |
| C | 60% - 69% |
| F | < 60% |

## Submission & Academic Integrity

• Submit assignments via GitHub by 11:59 PM (GYD)  
• **Plagiarism Policy**: You may not directly copy code or text without proper attribution  
• **Use of Generative AI**: Allowed as a learning aid for understanding concepts, but all submitted code must be your own implementation with proper documentation  

📌 **Honor Code**: Misuse of generative AI tools or plagiarism will be treated as an academic violation.

## Required Software & Tools

• **Python 3.8+** with packages: PyTorch, NumPy, Matplotlib  
• **Development Environment**: Jupyter Notebooks, VS Code (recommended)  
• **Version Control**: Git and GitHub  
• **Hardware**: GPU access recommended (Google Colab acceptable)  

## Course Resources

### Primary Materials
• Selected research papers from ICML, NeurIPS, ICLR, ACL, and other top-tier venues  
• Course GitHub repository with code templates and examples  

### Supplementary Resources
• Online tutorials and documentation for PyTorch and transformer implementations  
• Technical blogs and educational content on LLM development  
• Open-source transformer implementations for reference  

### Useful Websites
• [Hugging Face](https://huggingface.co/) - Pre-trained models and documentation  
• [Papers with Code](https://paperswithcode.com/) - Latest ML research with implementations  
• [Transformer Circuits](https://transformer-circuits.pub/) - Mechanistic interpretability research  
• [The Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html) - Implementation walkthrough  

## Communication

• **Course Announcements**: Via email and GitHub  
• **Questions**: Use GitHub Issues or email Dr. Clarke  
• **Office Hours**: By appointment  
• **Class Discussions**: Encouraged during and after sessions