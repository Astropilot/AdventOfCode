from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines_splitted = [line.split("   ") for line in f]

left_list = [int(i[0]) for i in lines_splitted]
right_list = [int(i[1]) for i in lines_splitted]

similarity = sum(item * right_list.count(item) for item in left_list)

print(f"Result: {similarity}")
