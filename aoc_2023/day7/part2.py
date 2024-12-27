from enum import Enum
from pathlib import Path


class HandType(Enum):
    FIVEKIND = 7
    FOURKIND = 6
    FULLHOUSE = 5
    THREEKIND = 4
    TWOPAIR = 3
    ONEPAIR = 2
    HIGHCARD = 1


strengths = "J23456789TQKA"


def get_hand_type(hand: str) -> HandType:
    cards: dict[str, int] = {}

    for c in hand:
        if c in cards:
            cards[c] += 1
        else:
            cards[c] = 1

    # Five kind
    if len(cards) == 1:
        return HandType.FIVEKIND
    # Four kind
    if len(cards) == 2 and any(c == 4 for c in cards.values()):
        return HandType.FOURKIND
    # Full house
    if len(cards) == 2:
        return HandType.FULLHOUSE
    # Three kind
    if len(cards) == 3 and any(c == 3 for c in cards.values()):
        return HandType.THREEKIND
    # Two pair
    if len(cards) == 3:
        return HandType.TWOPAIR
    # One pair
    if len(cards) == 4:
        return HandType.ONEPAIR
    # High card
    return HandType.HIGHCARD


def get_hand_type_with_jokers(hand: str) -> HandType:
    possibles_kind: list[HandType] = []

    for s in strengths[1:]:
        h = hand.replace("J", s)
        possibles_kind.append(get_hand_type(h))

    return sorted(possibles_kind, key=lambda k: k.value, reverse=True)[0]


contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

#                 hand bid  type
hands: list[tuple[str, int, HandType]] = []

for line in lines:
    hand, bid = line.split(" ")
    hands.append(
        (
            hand,
            int(bid),
            get_hand_type(hand) if "J" not in hand else get_hand_type_with_jokers(hand),
        )
    )

hands.sort(
    key=lambda h: (
        h[2].value,
        strengths.index(h[0][0]),
        strengths.index(h[0][1]),
        strengths.index(h[0][2]),
        strengths.index(h[0][3]),
        strengths.index(h[0][4]),
    )
)

sum_winnings = 0

for rank, h in enumerate(hands, 1):
    sum_winnings += h[1] * rank

print(f"Result: {sum_winnings}")
