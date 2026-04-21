### Paper: Direct Preference Optimization: Your Language Model Is Secretly a Reward Model (DPO)

#### Problem Addressed
RLHF typically involves a complex multi stage training pipeline. The issue addressed is that this pipeline requires training a separate reward model, sampling multiple outputs from the language model during training, and then tuning hyperparameters for both models. The added complexity leads to training instabilities and high memory requirements due to maintaining multiple models. 

#### State of Related Works
At the time of this paper, the standard approach was PPO based RLHF. This involved three stages: supervised fine tuning on high quality data, training a separate reward model on human preference rankings, and then using PPO to optimize the policy based on reward signals. The problem with this method was that during training, the model has to generate multiple candidate responses for each prompt, send them to the reward model for ranking, and then incorporate the signals into the loss function. This process was computationally expensive and created instabilities.

#### Proposed Solution and Key Insights
The researchers proposed using a fixed dataset of preference pairs and a simple classification loss to directly optimize the language model. Instead of training a separate reward model, DPO treats the language model itself as an "implicit" reward model. The insight here is that you only need pairwise comparisons, a winning response and a losing response for each prompt. The loss function calculates the ratio of how much more likely the winning response is under the new model compared to a reference model, and similarly for the losing response. The algorithm wants the winning response to be at a high probability and the losing response to be at a lower probability. This approach eliminates the need for a separate reward model and simplifies the pipeline in a similar way to finetuning. The researchers found that DPO is much less sensitive to hyperparameter changes, while PPO shows steep declines in performance as you adjust temperature, while DPO remains stable. 

#### Drawbacks and Limitations
The authors showed that DPO achieves better results than PPO with lower computational costs and greater stability. However, the approach requires a pre-existing dataset of preference pairs, which may limit flexibility compared to PPO.

#### Future Directions
The researchers suggested future studies can look at scaling this method to larger models. While the researchers looked at 6B models, state of the art models are hundreds of billions of parameters large.


### Paper: KTO: Model Alignment as Prospect Theoretic Optimization

#### Problem Addressed
Both PPO and DPO rely on preference data where humans compare multiple responses. The issue addressed is that collecting pairwise comparison data is expensive, slow, and introduces biases. When you ask humans to pick between two responses, both might actually be good, and forcing a comparison can penalize a perfectly acceptable answer. Additionally, if one response is terrible and the other is mediocre, this noisy pairing can skew the reward signal. The researchers proposed that you don't actually need preference data at all and that you can align models using simple binary signals (good or bad / thumbs up or thumbs down) for individual outputs, without any comparison.

#### State of Related Works
At the time of this paper, PPO based RLHF required training a separate reward model and sampling multiple outputs during training. DPO simplified this by using fixed pairwise preference data, eliminating the need for a separate reward model and online sampling. However, DPO still required pairs where for each prompt, you needed a winning response and a losing response. Both approaches relied on humans ranking or comparing outputs, which is more expensive and more cognitively demanding than just asking "do you think this response was good or bad?"

#### Proposed Solution and Key Insights
The ressearchers work was inspired by prospect theory, a behavioural economics model. The key insight is loss aversion, where humans are more scared to lose than they are excited to win. People don't judge value in absolute terms instead, they judge it relative to a reference point. KTO applies this to model alignment. Instead of comparing two outputs, you only need one output with a binary label "good or bad". The reference point becomes the average divergence across the training batch. The model essentially learns if something is better or worse than what it usually generates. 

This approach made collection simpler, this works with most LLMs currently that have a thumbs up or thumbs down button at the end of each response. Companies serving millions of users can collect this data easily.

#### Drawbacks and Limitations
The paper argues that maximizing human utility doesn't require pairwise comparisons, it just requires knowing if an output is good or bad relative to what the model usually generates. However, using the batch average as a reference point means the quality of that reference depends on the composition of your training batch. The approach also assumes that binary feedback captures enough signal for alignment, which may not hold for nuanced tasks where the difference between "good" and "great" matters.

#### Future Directions
The researchers suggested exploring how KTO could leverage synthetic data to further reduce dependence on human feedback.