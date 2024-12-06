from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
blocks = contents.split("\n\n")


def is_distance_one(str1: str, str2: str) -> bool:
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
        if distance > 1:
            break
    return distance == 1


def sum_rows_for_block(block_lines: list[str]) -> tuple[int, bool]:
    lines = block_lines
    first_line = lines[0]
    last_line = lines[-1]

    for y in range(1, len(lines) - 1):
        y_n = len(lines) - 1 - y

        is_distance = is_distance_one(lines[y], first_line)
        if lines[y] == first_line or is_distance:
            is_reflection = True
            is_inner_distance = False
            if y > 1:
                for y2 in range(1, y // 2 + 1):
                    y2_n = y - y2
                    if lines[y2] != lines[y2_n]:
                        d = is_distance_one(lines[y2], lines[y2_n])
                        if is_distance or is_inner_distance or not d:
                            is_reflection = False
                            break
                        elif d:
                            is_inner_distance = True
            if is_reflection and y % 2 == 1 and (is_distance or is_inner_distance):
                return y // 2 + 1, is_distance or is_inner_distance

        is_distance = is_distance_one(lines[y_n], last_line)
        if lines[y_n] == last_line or is_distance:
            is_reflection = True
            is_inner_distance = False
            if (len(lines) - 1) - y_n > 1:
                for y2 in range(y_n + 1, y_n + ((len(lines) - y_n) // 2)):
                    y2_n = y_n - 1 - y2
                    if lines[y2] != lines[y2_n]:
                        d = is_distance_one(lines[y2], lines[y2_n])
                        if is_distance or is_inner_distance or not d:
                            is_reflection = False
                            break
                        elif d:
                            is_inner_distance = True

            if is_reflection and y_n % 2 == 1 and (is_distance or is_inner_distance):
                return y_n + ((len(lines) - y_n) // 2), is_distance or is_inner_distance

    return 0, False


sum_patterns = 0
for block in blocks:
    block_lines = block.split("\n")
    block_transposed: list[str] = []

    for i in range(len(block_lines[0])):
        block_transposed.append("".join(ls[i] for ls in block_lines))

    rows, with_distance = sum_rows_for_block(block_lines)
    cols, with_distance2 = sum_rows_for_block(block_transposed)

    if with_distance:
        sum_patterns += 100 * rows
    else:
        sum_patterns += cols

print(f"Result: {sum_patterns}")  # Result: 40995
