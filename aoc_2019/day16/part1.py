from pathlib import Path

input = [int(c) for c in Path(Path(__file__).parent, "input").read_text()]


def compute_phase(input: list[int]) -> list[int]:
    output: list[int] = []
    pattern = [0, 1, 0, -1]

    for i in range(len(input)):
        n = 0
        for j, digit in enumerate(input, start=1):
            n += digit * pattern[(j // (i + 1)) % len(pattern)]
        output.append(abs(n) % 10)

    return output


for _ in range(100):
    input = compute_phase(input)

print(f"Result: {''.join([str(n) for n in input[:8]])}")
