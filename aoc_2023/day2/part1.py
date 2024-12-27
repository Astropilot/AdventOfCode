import re
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
possibles = {"r": 12, "g": 13, "b": 14}
sum_game_ids = 0

for line in contents.split("\n"):
    game_id_match = re.match(r"Game (\d+)", line)
    if game_id_match is None:
        print("Warn: Impossible go fetch the game id")
        continue
    game_id = int(game_id_match.group(1))
    colors_matchs = re.findall(r"((\d+) ([rgb]))", line)

    impossible = False
    for color in colors_matchs:
        if possibles[color[2]] < int(color[1]):
            impossible = True
            break

    if not impossible:
        sum_game_ids += game_id

print(f"Result: {sum_game_ids}")  # Result: 2447
