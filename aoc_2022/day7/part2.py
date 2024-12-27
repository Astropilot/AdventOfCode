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


def compute_folder_size(node: TreeNode) -> int:
    if node.type == "f":
        return node.size

    size = 0
    for child in node.children:
        size += compute_folder_size(child)

    node.size = size

    return size


compute_folder_size(root)

space_to_free = 30000000 - (70000000 - root.size)


def find_folder_to_remove(node: TreeNode, space_to_free: int) -> TreeNode | None:
    candidates: list[TreeNode] = []

    for child in node.children:
        if child.type == "f":
            continue
        folder = find_folder_to_remove(child, space_to_free)
        if folder:
            return folder
        if child.size >= space_to_free:
            candidates.append(child)

    if len(candidates) > 0:
        return sorted(candidates, key=lambda c: c.size)[0]

    if node.size >= space_to_free:
        return node
    return None


folder_to_remove = find_folder_to_remove(root, space_to_free)

assert folder_to_remove is not None

print(f"Result: {folder_to_remove.size}")
