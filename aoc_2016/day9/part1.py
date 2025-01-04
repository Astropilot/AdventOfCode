from pathlib import Path

compressed_file = Path(Path(__file__).parent, "input").read_text()

uncompressed_file = ""
idx = 0

while idx < len(compressed_file):
    if compressed_file[idx] == "(":
        x_idx = compressed_file.find("x", idx + 1)
        close_marker_idx = compressed_file.find(")", x_idx + 1)
        length = int(compressed_file[idx + 1 : x_idx])
        repeat = int(compressed_file[x_idx + 1 : close_marker_idx])

        uncompressed_file += (
            compressed_file[close_marker_idx + 1 : close_marker_idx + 1 + length]
            * repeat
        )
        idx = close_marker_idx + length + 1
    else:
        uncompressed_file += compressed_file[idx]
        idx += 1

print(len(uncompressed_file))
