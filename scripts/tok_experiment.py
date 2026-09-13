from nanochat.tokenizer import get_tokenizer

# script to look better at the performance of our tokenizer including
# compression ratio (tokens per character)
# sequence length for a fixed text sample
# printing of the results on a english string

english_string = "For this assignment, we needed to train a tokenizer"

tokenizer = get_tokenizer()
vocab_size = tokenizer.get_vocab_size()
print(f"vocab_size:  {vocab_size}")
# encoding the str using the tokenizer
encoded = tokenizer.encode(english_string)

# compression ratio: how compact is the text represented / formula = bytes / tokens
# can ued what is done in tok_eval.py
encoded_bytes = english_string.encode('utf-8')
ratio = len(encoded_bytes) / len(encoded)
print(f"compression ratio: {ratio}")

# sequence length: amount of tokens
seq_length = len(encoded)
print (f"Sequence Length: {seq_length}")

# visualizing what the tokens became
tokens = []
for token_id in encoded:
    token = tokenizer.decode([token_id])
    tokens.append(token)

print(f"tokens that are created \n {tokens}")