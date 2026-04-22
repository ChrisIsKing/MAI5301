import os
import json
import numpy as np
import torch
import urllib.request
from tqdm import tqdm


def download_gpt2(model_size="124M", models_dir="gpt2"):
    """Download GPT-2 checkpoint files from OpenAI."""
    model_dir = os.path.join(models_dir, model_size)
    base_url = "https://openaipublic.blob.core.windows.net/gpt-2/models"
    files = [
        "checkpoint", "encoder.json", "hparams.json",
        "model.ckpt.data-00000-of-00001", "model.ckpt.index",
        "model.ckpt.meta", "vocab.bpe"
    ]

    os.makedirs(model_dir, exist_ok=True)
    for f in files:
        url = f"{base_url}/{model_size}/{f}"
        dest = os.path.join(model_dir, f)
        if not os.path.exists(dest):
            print(f"Downloading {f}...")
            urllib.request.urlretrieve(url, dest)

    # Load settings
    with open(os.path.join(model_dir, "hparams.json")) as f:
        settings = json.load(f)

    # Load weights from tensorflow checkpoint
    import tensorflow as tf
    ckpt = tf.train.latest_checkpoint(model_dir)
    params = {"blocks": [{} for _ in range(settings["n_layer"])]}

    for name, _ in tf.train.list_variables(ckpt):
        arr = np.squeeze(tf.train.load_variable(ckpt, name))
        parts = name.split("/")[1:]  # skip "model/"

        target = params
        if parts[0].startswith("h"):
            target = params["blocks"][int(parts[0][1:])]

        for key in parts[1:-1]:
            target = target.setdefault(key, {})
        target[parts[-1]] = arr

    return settings, params


def load_weights(model, params):
    """Load GPT-2 weights into our GPTModel."""

    def assign(param, value):
        if param.shape != value.shape:
            raise ValueError(f"Shape mismatch: {param.shape} vs {value.shape}")
        return torch.nn.Parameter(torch.tensor(value))

    # Embeddings
    model.tok_emb.weight = assign(model.tok_emb.weight, params["wte"])
    model.pos_emb.weight = assign(model.pos_emb.weight, params["wpe"])

    # Each transformer block
    for b in range(len(params["blocks"])):
        block = params["blocks"][b]

        # Attention: GPT-2 stores Q,K,V as one matrix — split it
        qkv_w = block["attn"]["c_attn"]["w"]
        qkv_b = block["attn"]["c_attn"]["b"]
        q_w, k_w, v_w = np.split(qkv_w, 3, axis=-1)
        q_b, k_b, v_b = np.split(qkv_b, 3, axis=-1)

        model.blocks[b].att.W_query.weight = assign(model.blocks[b].att.W_query.weight, q_w.T)
        model.blocks[b].att.W_key.weight   = assign(model.blocks[b].att.W_key.weight, k_w.T)
        model.blocks[b].att.W_value.weight = assign(model.blocks[b].att.W_value.weight, v_w.T)
        model.blocks[b].att.W_query.bias   = assign(model.blocks[b].att.W_query.bias, q_b)
        model.blocks[b].att.W_key.bias     = assign(model.blocks[b].att.W_key.bias, k_b)
        model.blocks[b].att.W_value.bias   = assign(model.blocks[b].att.W_value.bias, v_b)

        model.blocks[b].att.out_proj.weight = assign(model.blocks[b].att.out_proj.weight, block["attn"]["c_proj"]["w"].T)
        model.blocks[b].att.out_proj.bias   = assign(model.blocks[b].att.out_proj.bias, block["attn"]["c_proj"]["b"])

        # Feed-forward
        model.blocks[b].ff.layers[0].weight = assign(model.blocks[b].ff.layers[0].weight, block["mlp"]["c_fc"]["w"].T)
        model.blocks[b].ff.layers[0].bias   = assign(model.blocks[b].ff.layers[0].bias, block["mlp"]["c_fc"]["b"])
        model.blocks[b].ff.layers[2].weight = assign(model.blocks[b].ff.layers[2].weight, block["mlp"]["c_proj"]["w"].T)
        model.blocks[b].ff.layers[2].bias   = assign(model.blocks[b].ff.layers[2].bias, block["mlp"]["c_proj"]["b"])

        # Layer norms
        model.blocks[b].norm1.scale = assign(model.blocks[b].norm1.scale, block["ln_1"]["g"])
        model.blocks[b].norm1.shift = assign(model.blocks[b].norm1.shift, block["ln_1"]["b"])
        model.blocks[b].norm2.scale = assign(model.blocks[b].norm2.scale, block["ln_2"]["g"])
        model.blocks[b].norm2.shift = assign(model.blocks[b].norm2.shift, block["ln_2"]["b"])

    # Final norm
    model.final_norm.scale = assign(model.final_norm.scale, params["g"])
    model.final_norm.shift = assign(model.final_norm.shift, params["b"])

    # Output head (weight-tied with token embedding)
    model.out_head.weight = assign(model.out_head.weight, params["wte"])
