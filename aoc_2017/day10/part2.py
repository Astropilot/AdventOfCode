from pathlib import Path

input = Path(Path(__file__).parent, "input").read_text()


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


hash = knot_hash(input)

print(f"Result: {hash}")
