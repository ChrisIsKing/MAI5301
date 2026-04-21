### WebArena: A Realistic Web Environment for Building Autonomous Agents

#### Problem Addressed

The issue that arose was that existing evaluation environments for autonomous web agents were either too simplified, too static, or too reliant on live websites to serve as meaningful benchmarks. Agents trained and tested in oversimplified environments appeared highly capable in research settings but struggled to transfer that capability to the real web. Part of the problem was task scope; many benchmarks limited both the variety and complexity of tasks available, which meant agents were never actually tested on the kind of multi-step, open-ended interactions that characterize real internet use. The other part of the problem was reproducibility. Benchmarks that used live websites introduced constant pages update, interfaces change, CAPTCHAs appear, making it impossible to reliably measure whether an agent had actually improved between experiments.

#### State of Related Works

At the time of this paper, most existing benchmarks fell into one of two categories. Static environments gave agents access only to pre-rendered page states with no real dynamic interaction, which meant agents were operating on snapshots rather than a live production environments. The other was live website environments, which solved the "realism" problem but introduced reproducibility issues as the same task run twice could yield different results depending on what had changed on the site since the last run.

#### Proposed Solution and Key Insights

The researchers built WebArena around four web platforms: an e-commerce site modeled after online shopping platforms, a social discussion forum modeled after Reddit, a collaborative software development platform modeled after GitLab, and a content management system. These sites were chosen because they reflect the most common categories of activity people actually perform on the internet. They were not live platforms however. WebArena replicated into a Dockerized image so that any researcher could spin up an identical environment and run experiments from the same initial state. This solves the reproducibility problem where every agent starts from the same world. The environment also included auxiliary tools like maps, a calculator, and a scratchpad, as well as knowledge resources like Wikipedia and domain specific documentation. The agent interacts with the environment through browser interface, observing the current URL, open tabs, and webpage content, and can act through clicks, typing, keyboard shortcuts, tab switching, and URL navigation.The agent can interact in three ways: the full HTML DOM tree, a pixel screenshot, and an accessibility tree.

The WebArena benchmark itself consists of 812 tasks written as high-level natural language instructions, the same way a human would phrase a request. The tasks require multiple steps to complete. Evaluation is outcome based, checking whether the agent actually achieved the intended goal rather than whether it followed a specific sequence of actions. WebArena also included a subset of unachievable tasks that cannot be completed given the available information. This was to test whether agents would hallucinate a false result or correctly identify that the task was impossible.

Human annotators completing 170 tasks across the benchmark achieved a success rate of 78.24%. The best performing model, GPT-4 with chain-of-thought prompting, achieved 14.41% when the unachievable hint was removed from the prompt. GPT-3.5 reached 8.75% and text-bison-001 reached 5.05%. GPT-4 with chain-of-thought and the unachievable hint enabled dropped to 11.7%, because the hint caused the model to prematurely label achievable tasks as impossible it flagged 54.9% of actually achievable tasks as unachievable. GPT-4 only achieved a 100% success rate on 4 out of 61 task templates.

#### Drawbacks and Limitations

The benchmark is limited to four website categories, which, while representative, doesn't cover the full range of platforms and interaction patterns present on the real internet.

#### Future Directions

The authors suggest that prompting strategy has a meaningful effect on performance, which leaves room for exploration in how agents are instructed and how they handle uncertainty about task feasibility.


### Mind2Web: Towards a Generalist Agent for the Web

#### Problem Addressed

The issue that arose was that existing web agents were either trained on simulated environments that didn't reflect real websites, tested on a narrow set of websites and tasks, or designed around pre-defined scripted rules that limited how well they could generalize. Most prior work also evaluated agents on single-step or very constrained tasks, which meant the benchmarks weren't capturing what it actually looks like to complete a real goal on the internet. The researchers proposed Mind2Web as a solution: a large-scale dataset collected from real websites across diverse domains, paired with a two-stage agent framework called MindAct, designed to train and evaluate generalist web agents that could handle the full complexity of real web interaction.

#### State of Related Works

At the time of this paper, most web agent benchmarks shared a common design flaw. They either relied on simulated environments that oversimplified real web interfaces, covered only a small number of websites, or evaluated agents on tasks that were scripted with a fixed path to completion. Agents built on these benchmarks also tended to depend on pre-defined rules, which made them brittle outside of the specific conditions they were trained on. The deeper problem was that none of these setups were testing true generalization. A web agent that performs well on a handful of familiar websites with structured tasks is a very different thing from an agent that can navigate an unseen website and complete an open-ended user goal. The field needed a benchmark built from the real web, with real diversity, to make any meaningful progress on that problem.

#### Proposed Solution and Key Insights

The researchers built the Mind2Web dataset by collecting tasks from 137 real websites spanning 31 domains, including travel, shopping, finance, education, entertainment, government services, and more. The dataset contains over 2,300 annotated tasks, each consisting of three components: a high-level task description written as a natural language instruction, an action sequence capturing the steps required to complete it, and a webpage snapshot representing the environment at each step. Tasks were designed to be open-ended rather than scripted, meaning there was no single correct path, only a correct outcome. Annotators proposed tasks inspired by seed prompts from language models, then completed those tasks on real websites using a custom Playwright-based recording tool that captured every interaction, including the target element, the action taken, and the resulting page state.

To actually build an agent that could operate on this data, the researchers proposed MindAct, a two-stage framework designed around one core insight: raw HTML pages are far too large for a language model to process efficiently, often containing thousands of elements, most of which are completely irrelevant to the task at hand. The first stage addresses this by using a small language model, specifically DeBERTa with 86 million parameters, to rank all elements on the page by relevance to the current task and filter down to the top 50 candidate elements. This dramatically reduces what gets passed into the second stage. The second stage then uses a larger language model, Flan-T5, to perform action prediction. The candidate elements are presented to the model as a multiple choice question: given the task description, the previous actions, and the reduced list of candidate elements, which element should the agent interact with, and what should it do? This formulation turns a search problem over thousands of HTML elements into a structured classification problem, which the language model can handle much more reliably.


DeBERTa performed strongly across all three evaluation settings, achieving 88.9% accuracy on cross-task, 85.3% on cross-website, and 85.7% on cross-domain. This showed that the filtering stage was reliable enough to consistently preserve the correct element for the second stage. On overall task completion, MindAct achieved a step success rate of 52% on cross-task, 39% on cross-website, and 13% on cross-domain. Performance degredation occurred because od website layout diversity. Even when two websites operate in the same domain, differences in their interface structure were enough to significantly hurt performance.

#### Drawbacks and Limitations

MindAct only uses textual HTML information and ignores visual layout cues like button placement, icons, and spatial structure, all of which a human naturally uses when navigating a webpage. Each page is also processed independently, meaning the agent has no awareness of how a page's layout relates to what it has seen before.

#### Future Directions

The authors identify several directions that could meaningfully advance the field. Integrating multimodal inputs, combining HTML structure with visual screenshots, would allow agents to leverage the same spatial and visual cues that humans rely on when browsing. 