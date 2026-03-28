import json
import torch
from torch.utils.data import Dataset


def format_prompt(entry):
    text = (
        f"Below is an instruction that describes a task. "
        f"Write a response that appropriately completes the request."
        f"\n\n### Instruction:\n{entry['instruction']}"
    )
    if entry["input"]:
        text += f"\n\n### Input:\n{entry['input']}"
    text += "\n\n### Response:\n"
    return text


def format_full(entry):
    return format_prompt(entry) + entry["output"]


class InstructionDataset(Dataset):
    def __init__(self, data, tokenizer):
        self.samples = []
        for entry in data:
            prompt_ids = tokenizer.encode(format_prompt(entry))
            full_ids = tokenizer.encode(format_full(entry))
            full_ids.append(tokenizer.eos_id)
            self.samples.append({
                "token_ids": full_ids,
                "prompt_len": len(prompt_ids),
            })

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        return self.samples[idx]

def custom_collate_fn(batch, pad_token_id=50256, ignore_index=-100,
                      allowed_max_length=None, device="cpu"):
    batch_max_length = max(len(item)+1 for item in batch)
    inputs_lst, targets_lst = [], []

    for item in batch:
        new_item = item.copy()
        new_item += [pad_token_id]                         
        padded = new_item + [pad_token_id] * (batch_max_length - len(new_item))
        inputs = torch.tensor(padded[:-1])
        targets = torch.tensor(padded[1:])

        # Mask padding
        mask = targets == pad_token_id
        indices = torch.nonzero(mask).squeeze()
        if indices.numel() > 1:
            targets[indices[1:]] = ignore_index

        if allowed_max_length is not None:
            inputs = inputs[:allowed_max_length]
            targets = targets[:allowed_max_length]

        inputs_lst.append(inputs)
        targets_lst.append(targets)

    inputs_tensor = torch.stack(inputs_lst).to(device)
    targets_tensor = torch.stack(targets_lst).to(device)
    return inputs_tensor, targets_tensor


def load_data(path):
    """Load an Alpaca-format JSON file."""
    with open(path) as f:
        return json.load(f)


def split_data(data, train_frac=0.85, test_frac=0.10):
    """Split into train / test / val."""
    n_train = int(len(data) * train_frac)
    n_test = int(len(data) * test_frac)
    return data[:n_train], data[n_train:n_train + n_test], data[n_train + n_test:]