### Tree of Thoughts: Deliberate Problem Solving with Large Language Models

#### Problem Addressed
LLMs are autoregressive, generating tokens one at a time based on some reasoning path. The issue addressed is that this process is sequential in nature and cannot backtrack to correct mistakes in reasoning. Consequentially, LLMs do not perform well on tasks that where strategic lookahead is required. Or where decisions made early on forces you to pivot to another reasoning path - tasks such as completing a crossword puzzle, or sudoko. The researchers proposed that models need the ability to explore multiple reasoning paths, evaluate them, and backtrack when necessary.

#### State of Related Works
At the time of this paper, Chain-of-Thought (CoT) prompting was the dominant method for improving reasoning. Specfically COT and self-consistency with COT. However, both approaches were still fundamentally sequential, where reasoning paths were generated with thought after another, without the ability to branch out, compare alternatives, or abandon a failing path. The model couldn't detect early on that the reasoning path it's currently on doesn't make sense and pivot to another branch.

#### Proposed Solution and Key Insights
The researchers proposed Tree of Thoughts (TOT), which, instead of chains of reasoning, created branches, where each branch leads to a differnt reasoning approach. It is not linear in nature like COT. In TOT, the model can generate diverse thoughts at each step, and the model can evaluate how promising each thought is and prune if it is unnecessary. It uses classical search algorithms such as breadth first search or depth first search to explore and evaluate thoughts on the tree.

The researchers found that TOT is a promising prompting method and it improved performance on tasks requiring non trivial planning. On the Game of 24, GPT4 with COT only solved 4% of tasks, while TOT achieved 74%. They also tested on Creative Writing and Mini Crosswords with similar improvements.

#### Drawbacks and Limitations**
The authors addressed directly that TOT is computationally expensive because you're generating and evaluating significantly more outputs than standard prompting. For simple tasks where COT already works well, the extra cost isn't justified.

#### Future Directions
As discussed in class, future works could explore how biases are either increased or reduced while prompting using TOT.


### Let's Verify Step by Step

#### Problem Addressed
State of the art models still hallicunate. The issue addressed is that when training reward models to detect these mistakes, we have two choices: outcome supervision (only checking if the final answer is correct) or process supervision (checking each intermediate reasoning step). Outcome supervision is simpler to collect but has a fundamental problem where models can reach correct answers through incorrect reasoning, and you'd never catch that. The researchers proposed that process supervision should significantly outperform outcome supervision, especially on challenging multi step reasoning tasks.

#### State of Related Works
At the time of this paper, outcome supervision was the dominant approach because it's much cheaper to collect. You just need to know if the final answer is right or wrong.

#### Proposed Solution and Key Insights
The researchers conducted a comparison using GPT 4 as the base model for verifying outputs. They trained two types of reward models, an Outcome Reward Model (ORM) that only looks at final answers, and a Process Reward Model (PRM) that evaluates each step in the reasoning chain.
The researchers found that process supervision significantly outperformed outcome supervision. Their process supervised model solved 78% of problems from the MATH test set. More importantly, the performance gap widened as they considered more candidate solutions, showing that the PRM is more reliable at distinguishing good solutions from bad ones.

#### Drawbacks and Limitations
The authors addressed directly that collecting process supervision is expensive because you need humans to evaluate each step, not just the final answer. They also noted that it's unknown how broadly these results generalize beyond math. Mathematical reasoning has clear right or wrong steps, but other domains may have more subjective intermediate reasoning.

#### Future Directions
Future work should explore whether process supervision generalizes to other domains and how to reduce the cost of collecting step-level feedback.
