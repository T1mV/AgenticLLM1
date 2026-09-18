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


# Additional examples for inspecting possible artifacts / failure cases

test_examples = {
    "number": [
        "2026",
        "1234567890",
        "3.1415926535",
        "1000000",
        "2026-09-17",
    ],
    "code": [
        "def calculate_score(x):",
        "return x * 2 + 1",
        "vocab_size = 32768",
        "text_bytes = text.encode('utf-8')",
    ],
    "Korean": [
        "한국어로 작성된 문장입니다.",
        "정직한 사실 위에, 공정한 시선을 더하다",
    ],
    "Dutch": [
        "Dit is een normale nederlandse zin.",
        "Ik ben nu aan het typen op mijn laptop."
    ],
    "English": [
        "This is a normal english scentence",
        "I'm now typing on my laptop"
    ],
    "Code": [
        "def train(self, text, vocab_size, verbose=False):",
        "vocab[idx] = vocab[pair[0]] + vocab[pair[1]]"
    ],
    "Math": [
        "\sum_{k=1}^{n} k^{3} \;=\; \left(\frac{n(n+1)}{2}\right)^{2}.",
        "S(n+1)=\left(\frac{(n+1)(n+2)}{2}\right)^2"
    ]
}

print("\n" + "=" * 60)
print("ADDITIONAL TOKENIZATION TESTS")
print("=" * 60)

for category, examples in test_examples.items():
    print(f"\n--- {category.upper()} ---")

    for text in examples:
        encoded = tokenizer.encode(text)
        tokens = [tokenizer.decode([token_id]) for token_id in encoded]

        encoded_bytes = text.encode("utf-8")
        ratio = len(encoded_bytes) / len(encoded)

        print(f"\nText: {text}")
        print(f"Tokens: {tokens}")
        print(f"Sequence Length: {len(encoded)}")
        print(f"Compression ratio: {ratio:.2f} bytes/token")


