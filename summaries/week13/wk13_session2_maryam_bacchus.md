### OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

#### Problem Addressed

The issue that arose was that existing benchmarks for autonomous agents were either limited to specific applications, lacked interactive environments, or were too narrow in scope and did not truly reflect what real computer use actually looks like. Agents that were trained on thoese benchmarks couldn't handle the diversity of tasks that a person would, when working on a real computer, which consists of multiple applications, multiple interfaces, and multiple operating systems. The researchers proposed OSWorld as a solution, a scalable and real computer environment capable of evaluating multimodal agents on actual tasks people perform on computers.

#### State of Related Works

At the time of this paper, existing benchmarks generally fell into one of a few limited categories. Some provided only static demonstration datasets with no interactive execution environment, which meant they could only evaluate whether an agent predicted the right next action, not whether it actually completed a task. Others built executable environments but restricted them to a single application or domain, like web browsing or coding, which meant agents developed in those environments had no way to handle tasks that required switching between applications or using the operating system directly. No existing benchmark at the time could support openended tasks performed on a computer, the way a real human workday demands, where completing one goal might require Chrome, a spreadsheet, a terminal, and an email client working in synchronization.

#### Proposed Solution and Key Insights

The researchers built OSWorld on top of virtual machines running Ubuntu OS (because of its opensource nature). Virtual machines were proposed over docker containers because the VM can run their own kernel, which supports OS interactions, including GUI and CLI options. The environment supports initial state configuration, execution-based evaluation, and interactive agent learning, all within a controllable and resettable setup. OSWorld gives agents access to a full desktop screenshot and an accessibility tree, and agents interact through mouse and keyboard actions using pyautogui. OSWorld uses the full action space, including right clicks, hotkeys, drag and drop, and scrolling.

The benchmark developed consisted of 369 computer tasks drawn from realworld usage, covering eight core applications in Chrome, VLC, Thunderbird, VSCode, LibreOffice Calc, LibreOffice Writer, LibreOffice Impress, and GIMP. It also contained basic OS operations and multi-app workflow tasks. Task examples were sourced from tutorials, forums, blogs sites, and community Q&A, and were selected based on popularity and difficulty. Each task is paired with an initial state configuration that simulates an "in progress" work environment, rather than starting from a blank slate. Each task also comes with a custom evaluation script that checks whether the task was genuinely completed by querying the environment's final state directly. 

Human annotators, computer science students who had not seen the tasks before, achieved a 72.36% success rate with a median completion time of 111.94 seconds per task. Among the models tested, GPT-4 using an accessibility tree as input achieved the best overall success rate at 12.24%. All other models fell below 7%. A consistent finding across models was that agent performance varied wildly depending on the task type, while human performance remained stable at around 70% across all categories. The most common failure mode was mouse click inaccuracy. In more than 75% of failed attempts from GPT-4, the agent planned the correct steps but clicked the wrong coordinates during execution, which then triggered other follow up errors. Models also struggled with pop-ups and unexpected application windows that appeared mid task, and they frequently demonstrated limited knowledge of domain specific software features, especialy in GIMP and Libre Office.

#### Drawbacks and Limitations

OSWorld is computationally more expensive than a simplier, albeit more technical solution - where you integrate directly with tools via an api call. Even though the setup might be more difficult, the overall benefit in integrating directly with tools ensures that tools are being used effectively and can use the wide range of operations a software offers, which some agents struggle in learning from simply interacting via a CLI and GUI.

#### Future Directions

Improving grounding capabilities, specifically the ability to accurately predict pixel coordinates for mouse actions, would significantly improve the effectiveness of this solution, given how dominant click inaccuracy was as a failure mode.


### AppAgent: Multimodal Agents as Smartphone Users

#### Problem Addressed

The issue that arose was that existing intelligent phone assistants like Siri operated through system back-end access and function calls, which meant they only worked within the specific apps and integrations that had been explicitly set up for them. This design created a hard ceiling on what these assistants could do and made them completely dependent on developers building in the right hooks. At the same time, prior LLM-based agents were limited to text only inputs, which made them poorly suited for interacting with smartphone apps where the interface is visual and the relevant information is in icons, buttons, and layout rather than text. The researchers proposed AppAgent as a solution, where a multimodal agent framework interacts with smartphone applications at the GUI level, the same way a human does, without requiring any system back-end access. It is also cross-app.

