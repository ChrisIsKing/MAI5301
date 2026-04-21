### ReAct: Synergizing Reasoning and Acting in Language Models

#### Problem Addressed
Large language models have two core capabilities which are reasoning (like chain-of-thought prompting) and acting (like generating action plans). However, these two capabilities do not act in synergy. The issue addressed is that models using chain-of-thought alone cannot pull information from external sources, they rely solely on knowledge gathered during the pretraining and finetuning phases. This restriction leads to hallucination and the propogation of errors at different reasoning steps. In "acting", models that only produce actions have no mechanism of producing a sequence of reasoning steps, reason through that plan, or backpropagating when it encounters an error in reasoning. The researchers proposed that interleaving reasoning and acting together in a single framework could let the model do both at once, using reasoning to guide actions, and using the results of actions to inform further reasoning.

#### State of Related Works
At the time of this paper, the two dominant paradigms were chain-of-thought prompting and action generation, and they were studied separately. Chain-of-thought allowed models to produce step-by-step reasoning that improved performance on multi-step tasks. Action generation methods, like those used in WebGPT, let models interact with environments and external tools, but without a reasoning component they couldn't abstract high level goals or maintain a working memory. Neither approach was capable of doing both at the same time.

#### Proposed Solution and Key Insights
The researchers proposed ReAct, which is a prompting paradigm that interleaves reasoning and action. The key insight is that reasoning and acting aren't competing objectives, they're complementary and should work together. This is similar to how humans perform multi step tasks in everyday life. Reasoning traces update the model's internal state, helping it plan and track what it's doing. Actions, on the other hand, interact with external sources like Wikipedia or a game environment and return observations that feed back into the reasoning process. This creates a loop, where the model thinks, then acts, then receives an observation, then thinks again. When applied to question answering and fact verification, ReAct used a Wikipedia API to collect information, thereby significantly reducing hallucinations compared to chain-of-thought alone. On decision-making benchmarks, ReAct also outperformed imitation and reinforcement learning methods by 34% and 10% respectively in success rate, using just one or two in-context examples.

#### Drawbacks and Limitations
Due to the lenghty process of reasoning, grabbing information from external sources, processing it, then calculating the next steps, a lot of token is used up. ReAct is not token efficient and may not be suitable for large multi-step tasks or using on models with small context windows.

#### Future Directions
The paper explicitly mentioned that future research can explore how to make this process more token efficient. 



### Reflexion: Language Agents with Verbal Reinforcement Learning

#### Problem Addressed
LLM-based agents that interact with environments, like in games, compilers, or APIs. They however struggle to learn efficiently from mistakes committed and the corrections given to those mistakes. The issue addressed is that traditional reinforcement learning requires either extensive training samples or expensive model fine-tuning improve agent behavior, neither of which is feasible when you're working with a large, already pretrained model. The researchers proposed that instead of updating model weights, you could teach an agent to improve by having it verbally reflect on what went wrong and store those reflections as memory. This is essentially like reinforcement learning during prompting.

#### State of Related Works
At the time of this paper, the dominant approach for improving LLM agent behavior was in-context learning, where users would provide few-shot examples to guide the model. Methods like ReAct, SayCan, and WebGPT had shown that LLMs could make decisions and take actions in environments, but they had no mechanism for learning from failure across multiple attempts. If the agent made the same mistake repeatedly, it would keep making it, because nothing in the pipeline updated based on prior outcomes. Some kind of reinforcement learning was needed, however, traditional reinforcement learning required running thousands of training episodes and updating of the model parameters, which was computationally expensive at the large scale of these models.

#### Proposed Solution and Key Insights
The researchers proposed Reflexion, which uses three components working together:
- An Actor - that generates actions and text
- An Evaluator - that scores those outputs
- A Self-Reflection model - that analyzes what went wrong and writes a verbal explanation in the first person. 

The self-reflection is stored in a memory buffer and is provided to the Actor as additional context on the next prompt or attempt at solving a task. The key insight here is that the "weight update" in traditional RL is replaced by a memory, or a summary, guiding it to perform a given task in a diffrent way. The agent is essentially writing its own lesson from each failure. Reflexion doesn't require any gradient updates, any additional training data, or an additional model to correct it, it reuses the same LLM to reflect on its own behavior. 

Reflexion agents outperformed strong baselines where it achieved a 22% improvement on AlfWorld decision-making tasks over 12 iterative steps, 20% improvement on HotPotQA reasoning, and up to 11% improvement on Python programming tasks in HumanEval.

#### Drawbacks and Limitations
The reflective approach depends on the evaluator function accurately identifying when something went wrong. If the reward signal is noisy or the Evaluator is unreliable, the reflections generated will be based on bad feedback and may not actually help. 

#### Future Directions
Reflexion can be used to evaluate and fine-tune models, as an improvement for the manual human/LLM evaluation then reinforcement feedback process currently used