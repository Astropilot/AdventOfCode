from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

gamma_rate_b = ""
epsilon_rate_b = ""

for bit_idx in range(len(lines[0])):
    bit1 = 0
    bit0 = 0
    for line in lines:
        if line[bit_idx] == "0":
            bit0 += 1
        else:
            bit1 += 1
    if bit1 > bit0:
        gamma_rate_b += "1"
        epsilon_rate_b += "0"
    else:
        gamma_rate_b += "0"
        epsilon_rate_b += "1"

result = int(gamma_rate_b, 2) * int(epsilon_rate_b, 2)

print(f"Result: {result}")
