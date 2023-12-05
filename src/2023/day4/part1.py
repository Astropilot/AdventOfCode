import re
from pathlib import Path

contents = Path(Path(__file__).parent, "sample").read_text()

sum_cards_worth = 0
for line in contents.split("\n"):
    left, right = line.split("|")
    card_numbers = list(map(int, re.findall(r"\d+", left.split(":")[1])))
    my_numbers = list(map(int, re.findall(r"\d+", right)))

    card_worth = 0

    for n in my_numbers:
        if n in card_numbers:
            if card_worth == 0:
                card_worth = 1
            else:
                card_worth *= 2

    sum_cards_worth += card_worth

print(f"Result: {sum_cards_worth}")  # Result: 22193

# One liner (code golf for fun)
# fmt: off
print(
    sum(
        [
            (lambda ns: len(ns))([
                n
                for n in list(map(int, L.split(":")[1].split("|")[1].strip().replace('  ', ' ').split(' ')))
                if n in map(int, L.split(":")[1].split("|")[0].strip().replace('  ', ' ').split(' '))
            ])
            for L in open("sample")
        ]
    )
)
# fmt: on
