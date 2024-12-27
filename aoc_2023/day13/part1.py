from pathlib import Path

contents = Path(Path(__file__).parent, "test").read_text()
blocks = contents.split("\n\n")


def sum_rows_for_block(block_lines: list[str]) -> int:
    lines = block_lines
    first_line = lines[0]
    last_line = lines[-1]

    for y in range(1, len(lines) - 1):
        y_n = len(lines) - 1 - y

        if lines[y] == first_line:
            is_reflection = True
            for y2 in range(1, y // 2 + 1):
                y2_n = y - y2
                if lines[y2] != lines[y2_n]:
                    is_reflection = False
                    break
            if is_reflection and y % 2 == 1:
                return y // 2 + 1
        if lines[y_n] == last_line:
            is_reflection = True
            for y2 in range(y_n + 1, len(lines) - 1):
                y2_n = y_n - 1 - y2
                if lines[y2] != lines[y2_n]:
                    is_reflection = False
                    break
            if is_reflection and y_n % 2 == 1:
                return y_n + ((len(lines) - y_n) // 2)
    return 0


sum_patterns = 0
for block in blocks:
    block_lines = block.split("\n")
    block_transposed: list[str] = []

    for i in range(len(block_lines[0])):
        block_transposed.append("".join(ls[i] for ls in block_lines))

    rows = sum_rows_for_block(block_lines)
    cols = sum_rows_for_block(block_transposed)

    print(f"Block 1: {rows} | {cols}")

    sum_patterns += cols + (100 * rows)

print(f"Result: {sum_patterns}")
