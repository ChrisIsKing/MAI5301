### 1. How Instruction Formatting Affects Training

Before finetuning using the Alpace style formattting, there was no format. The model just repeated the phrase "Write a response that appropriately completes the request" in a loop when given an instruction. After finetuning using the prompt format template (### Instruction:), (### Input:) and (### Response:), the model learned that (### Response:) is where it should provide a direct answer. This is shown in the model comparison section in assignment5_instruction.ipynb


### 2. Why Masking Is Crucial for Instruction Tuning

The model only needs to generate responses, not prompts. Without masking, the loss penalizes the model for every wrong prediction, including the prompt tokens. Masking tells the loss function to ignore these positions, don't count them. In the code, padding tokens was set to -100 (ignore_index=-100) so the loss is computed only on response tokens.


### 3. Quality of the Model's Instruction-Following

The fine-tuned model produces direct, responses in the correct format, although the answer itself may not be accurate. This is different from the base Gpt-2 model which, without finetuning, repeats the prompt given to it.

### 4. Differences from Classification Fine-tuning

Classification fine-tuning differs because it changes the model's output layer to predict a category (e.g. spam or not spam). Instruction fine-tuning keeps the original output layer and trains the model to generate text responses word by word. 
