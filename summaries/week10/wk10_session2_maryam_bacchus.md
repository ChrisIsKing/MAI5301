### Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference

#### Problem Addressed
Evaluating LLMs on real world tasks is difficult because most benchmarks rely on static datasets with fixed answers. The issue addressed is that the static benchmarks do not capture how LLMs would actually perform on open ended, real world questions/scenarios. These tasks are often complex where there could be multiple answers to the same question.

#### State of Related Works
At the time of this paper, the evaluation approaches were either static or human/LLM judge evaluated. Static benchmarks included MMLU, HellaSwag, and GSM-8K, which test language understanding, math, and coding with predefined correct answers. The problem with this however is that these are cheap and reproducible. They were also close ended questions and models could just train on those QA combos before being evaluated. The second approach to evaluation involving human/LLM judges also used fixed questions and answers. These however handled open ended tasks better by allowing outputs to be rated. The limitation with this approach was that rather than a diverse, real world user base, it was limited to a small group of human evaluators or potentially biased LLM judges. The two approaches lacked scalability to many models and consistent ordering across all models.

#### Proposed Solution and Key Insights
The researchers proposed Chatbot Arena, a free web platform where users chat with two anonymous models simultaneously, then vote for whichever response they prefer. The models are anonymous, so users don't know which model is which until after they vote, preventing bias towards some models. The platform collects live, diverse prompts directly from real users, and convert all of these votes into a single ranked leaderboard. For generating the leaderboard however, instead of just counting wins and losses, it estimates each model's strength based on who it beat and who beat it. The researchers also designed a sampling algorithm to select which model pairs to show to users next, creating model matchups to bettwe narrow down rankings. To clean the data, they built a system to flag and remove votes from bots or bad actors. The researchers found that the resulting rankings aligned very closely with expert evaluations, confirming their hypothesis that crowdsourced human preference is a reliable method of evaluating LLMs.

#### Drawbacks and Limitations
Human preferences are inherently noisy, where different users have different standards for what makes a good response, and there's no way to fully control for that at scale. 

#### Future Directions
Future work could explore creating task specific sub leaderboards, for example a coding leaderboard so models are properly evaluated for their strengths in a given area. This would produce more useful rankings than a single score.



### On the Measure of Intelligence

#### Problem Addressed
The issue addressed is that task specific skill is not the same as intelligence. If you give a model enough training data, and enough compute, you can achieve high performance on almost any benchmark, but that doesn't mean the system is actually intelligent. It simply means the system has. The author argued that to actually measure intelligence, you need to account for how much prior knowledge and training experience a system used, and evaluate how efficiently it can acquire new skills, not how skilled it already is at pre trained tasks.

#### State of Related Works
At the time of this paper, intelligent systems were defined differently. Some treated intelligence as having a task specific skill, where they have the ability to perform well at particular games, benchmarks, or domains. Others argued that to measure general cognitive abilities more broadly, tests like IQ were sufficeint. These approaches were not a not a fair basis for comparing humans to AI systems. Neither approach considered the efficiency of skill acquisition, the role of prior knowledge, or the general difficulty of each of the tasks being evaluated.

#### Proposed Solution and Key Insights
Chollet argued that intelligence is "skill acquisition efficiency over a scope of tasks, given the priors and experience a system brings in". The argument is that you can't just look at what a system can do, you have to account for how much it already knew coming in and how much data it needed to get there. If you've memorised every exam question and their answer, allowing you to pass with 100%, that is not intelligence but more of an algorithmic lookup from a database of QA pairs. The researcher proposed Abstraction and Reasoning Corpus (ARC)  benchmark to truly measure intelligence, which he argued is the abilitiy to figure out a task with minimal examples.The ARC benchmark is designed to measure a human like form of general intelligence. Each ARC task shows a few input/output grid pairs that follow some abstract patter or rule. The LLM must figure out the rule and apply it to a new input. The benchmark is deliberately designed to be easy for humans but hard for models that rely on pattern recognition and memorization rather than genuine abstraction.

#### Drawbacks and Limitations
The paper is conceptual and provides no empirical results on how well AI systems actually perform on ARC at the time of publication. It also does not actually evaluate models on the ARC benchmark so there is no way of letting how efficient this method might be when applied in the real world. 

#### Future Directions
The reseacher mentioned that ARC might be easily gamed if given enough examples. Chollet suggested introdcuing a programmatic way of creating new ARC tasks in future studies. 