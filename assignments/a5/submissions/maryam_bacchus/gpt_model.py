# gpt_model.py
import torch
import torch.nn as nn
from embedding import Embedding
from layernorm import LayerNorm
from transformer_block import TransformerBlock

class GPTModel(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.tok_emb = Embedding(cfg["vocab_size"], cfg["emb_dim"])
        self.pos_emb = Embedding(cfg["context_length"], cfg["emb_dim"])
        self.drop_emb = nn.Dropout(cfg["drop_rate"])

        self.blocks = nn.Sequential(
            *[TransformerBlock(cfg) for _ in range(cfg["n_layers"])]
        )

        self.final_norm = LayerNorm(cfg["emb_dim"])
        self.out_head = nn.Linear(cfg["emb_dim"], cfg["vocab_size"], bias=False)

    def forward(self, token_ids):
        batch, seq_len = token_ids.shape
        tok = self.tok_emb(token_ids)
        pos = self.pos_emb(torch.arange(seq_len, device=token_ids.device))
        x = self.drop_emb(tok + pos)
        x = self.blocks(x)
        x = self.final_norm(x)
        logits = self.out_head(x)   # (batch, seq_len, vocab_size)
        return logits
