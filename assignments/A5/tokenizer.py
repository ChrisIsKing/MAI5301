import tiktoken


class Tokenizer:
    def __init__(self):
        self.encoding = tiktoken.get_encoding("gpt2")

    def encode(self, text):
        return self.encoding.encode(text, allowed_special={"<|endoftext|>"})

    def decode(self, ids):
        return self.encoding.decode(ids)

    @property
    def vocab_size(self):
        return self.encoding.n_vocab

    @property
    def eos_id(self):
        return 50256