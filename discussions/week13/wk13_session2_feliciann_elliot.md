### Problem Addressed and Problem Importance

A generalist agent for the web should follow high-level language instructions to complete complex tasks on any real website. Existing datasets use simulated environments or cover only limited sites and tasks making them unsuitable for developing agents that generalize to unseen websites and handle dynamic noisy real-world interactions.

### State of Related Works in This Topic

Prior web and mobile agent datasets operate on pre-specified simplified sites provide low-level step-by-step instructions or rely on cached states that prevent full exploration. They lack diversity in domains websites and interaction patterns and evaluate only surface-form matching rather than functional correctness on authentic dynamic sites.

### Proposed Solution

The authors present Mind2Web the first dataset with over 2350 open-ended high-level tasks from 137 real websites across 31 domains plus crowdsourced action sequences. Full interaction traces webpage snapshots and network traffic are provided for replay. The MINDACT framework first uses a fine-tuned small language model to rank candidate DOM elements then feeds top candidates to a large language model framed as multi-choice question answering for element selection and operation prediction.

### Drawbacks and Limitations

Even the best model achieves only 52 percent step success rate on seen tasks dropping to around 39 percent when generalizing to unseen websites or domains. Overall task success rates remain low because a single error step fails the entire task. Raw HTML is too large for direct LLM input and models struggle with complex navigation and grounding in varying website designs.

### Future Research

Extensions can integrate multi-modal visual information reinforcement learning from real website feedback and specialized language models for web understanding and action taking. The dataset and framework support further development toward truly generalizable agents that work on any website.

### References
Deng, X., Gu, Y., Zheng, B., Chen, S., Stevens, S., Wang, B., Sun, H., & Su, Y. (2023, June 9). Mind2Web: towards a generalist agent for the web. arXiv.org. https://arxiv.org/abs/2306.06070
