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

# Sequence length: amount of tokens
seq_length = len(encoded)
print (f"Sequence Length: {seq_length}")

# Compression ratio: tokens per character
compression_ratio =  seq_length/ len(english_string)
print (f"Compression Ratio: {compression_ratio}")

# visualizing what the tokens became
tokens = []
for token_id in encoded:
    token = tokenizer.decode([token_id])
    tokens.append(token)

print(f"tokens that are created: \n {tokens}")