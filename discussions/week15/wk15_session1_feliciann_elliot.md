### Problem Addressed and Problem Importance
Autonomy in AI agents is a double-edged sword: it unlocks transformative capabilities like proactive task execution and multi-step workflows, but it also amplifies risks around safety, accountability, human deskilling, and unintended consequences. Developers need a practical way to deliberately calibrate an agent’s level of autonomy rather than treating full autonomy as the inevitable endpoint of increasing model capability.

### State of Related Works in This Topic
Prior frameworks in robotics and human-AI interaction often treat autonomy as “the ability to operate without human input for a protracted period,” but they rarely separate it from raw capability or provide actionable design guidance for LLM-powered agents. Existing scaling policies and alignment work (e.g., HHH frameworks) focus on model behavior during training rather than runtime user involvement. No standardized, user-centered taxonomy existed that treats autonomy as an independent design lever across single- and multi-agent settings.

### Proposed Solution
The authors introduce a five-level framework centered on the user’s role when interacting with an agent:

L1: User as Operator — user directs and makes decisions; agent acts on command.
L2: User as Collaborator — user and agent jointly plan, delegate, and execute.
L3: User as Consultant — agent leads but consults the user for expertise or preferences.
L4: User as Approver — agent acts autonomously except in risky or pre-specified scenarios.
L5: User as Observer — agent operates with full autonomy under passive monitoring.

For each level they describe concrete control mechanisms, open design questions, and example interactions. They further propose autonomy certificates as a governance tool that third-party bodies could issue to communicate an agent’s behavioral constraints to developers and other agents.

### Drawbacks and Limitations
The framework is conceptual and forward-looking; it has not yet been validated on large numbers of deployed agents. It assumes developers will choose lower autonomy when appropriate, which may not hold in highly competitive commercial environments. Evaluation methods for autonomy (separate from capability) remain preliminary.

### Future Research
Developing rigorous evaluation protocols that let users collaborate with agents on test tasks, integrating autonomy certificates into multi-agent systems, and empirically testing how different autonomy levels interact with capability scaling and cross-agent coordination. Extending the framework to physical agents and long-term societal impacts will also be valuable.

### References
Feng, K. J. K., McDonald, D. W., & Zhang, A. X. (2025, June 14). Levels of autonomy for AI agents. arXiv.org. https://arxiv.org/abs/2506.12469
