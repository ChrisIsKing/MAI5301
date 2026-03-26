### Problem Addressed and Problem Importance
Past attempts to forecast AI’s labor-market effects have produced conflicting or poorly predictive results (offshorability studies, robot exposure measures, occupational forecasts). A reliable, forward-looking measure is needed to identify which jobs are most exposed before large-scale displacement becomes visible.

### State of Related Works in This Topic
Earlier work relied on theoretical exposure ratings or expert forecasts that often failed to predict actual outcomes. Studies on trade shocks, robots, and offshorability showed mixed or debated results. No prior framework combined theoretical LLM capability estimates with real-world usage data at the task level.

### Proposed Solution
The authors introduce “observed exposure,” a new measure that weights theoretical LLM task coverage (from Eloundou et al., 2023) by actual Claude usage data from the Anthropic Economic Index. They map this to O*NET tasks, aggregate to occupations, and compare with BLS growth projections. Key findings: AI exposure is concentrated in specific occupations; higher-exposed jobs are still projected to grow through 2034; there is limited evidence of unemployment increases since late 2022, though hiring of younger workers in exposed occupations appears to have slowed. Workers in the most exposed professions tend to be older, female, more educated, and higher-paid.

### Drawbacks and Limitations
The measure relies on usage data from one provider (Anthropic) and captures only early 2025 patterns. It reflects task coverage rather than full automation or job creation effects. The observation window is still short, making strong causal claims difficult.

### Future Research
Periodic re-measurement as AI usage grows, incorporation of data from additional providers, and deeper analysis of skill shifts, wage effects, and new job creation within exposed occupations. Extending the framework to track actual displacement versus augmentation over longer horizons will be critical.

### References
Massenkoff, M., & McCrory, P. (2026, March 5). Labor market impacts of AI: A new measure and early evidence. Anthropic. https://cdn.sanity.io/files/4zrzovbb/website/2b5bbaf2c1eb81dbf6e6fb813c1a24e35a64d376.pdf