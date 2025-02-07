from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

for id1 in lines:
    for id2 in lines:
        if id1 == id2:
            continue
        diffs: list[int] = []
        for i in range(len(id1)):
            if id1[i] != id2[i]:
                diffs.append(i)
        if len(diffs) == 1:
            print(f"Result: {id1[:diffs[0]] + id1[diffs[0]+1:]}")
