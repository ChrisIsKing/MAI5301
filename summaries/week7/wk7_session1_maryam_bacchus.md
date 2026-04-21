### Training language models to follow instructions with human feedback (InstructGPT)

#### Problem Addressed 
Large language models like GPT-3 are trained to predict the next word in a sequence however, this isn't the same as following user instructions. The model might generate fluent text that is unhelpful, untruthful, or harmful. The researchers proposed that aligning language models with human preferences through reinforcement learning could help the model learn what users actually want, rather than just what statistically follows in text.

#### State of Related Works
At the time of this paper, large language models were primarily trained using unsupervised learning on massive text corpora. These models were capable but not aligned with user intent. Supervised fine tuning existed, where models were trained on high quality examples, but it required large amounts of labelled data. The issue with pure supervised learning is that it's expensive to scale where you'll need a human written example for every type of response you want the model to produce. Reinforcement Learning from Human Feedback (RLHF) had been explored in other domains, but it wasn't yet widely adopted for aligning language models.

#### Proposed Solution and Key Insights 
The researchers proposed using reinforcement learning from human feedback (RLHF) to align GPT-3 with human intent. Instead of just predicting text, the model learns what humans prefer through a three step process. First, human labelers wrote preferred responses to prompts, creating example data for supervised fine tuning (SFT). Second, the model generated multiple outputs for the same prompt, and labelers ranked these outputs from best to worst. These rankings trained a reward model to predict human preferences. Third, the SFT model was optimized using proximal policy optimization (PPO) to maximize the reward model's score, with a penalty to prevent the model from diverging too far from the preferred output. This algorithm was intelligently designed to shape the model behaviour rather than requiring labelled data for every scenario.

The researchers found that a 1.3B parameter InstructGPT model was preferred over the 175B GPT-3 model, even though it was 100x smaller. The model also showed improvements in truthfulness and in reducing harmful outputs. The researchers found that RLHF is a viable architecture for aligning language models with human instructions. The approach assisted in the development of ChatGPT and other LLMs. 

#### Drawbacks and Limitations 
The approach requires significant manpower to label the data. As discussed in class, some demographics are subjected to unhealthy work environments to manually label the data needed to train models using RLHF. 

#### Future Directions 
Future work could explore reducing the manpower required for labelling datasets.


### Scaling Instruction Finetuned Language Models

#### Problem Addressed
Similarly to to InstructGPT paper, the researchers aimed to address the issue of models not aligning with user intent. InstructGPT showed that reinforcement learning with human feedback improved output, however, there wasn't enough generalization to unseen tasks.

#### State of Related Works
At the time of this paper, instruction finetuning had been explored with FLAN and T0, which involved training models on specific tasks and instructions. The methods showed promise but were limited in scale. InstructGPT used RLHF to align models with human preferences, which was effective but computationally expensive. Chain-of-thought prompting improved reasoning, but it wasn't integrated into the finetuning process as yet. Additionally, there was no study on the interaction between task scaling, model scaling, and reasoning data in instruction finetuning.

#### Proposed Solution and Key Insights
The researchers proposed scaling instruction finetuning along: number of tasks (1.8K tasks), model size (up to 540B parameters), and chain-of-thought annotations. They combined four task mixtures: Muffin, T0-SF, NIV2, and a new COT mixture containing nine datasets with human written reasoning phrases or chains. 

The researchers found that instruction finetuning scales well with both the number of tasks and the size of the model. Flan PaLM 540B outperformed the PaLM 540B by 9.4% on average. They also found that by adding nine COT datasets into the finetuning mixture improved performance on reasoning evaluations without hurting other tasks. Flan T5 XL 3B also achieved 52.4% on MMLU, performing better than GPT-3 175B with a score of 43.9%. They found that the instruction finetuning improves performance in general purpose prompting, and it improved zero-shot, few-shot, and CoT performance.

#### Drawbacks and Limitations
After a certain point, the researchers found that scaling the number of finetuning tasks shows diminishing returns after a certain point. While both model size and task count help improve performance, the gains from adding more tasks level off. 

#### Future Directions
The researchers recommended building instruction finetuning for all pretrained language models, given the large benefits come with small computational cost.