import re
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()

cards: list[int] = []

for line in contents.split("\n"):
    left, right = line.split("|")
    card_numbers = list(map(int, re.findall(r"\d+", left.split(":")[1])))
    my_numbers = list(map(int, re.findall(r"\d+", right)))

    card_worth = 0

    for n in my_numbers:
        if n in card_numbers:
            card_worth += 1

    cards.append(card_worth)


def countWinningCards(cards: list[int], idx: int) -> int:
    if idx >= len(cards):
        return 0

    s = 1

    for i in range(1, cards[idx] + 1):
        s += countWinningCards(cards, idx + i)

    return s


result = 0

for i in range(len(cards)):
    result += countWinningCards(cards, i)

print(f"Result: {result}")  # Result: 5625994
