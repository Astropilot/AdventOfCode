import typing as t
from dataclasses import dataclass
from pathlib import Path


@dataclass
class TreeNode:
    type: t.Literal["f", "d"]
    name: str
    size: int
    parent: "TreeNode | None"
    children: list["TreeNode"]


root = TreeNode("d", "/", 0, None, [])

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

current_directory = root
for line in lines:
    if line.startswith("$ cd"):
        folder = line.split(" ")[-1]
        if folder == "/":
            current_directory = root
        elif folder == ".." and current_directory.parent is not None:
            current_directory = current_directory.parent
        else:
            for child in current_directory.children:
                if child.type == "d" and child.name == folder:
                    current_directory = child
                    break
        continue
    elif line == "$ ls":
        continue

    dir_or_size, name = line.split(" ")

    if dir_or_size == "dir":
        current_directory.children.append(TreeNode("d", name, 0, current_directory, []))
    else:
        current_directory.children.append(
            TreeNode("f", name, int(dir_or_size), current_directory, [])
        )

total_size = 0


def count_folder(node: TreeNode) -> int:
    global total_size

    if node.type == "f":
        return node.size

    size = 0
    for child in node.children:
        size += count_folder(child)

    if size <= 100000:
        total_size += size

    return size


count_folder(root)

print(f"Result: {total_size}")  # Result: 1844187
