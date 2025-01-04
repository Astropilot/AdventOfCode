from functools import cache
from pathlib import Path

compressed_file = Path(Path(__file__).parent, "input").read_text()


@cache
def uncompress_size(compressed: str) -> int:
    size = 0
    idx = 0

    while idx < len(compressed):
        if compressed[idx] == "(":
            x_idx = compressed.find("x", idx + 1)
            close_marker_idx = compressed.find(")", x_idx + 1)
            length = int(compressed[idx + 1 : x_idx])
            repeat = int(compressed[x_idx + 1 : close_marker_idx])

            size += uncompress_size(
                compressed[close_marker_idx + 1 : close_marker_idx + 1 + length]
                * repeat
            )
            idx = close_marker_idx + length + 1
        else:
            size += 1
            idx += 1

    return size


print(uncompress_size(compressed_file))
