import typing as t
from pathlib import Path


class CoordsT(t.NamedTuple):
    x: int
    y: int


key = Path(Path(__file__).parent, "input").read_text()


# From day 10 part 2
def knot_hash(input: str, size: int = 256) -> str:
    lenghts = [ord(c) for c in input] + [17, 31, 73, 47, 23]
    size = 256
    current_pos = 0
    skip_size = 0
    sparse_hash = list(range(0, size))

    if any(l > size for l in lenghts):
        raise ValueError("The sequence of lengths contains an invalid length! (> size)")

    for _ in range(64):
        for length in lenghts:
            end_pos = current_pos + length

            if end_pos < size:
                sparse_hash[current_pos:end_pos] = sparse_hash[current_pos:end_pos][
                    ::-1
                ]
            else:
                n = len(sparse_hash[current_pos:])
                sublist = sparse_hash[current_pos:] + sparse_hash[: end_pos % size]
                sublist = sublist[::-1]
                sparse_hash[current_pos:] = sublist[:n]
                sparse_hash[: end_pos % size] = sublist[n:]

            current_pos = (current_pos + length + skip_size) % size
            skip_size += 1

    dense_hash: list[int] = []

    for i in range(0, len(sparse_hash), 16):
        n = sparse_hash[i]
        for j in range(1, 16):
            n = n ^ sparse_hash[i + j]
        dense_hash.append(n)

    return "".join(f"{n:02x}" for n in dense_hash)


disk: list[list[int]] = []
for i in range(128):
    hash = knot_hash(f"{key}-{i}")
    row: list[int] = []
    for c in hash:
        n = int(c, 16)
        for bit in format(n, "04b"):
            row.append(int(bit))
    disk.append(row)


def bfs(visited: set[CoordsT], start: CoordsT, disk: list[list[int]]) -> None:
    queue: list[CoordsT] = []

    visited.add(start)
    queue.append(start)

    while len(queue) > 0:
        v = queue.pop()

        for vec in [
            CoordsT(0, -1),
            CoordsT(0, 1),
            CoordsT(-1, 0),
            CoordsT(1, 0),
        ]:
            neighbor = CoordsT(v.x + vec.x, v.y + vec.y)
            if (
                0 <= neighbor.x <= 127
                and 0 <= neighbor.y <= 127
                and disk[neighbor.y][neighbor.x] == 1
                and neighbor not in visited
            ):
                visited.add(neighbor)
                queue.append(neighbor)


visited: set[CoordsT] = set()
regions = 0

for y in range(128):
    for x in range(128):
        if CoordsT(x, y) in visited or disk[y][x] == 0:
            continue

        bfs(visited, CoordsT(x, y), disk)
        regions += 1

print(f"Result: {regions}")