#### State of Related Works

At the time of this paper, LLM-based agents operated mostly text inputs, which meant that tasks requiring visual understanding of a UI, where the meaning of an element depends on how it looks rather than what it is labeled, were impossible to automate using agents. Early experiments with GPT-4V showed promise for understanding smartphone interfaces, but these worked best on familiar, widely used apps where the UI patterns were common enough to be represented in training data. For newer or less typical applications with unusual layouts, GPT-4V struggled to figure out what elements did or how to interact with them. There was no systematic way for an agent to learn the specific operational logic of an unfamiliar app without either massive training data collected in advance or a human programmer setting up explicit integrations.

#### Proposed Solution and Key Insights

The researchers built AppAgent around a two-phase framework: an exploration phase and a deployment phase. The core idea is that before an agent tries to complete tasks in an app, it first learns how that app works by exploring it and building a reference document. This separates the learning of app-specific knowledge from the execution of actual tasks, which means the agent does not have to figure out what each UI element does at the same time it is trying to complete a goal.

During exploration, the agent can learn in one of two ways. In autonomous exploration, the agent interacts with UI elements, observes what happens before and after each action, and records the results in a knowledge document. The exploration is goal-oriented rather than random, meaning the agent focuses on elements relevant to the app's main functions and uses the Android Back() function to exit irrelevant pages like advertisements. In the alternative approach, the agent observes a human completing tasks in the app and records only the elements and actions the human used. This approach is more efficient because it narrows the exploration space directly to what matters and avoids having the agent get lost in irrelevant parts of the interface.

During deployment, when the agent is given a real task, it accesses its reference document to understand what each UI element does on the current screen, then decides the next action based on that knowledge combined with its current observation. Each step follows a structured observe-think-act-summarize loop, and a summary of the interaction history is carried forward into each subsequent prompt, giving the agent a form of working memory across steps.

The action space was deliberately kept simple. Rather than requiring the agent to predict exact screen coordinates, which language models consistently struggle with, actions are defined as operations on numbered UI elements overlaid on the screenshot. Tap, long press, swipe, and text input are all parameterized by element number rather than pixel location, which makes the agent's job fundamentally easier and more reliable.

The evaluation covered 50 tasks across 10 apps including Google Maps, Twitter, Telegram, YouTube, Spotify, Yelp, Gmail, TEMU, Clock, and Lightroom. The baseline GPT-4 without any reference document and using the raw action API achieved a success rate of only 2.2%. When given the simplified action space but still no document, performance jumped to 48.9%, which shows how much the action space design alone contributes to agent capability. Adding documents generated through autonomous exploration brought the success rate to 73.3%, and documents generated by watching human demonstrations reached 84.4%. The oracle baseline using manually crafted documents achieved 95.6%, which sets the ceiling for what the framework can achieve with perfect knowledge of the app. The gap between the exploration-generated documents and the manually crafted ones is relatively small, which suggests that the exploration phase is producing genuinely useful and accurate app knowledge.

For the Lightroom image editing case study, which was evaluated through a user ranking study rather than a binary success metric, agents with documents consistently outperformed the GPT-4 baseline and also used a broader range of tools when editing, which produced higher-quality results.

#### Drawbacks and Limitations

There is not sufficient research into the potential risks in offering models unrestricted access to a personal device may have. Weaker models, those can run comfortably on smartphones are usually susceptible to prompt injections which can leak personal and sensitive information. A smartphone is commonly used as a socializing tool, for sending messages, interating on social media platforms and taking photos - the risks are higher if sensitive information gets leaked from these devices rather than for example, a work laptop that is used primarily for productivity tasks, where there is limitied personal information stored.

#### Future Directions

To get the most effective use of a solution such as this, future reseach can expand the action space to support multi-touch and more complex gesture types, which would make the framework applicable to a wider range of apps. 