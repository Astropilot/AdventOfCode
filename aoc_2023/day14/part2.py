from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

platform: list[list[str]] = []

for y in range(len(lines)):
    platform.append([])
    for x in range(len(lines[y])):
        platform[y].append(lines[y][x])


def count_north_load(platform: list[list[str]]) -> int:
    sum_loads = 0
    for col in range(len(platform[0])):
        for i in range(len(platform)):
            if platform[i][col] == "O":
                sum_loads += len(platform) - i
    return sum_loads


def tilt_north(platform: list[list[str]]) -> None:
    for col in range(len(platform[0])):
        next_available_i = 0
        for i in range(len(platform)):
            if platform[i][col] == "O":
                platform[i][col], platform[next_available_i][col] = (
                    platform[next_available_i][col],
                    platform[i][col],
                )
                next_available_i += 1
            elif platform[i][col] == "#":
                next_available_i = i + 1


def tilt_south(platform: list[list[str]]) -> None:
    for col in range(len(platform[0])):
        next_available_i = len(platform) - 1
        for i in range(len(platform) - 1, -1, -1):
            if platform[i][col] == "O":
                platform[i][col], platform[next_available_i][col] = (
                    platform[next_available_i][col],
                    platform[i][col],
                )
                next_available_i -= 1
            elif platform[i][col] == "#":
                next_available_i = i - 1


def tilt_west(platform: list[list[str]]) -> None:
    for row in range(len(platform)):
        next_available_i = 0
        for i in range(len(platform[row])):
            if platform[row][i] == "O":
                platform[row][i], platform[row][next_available_i] = (
                    platform[row][next_available_i],
                    platform[row][i],
                )
                next_available_i += 1
            elif platform[row][i] == "#":
                next_available_i = i + 1


def tilt_east(platform: list[list[str]]) -> None:
    for row in range(len(platform)):
        next_available_i = len(platform[row]) - 1
        for i in range(len(platform[row]) - 1, -1, -1):
            if platform[row][i] == "O":
                platform[row][i], platform[row][next_available_i] = (
                    platform[row][next_available_i],
                    platform[row][i],
                )
                next_available_i -= 1
            elif platform[row][i] == "#":
                next_available_i = i - 1


def guess_seq(seq: list[int]) -> tuple[int, int] | None:
    for i in range(len(seq)):
        # n = seq[i]
        try:
            i2 = seq.index(seq[i], i + 1)
        except ValueError:
            i2 = -1
        if i2 >= 0 and i2 - i > 1:
            is_seq = True
            for j in range(i + 1, i2):
                if i2 + (j - i) >= len(seq) or seq[j] != seq[i2 + (j - i)]:
                    is_seq = False
                    break
            if is_seq:
                return i, i2 - i
    return None


seq: list[int] = []
loop: tuple[int, int] | None = None
for _ in range(1000000000):
    tilt_north(platform)
    tilt_west(platform)
    tilt_south(platform)
    tilt_east(platform)

    t = count_north_load(platform)

    seq.append(t)

    loop = guess_seq(seq)

    if loop is not None:
        break

if loop is not None:
    # TODO: Optimize this part because my god this is disgusting
    i = 1
    res = 0
    while res < 1000000000:
        res = loop[0] + 1 + (loop[1] * i)
        i += 1
    res -= 1000000000
    print(f"Result: {seq[loop[0] + loop[1] - res]}")
else:
    print("ERROR!")
