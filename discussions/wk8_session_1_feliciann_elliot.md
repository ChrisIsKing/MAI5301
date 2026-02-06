### Problem Addressed and Problem Importance

The paper is trying to fix a pretty common failure mode in LLMs: they often “sound confident” while committing early to one line of reasoning, even when the task clearly needs exploration, backtracking, and planning (Yao et al., 2023). In normal decoding, the model picks a path token by token, and once it drifts, it usually keeps drifting. That matters because a lot of real problems are not solved by one clean straight-line thought. They are solved by trying options, comparing them, and changing direction when something doesn’t work.

### State of Related Works in This Topic

Most existing prompting methods still behave like a single-track attempt. You might do input–output prompting, or you might add a chain-of-thought, but you are still mostly riding one trajectory (Yao et al., 2023). Search methods exist in AI, but the “search heuristics” are typically hand-programmed or learned in specialized ways. What this paper leans into is the idea that the language model itself can generate candidate steps and also judge progress, so search becomes something you can run in-language instead of outside the model (Yao et al., 2023). 

### Proposed Solution

They propose Tree of Thoughts (ToT), where the model doesn’t just produce one long completion. Instead, it produces intermediate chunks they call “thoughts,” and these thoughts become nodes in a tree (Yao et al., 2023). The key move is that ToT keeps multiple candidate thoughts alive, evaluates them, and then uses a search strategy like breadth-first search or depth-first search to explore and prune the tree, including lookahead and backtracking (Yao et al., 2023). 

The motivation is simple: if you treat reasoning as a search problem, you can compare partial solutions instead of gambling everything on the first decent-sounding step. They show this setup helps on tasks that are naturally “search-y,” like the Game of 24, creative writing with constraints, and crosswords, where committing too early is basically asking to fail (Yao et al., 2023). 

### Drawbacks and Limitations

ToT leans heavily on the model’s ability to self-evaluate intermediate thoughts. If the model’s internal judging is weak or biased, it can prune good paths and keep bad ones. Also, search costs add up fast. Keeping many branches, generating many thoughts, and scoring them is more expensive than a single pass of decoding, so you usually pay for the extra reliability with extra compute and latency (Yao et al., 2023).

### Future Research

A natural next step is making the evaluation side stronger and more stable, so the search is guided by something more trustworthy than the same model that produced the candidates in the first place. Another direction is figuring out when ToT is worth the overhead and when it is not, because not every task needs search. Finally, there’s room to connect ToT-style inference to training, so models get better at generating “useful” thoughts and better at judging them, instead of relying on fragile prompting alone (Yao et al., 2023).

### References
Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., & Narasimhan, K. (2023, May 17). Tree of Thoughts: Deliberate Problem Solving with Large Language Models. arXiv.org. https://arxiv.org/abs/2305.10601