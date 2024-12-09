from pathlib import Path
from typing import Literal, NamedTuple, cast

disk_map = Path(Path(__file__).parent, "input").read_text()


class FileBlock(NamedTuple):
    block_type: Literal["file"]
    file_id: int
    position: int
    size: int


class FreeBlock(NamedTuple):
    block_type: Literal["free"]
    position: int
    size: int


blocks: list[FileBlock | FreeBlock] = []
file_blocks_reverse: list[FileBlock] = []

# Expand
file_id = 0
for i in range(len(disk_map)):
    n = int(disk_map[i])

    if len(blocks) == 0:
        position = 0
    else:
        position = blocks[-1].position + blocks[-1].size

    if i % 2 == 0:
        blocks.append(FileBlock("file", file_id, position, n))
        file_blocks_reverse.insert(0, FileBlock("file", file_id, position, n))
        file_id += 1
    else:
        blocks.append(FreeBlock("free", position, n))


def find_freeblock(fileblock: FileBlock) -> int | None:
    freeblocks = [
        i
        for i, b in enumerate(blocks)
        if b.block_type == "free"
        and b.position < fileblock.position
        and b.size >= fileblock.size
    ]

    if len(freeblocks) == 0:
        return None
    return freeblocks[0]


# Moving
for file_block in file_blocks_reverse:
    i_free = find_freeblock(file_block)

    if i_free is None:
        continue

    free_block = cast(FreeBlock, blocks.pop(i_free))

    blocks.insert(
        blocks.index(file_block),
        FreeBlock("free", file_block.position, file_block.size),
    )
    blocks.insert(
        i_free,
        FileBlock("file", file_block.file_id, free_block.position, file_block.size),
    )
    blocks.remove(file_block)

    if file_block.size < free_block.size:
        blocks.insert(
            i_free + 1,
            FreeBlock(
                "free",
                free_block.position + file_block.size,
                free_block.size - file_block.size,
            ),
        )

# Checksum
checksum = 0
for file_block in [b for b in blocks if b.block_type == "file"]:
    for i in range(file_block.position, file_block.position + file_block.size):
        checksum += i * file_block.file_id

print(f"Result: {checksum}")  # Result: 6448168620520
