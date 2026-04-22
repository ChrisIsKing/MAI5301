import torch
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, emb_dim, num_heads, context_length, dropout=0.0, qkv_bias=False):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = emb_dim // num_heads

        self.W_query = nn.Linear(emb_dim, emb_dim, bias=qkv_bias)
        self.W_key   = nn.Linear(emb_dim, emb_dim, bias=qkv_bias)
        self.W_value = nn.Linear(emb_dim, emb_dim, bias=qkv_bias)
        self.out_proj = nn.Linear(emb_dim, emb_dim)
        self.dropout = nn.Dropout(dropout)

        mask = torch.triu(torch.ones(context_length, context_length), diagonal=1)
        self.register_buffer("mask", mask)

    def forward(self, x):
        batch, seq_len, emb_dim = x.shape

        # Q, K, V
        q = self.W_query(x)  # (batch, seq_len, emb_dim)
        k = self.W_key(x)
        v = self.W_value(x)

        q = q.view(batch, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        k = k.view(batch, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        v = v.view(batch, seq_len, self.num_heads, self.head_dim).transpose(1, 2)

        # calculate attention
        scores = q @ k.transpose(-2, -1) / (self.head_dim ** 0.5)

        scores = scores.masked_fill(self.mask[:seq_len, :seq_len].bool(), float("-inf"))

        # softmax + dropout
        weights = torch.softmax(scores, dim=-1)
        weights = self.dropout(weights)

        # weighted sum of values
        context = weights @ v  # (batch, num_heads, seq_len, head_dim)

        # concatenate heads: -> (batch, seq_len, emb_dim)
        context = context.transpose(1, 2).contiguous().view(batch, seq_len, emb_dim)

        return self.out_proj(context)
