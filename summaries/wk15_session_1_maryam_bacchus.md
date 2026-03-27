### Paper: GPTs are GPTs: An Early Look at the Labor Market Impact Potential. 
#### Problem Addressed
The paper addressed that existing frameworks for measuring the labor market impact of automation were built around earlier forms of technology, such as robotics and some task specific automation software. These systems primarily affected routine, and process-based work. These frameworks were not designed to account for large language models, which operate across cognitive and language-based tasks and are not confined to any single industry or application domain. Because LLMs can process text, code and perform analysis, across any field, it was argued that their potential to affect employment is broader and different from previous automation techniques.

#### State of Related Works
At the time, when measuring AI's labor market impact, researchers used databases like O*NET, which catalogs the tasks, activities, and skill requirements associated with hundreds of occupations across the US workforce. Prior studies applied expert judgment and machine learning to these task descriptions to estimate which jobs were at risk from automation. A consistent finding from earlier literature was that routine tasks were easiest to automate, that technology would reshape tasks within jobs rather than eliminating the entire job, and that these shifts affected wage structures and hiring demand. However, when the researchers tested their new LLM-specific exposure scores against prior AI and automation metrics, they found negative correlations with robotics and manual task measures. These results confirmed that LLMs introduce an entirely new set of impact, and that it does not map cleanly onto earlier frameworks. It also shows that existing tools could not detect where language models would actually have their greatest effect.

#### Proposed Solution and Key Insights
The researchers created a task-level rubric that asked a single question for each task in the O*NET database: can an LLM, or an LLM combined with supporting software tools, reduce the time required to complete this task by fifty percent or more? If the answer was no, the task was classified as unexposed. If the answer was yes, it was classified under a direct exposure label. If the threshold was only reachable with the addition of specialized tools built on top of the LLM, it received a combined exposure label. 

Across the full O*NET dataset, roughly fifteen percent of tasks were found to be directly exposed to LLMs alone, and approximately eighty percent of workers in the US workforce were found to have at least some degree of task-level exposure. Around nineteen percent of occupations had fifty percent or more of their tasks classified as exposed. When LLM-powered tools were included in the analysis, the proportion of tasks reaching the exposure threshold rose from the direct LLM figure to approximately thirty percent, and with fully specialized systems the coverage extended further still.

The research also showed thata the highest exposure rates, with roles such as interpreters and translators, mathematicians, court reporters, software developers, and creative writers are among the most affected. Jobs requiring physical presence, manual dexterity, or extensive domain-specific training developed over years showed much lower exposure. Writing and programming tasks emerged as particularly vulnerable to direct LLM impact, while tasks requiring scientific reasoning and critical judgment were less affected. This pattern was different from previous automation trends.

Finally, the researchers make a direct comparison between electricity and LLMs, just as electricity required the development of power lines, appliances, and new industrial processes before it realized its full economic potential, LLMs must follow the same pattern. Their value would only grow when complementary tools are built around them.

#### Drawback and Limitations
The dataset is drawn from O*NET, which reflects the US workforce and does not generalize to labor markets with different occupational structures, wage levels, or technology adoption patterns. 

#### Future Research
Future work could look at re-evaluation of the rubric as model capabilities evolve. 


### Paper: Levels of Autonomy for AI Agents
#### Problem Addressed
In this paper, the researchers posited that AI agent development had been treating autonomy as an byproduct of increasing model capability. It is rather a deliberate design decision. As AI agents become more capable of acting on behalf of users, such as browsing the web, resolving software issues, and managing tasks across applications, there needed to be a structured framework specifying how much autonomy an agents should actually exercise. Without this, developers had no way to calibrate the level of user involvement appropriate for a given use case, and governance bodies had no clear standard against which to evaluate agent behavior.

#### State of Related Works
Research on AI agents was focused on autonomous task completion, with benchmarks designed to measure how well an agent could complete a goal without any human involvement. This evaluation reinforced a view of autonomy as something to be maximized rather than calibrated. Related work on levels of AGI, treated autonomy as linked to performance and generality, making it difficult to separate from capability. Other researchers had begun raising concerns about the risks of increasing agent autonomy, including accountability gaps, scams enabled by voice agents, leaking of private information, and the gradual deskilling of human users, but no framework existed to describe and manage those risks through design.

#### Proposed Solution and Key Insights
The researchers proposed a five-level framework that defines agent autonomy based on the role a user takes when interacting with the agent, rather than on what the agent is capable of doing. The key argument is that autonomy is a design decision that can be made independently of capability. A highly capable agent can still be deployed at a low autonomy level if the developer requires it to seek user input before acting.  

