from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    passphrases = [line.rstrip("\n") for line in f]

valid_passphrases = 0

for passphrase in passphrases:
    words = passphrase.split(" ")
    visited: set[str] = set()
    is_valid = True

    for word in words:
        if word in visited:
            is_valid = False
            break
        visited.add(word)

    if is_valid:
        valid_passphrases += 1

print(f"Result: {valid_passphrases}")
