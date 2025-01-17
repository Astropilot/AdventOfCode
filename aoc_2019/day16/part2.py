from pathlib import Path

input = [int(c) for c in Path(Path(__file__).parent, "sample").read_text()]


def compute_phase(input: list[int]) -> list[int]:
    output: list[int] = []

    for i in range(len(input)):
        switch = i + 1
        steps = i + 2
        j = i
        delta = 1
        count = 1
        n = 0
        while j < len(input):
            print(f"{input[j]} * {delta} = {input[j] * delta}")
            n += input[j] * delta

            if count % switch == 0:
                j += steps
                delta *= -1
            else:
                j += 1

            count += 1
        output.append(abs(n) % 10)

    return output


input = compute_phase(input)

# Work In Progress
