from itertools import pairwise
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    words = [line.rstrip("\n") for line in f]


def is_word_nice(word: str) -> bool:
    all_pairs: set[str] = {a + b for a, b in pairwise(word)}
    is_pair_twice = False
    is_letter_repeat = False

    for pair in all_pairs:
        if word.count(pair) > 1:
            is_pair_twice = True
            break

    for i, c in enumerate(word[:-2]):
        if c == word[i + 2]:
            is_letter_repeat = True
            break

    return is_pair_twice and is_letter_repeat


total_nice_words = 0
for word in words:
    if is_word_nice(word):
        total_nice_words += 1

print(f"Result: {total_nice_words}")