The five proposed levels are: 
Level 1 - The user acts as an operator, directly controlling the agent's actions at each step, similar to a pilot manually flying a plane.  
Level 2 - the user acts as a collaborator, working alongside the agent on a shared task where both contribute, comparable to how tools like OpenAI's Operator function.  
Level 3 - the user acts as a consultant, where the agent handles most of the work but checks in with the user at key decision points.  
Level 4 - the user acts as an approver, reviewing the agent's completed plan or output before it is executed, but not involved during execution.  
Level 5, the user acts as an observer, able only to monitor what the agent is doing and trigger an emergency stop, with no ability to direct the agent mid-task.

The paper also introduces the concept of autonomy certificates, which are like documents issued by a third-party governing body that cap the maximum autonomy level at which an agent is permitted to operate. These certificates are modeled from SSL certificates and are designed to communicate an agent's behavioural characteristics to other developers and agents.

#### Drawback and Limitations
I beleive that the autonomy certificates may not be feasible and may have some resistance to adoption. It also begs the question, what institutional structures, legal grounding, or incentives that would be required to make a third-party certification body functional? And who decides who should have authority over something like this?

#### Future Research. 
The authors mentioned that current benchmarks measure only autonomous task completion accuracy, so new evaluation methods are needed that can assess an agent's behavior across all five levels and capture how well it supports user involvement rather than minimizing it.

### Paper: Labor market impacts of AI: A new measure and early evidence. 
#### Problem Addressed. 
The problem addressed is that existing methods for measuring AI's labor market impact had a poor track record, and that relying on purely theoretical exposure measures risked producing forecasts that looked plausible but failed to reflect what was actually happening in the economy. Prior attempts to quantify job vulnerability, such as measures had identified roughly a quarter of US jobs as at risk, yet almost a decade later most of those jobs had maintained healthy employment growth. The researchers argued that the field needed a measure that moved beyond what AI could theoretically do and incorporated evidence of what it was actually doing in real work settings.

#### State of Related Works. 
At the time, the dominant approach to measuring Ai's effects on the labor market was to estimate theoretical exposure at the task level. Other researchers had built on this foundation in various ways. Gimbel et al. tracked shifts in the occupational mix using Current Population Survey data and found changes had so far been unremarkable. Brynjolfsson et al. examined employment levels split by age group using payroll data from ADP. Acemoglu et al. and Hampole et al. studied job posting data to look for early hiring signals. The common limitation across this body of work was that theoretical exposure measures had not been tested against real-world AI usage data and had produced no actual accurate predictions in labour market shifts so far. The researchers also noted that the government's own occupational growth forecasts had added little predictive value beyond simple linear extrapolation of past trends.

#### Proposed Solution and Key Insights. 
The researchers built a new occupation-level exposure measure by combining three data sources: the O*NET database; task-level theoretical exposure scores from Eloundou et al.; and actual usage data from Anthropic's Economic Index, which tracks how Claude is being used in professional settings across thousands of tasks. 
Tasks are counted as covered only if they are both theoretically feasible for an LLM and have also appeared with sufficient frequency in real Claude usage data. The measure further adjusts for how a task is being carried out, giving full weight to automated implementations and half weight to augmentative use, where the human remains in the loop. These task-level scores are then averaged to the occupation level, weighted by the fraction of working time each task occupies within that role.

The results showed a significant gap between theoretical capability and actual practice. Computer and mathematical occupations had theoretical task coverage of ninety-four percent under Eloundou et al.'s measure, but actual observed coverage of only thirty-three percent. Office and administrative support occupations showed a similar gap between ninety percent theoretical and much lower actual exposure. Computer programmers were the most exposed occupation under the new measure at seventy-five percent task coverage, followed by customer service representatives and data entry keyers. At the other end, roughly thirty percent of workers had zero observed exposure, including cooks, mechanics, lifeguards, and dishwashers.

The researchers showed overall that workers in the top quartile of observed exposure were sixteen percentage points more likely to be female, almost twice as likely to be Asian, earned forty-seven percent more on average, and had significantly higher education levels. Graduate degree holders made up less than five percent of the unexposed group but seventeen percent of the most exposed group.

#### Drawback and Limitations. 
The researcheres used Claude usage data alone, which means it reflects the behavior of just Claude's AI system's user base and may not generalize to how other models or tools are being used across the economy.

#### Future Research. 
Further work is needed to understand why actual usage lags so far behind theoretical possibility in many high exposure occupations, including whether the barriers are primarily legal, organizational, or technical in nature. It is possible that due to the reduction of hiring of younger workers aged twenty-two to twenty-five - the deomgraphic more likely to adopt to AI usage, may be the cause of this.
