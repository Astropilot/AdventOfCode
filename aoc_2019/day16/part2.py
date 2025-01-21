from pathlib import Path

input = [int(c) for c in Path(Path(__file__).parent, "input").read_text()]

offset = int("".join(str(c) for c in input[:7]), base=10)
input = input * 10000
input = input[offset:]

for _ in range(100):
    output: list[int] = [0] * len(input)

    n = 0
    for j in range(len(input)):
        n += input[j]

    output[0] = n % 10

    for i in range(1, len(input)):
        n = n - input[i - 1]
        output[i] = n % 10

    input = output

print(f"Result: {''.join([str(n) for n in input[:8]])}")
