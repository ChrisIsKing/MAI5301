### Problem Addressed and Problem Importance
Pseudonymous online accounts have long enjoyed practical obscurity because deanonymization required either structured data or hours of manual investigation. When attackers can now use large language models on raw unstructured text from forums and conversations alone, this protection collapses at scale. The ability to automatically link anonymous profiles to real identities or to each other threatens the privacy assumptions that underpin Reddit throwaways, Hacker News accounts, anonymous forums, and similar spaces.

### State of Related Works in This Topic
Classical attacks such as the Netflix Prize matching relied on structured ratings or spatiotemporal points and could not handle raw text across arbitrary platforms. Earlier LLM work showed that models can infer personal attributes from forum posts, yet no prior system performed full end-to-end deanonymization at scale. Existing benchmarks evaluated only small closed-world settings or required manual verification, leaving the open-web and large-candidate-pool threat models unexplored.

### Proposed Solution
The authors present two complementary approaches. First, frontier LLM agents equipped with web search autonomously summarize a pseudonymous profile, generate an anonymized search prompt, query the internet, and reason over evidence to identify the real person. Second, they introduce the scalable ESRC pipeline: Extract identity-relevant features from unstructured text with an LLM, embed those features for fast nearest-neighbor search across thousands or millions of candidates, Reason over the top matches with extended LLM deliberation to select and verify the best candidate, and Calibrate confidence scores to trace precision-recall curves at high precision thresholds. The pipeline is evaluated on three ground-truth datasets: Hacker News to LinkedIn, Reddit movie communities split by subreddit, and Reddit histories split temporally.

### Drawbacks and Limitations
The evaluation datasets necessarily contain users who once linked accounts or posted enough to create verifiable ground truth, introducing selection bias toward less privacy-conscious individuals. Truly private users may leave weaker signals. The agentic approach produces single-point estimates rather than full tunable precision-recal curves, and its dependence on opaque search engines makes isolating the LLM contribution difficult. Cost per profile remains non-trivial for truly massive scale.

### Future Research
The authors call for larger and more diverse evaluation sets, including genuinely pseudonymous accounts where ground truth can be obtained ethically. They suggest exploring mitigation strategies such as platform policies that discourage cross-linking or technical defenses that obscure micro-data signals. Extending the pipeline to handle dynamic real-time content and multi-platform temporal drifts would further test its robustness.

### References
Lermen, S., Paleka, D., Swanson, J., Aerni, M., Carlini, N., & Tramèr, F. (2026, February 18). Large-scale online deanonymization with LLMs. arXiv.org. https://arxiv.org/abs/2602.16800
