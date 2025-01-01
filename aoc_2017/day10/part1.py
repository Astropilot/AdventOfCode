from pathlib import Path

lengths = [int(n) for n in Path(Path(__file__).parent, "input").read_text().split(",")]


def knot_hash(size: int, lenghts: list[int]) -> list[int]:
    numbers = list(range(0, size))
    current_pos = 0
    skip_size = 0

    if any(l > size for l in lenghts):
        raise ValueError("The sequence of lengths contains an invalid length! (> size)")

    for length in lenghts:
        end_pos = current_pos + length

        if end_pos < size:
            numbers[current_pos:end_pos] = numbers[current_pos:end_pos][::-1]
        else:
            n = len(numbers[current_pos:])
            sublist = numbers[current_pos:] + numbers[: end_pos % size]
            sublist = sublist[::-1]
            numbers[current_pos:] = sublist[:n]
            numbers[: end_pos % size] = sublist[n:]

        current_pos = (current_pos + length + skip_size) % size
        skip_size += 1

    return numbers


hash = knot_hash(256, lengths)

print(f"Result: {hash[0] * hash[1]}")
