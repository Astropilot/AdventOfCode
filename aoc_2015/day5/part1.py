from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    words = [line.rstrip("\n") for line in f]


def is_word_nice(word: str) -> bool:
    vowels = 0
    twice_in_row = False

    for i, c in enumerate(word):
        if c in "aeiou":
            vowels += 1
        if i + 1 < len(word):
            if c == word[i + 1]:
                twice_in_row = True
            if c + word[i + 1] in ("ab", "cd", "pq", "xy"):
                return False
    return vowels >= 3 and twice_in_row


total_nice_words = 0
for word in words:
    if is_word_nice(word):
        total_nice_words += 1

print(f"Result: {total_nice_words}")
