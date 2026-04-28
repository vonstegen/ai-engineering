"""
Day 01 - Tokenization: Exercise 1
Exploring how OpenAI's cl100k_base tokenizer (used by GPT-4) handles different inputs.
"""
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

samples = [
    "Hello world",
    "Hello, world!",
    "antidisestablishmentarianism",
    "🤖 agents are cool",
    "def hello(): return 'world'",
    "1234567890",
    "こんにちは",
    " world",       # note the leading space
    "world",        # same word, no leading space
]

print(f"{'INPUT':<40} | {'TOKENS':>6} | PIECES")
print("-" * 100)
for s in samples:
    ids = enc.encode(s)
    pieces = [enc.decode([i]) for i in ids]
    print(f"{repr(s):<40} | {len(ids):>6} | {pieces}")