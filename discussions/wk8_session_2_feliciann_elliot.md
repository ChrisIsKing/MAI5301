### Problem Addressed and Problem Importance

This paper focuses on a more grounded issue: even when LLMs write step-by-step solutions, they still slip in logical errors, and one bad step can wreck the whole answer (Lightman et al., 2023). If you only score the final answer, you often miss where the reasoning went off the rails. That’s a big deal for math, logic, and any domain where correctness is not forgiving.

### State of Related Works in This Topic

A lot of recent work uses reward models and selection methods, either inside RL pipelines or to pick the best answer out of many samples (Lightman et al., 2023). But reward models themselves depend on how you supervise them. Prior comparisons looked at outcome supervision versus process supervision, and in some easier settings the gap did not look dramatic. This paper re-tests that question in a harder regime, using more feedback and a more challenging benchmark (Lightman et al., 2023). 

### Proposed Solution

The core proposal is straightforward: train reward models with process supervision, meaning humans label whether each intermediate step is correct, instead of only labeling whether the final answer is correct (Lightman et al., 2023). The paper argues process supervision gives cleaner credit assignment because it tells you exactly where the mistake happens, rather than leaving the reward model to guess which step caused the failure (Lightman et al., 2023). 

They show process supervision works better than outcome supervision for selecting correct solutions from many generated candidates. In their main result summary, they report that process supervision significantly outperforms outcome supervision on a representative subset of the MATH test set, and they also release PRM800K, a large dataset of step-level human feedback used to train the best reward model (Lightman et al., 2023). 

Two implementation details matter for why this works in practice. First, they define a single score for a full solution by combining step-level correctness scores, and they treat the “probability every step is correct” as a useful overall signal (Lightman et al., 2023). 

Second, they use active learning to focus labeling effort on the most informative solutions, improving data efficiency rather than labeling blindly at scale (Lightman et al., 2023).

### Drawbacks and Limitations

The obvious limitation is cost and practicality. Outcome supervision can sometimes be automated (like checking a final numeric answer), but step-level supervision usually needs humans, which is expensive and slow (Lightman et al., 2023). 

Also, their design choice to supervise only up to the first incorrect step keeps labeling manageable, but it still doesn’t magically solve the general “human feedback is costly” proble(Lightman et al., 2023). 

Another limitation is scope. Their strongest evidence is in mathematical reasoning, and they explicitly raise the question of how broadly these gains generalize beyond math-heavy tasks (Lightman et al., 2023). 

### Future Research

Future work basically writes itself. One direction is extending process supervision beyond math into other domains where mistakes are harder to automatically verify. Another is improving active learning and iterative retraining, because the paper notes instability when trying to retrain the selector model over rounds, but they still see it as a promising path (Lightman et al., 2023). 

Finally, there’s a bigger alignment angle: they argue process supervision can be easier to interpret and may better reward “doing the right reasoning,” not just landing on the right outcome, but it needs more evidence across tasks to become a general claim (Lightman et al., 2023). 

### References
Lightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J., Schulman, J., Sutskever, I., & Cobbe, K. (2023, May 31). . arXiv.org. https://arxiv.org/abs/2305.20050