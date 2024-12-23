from collections.abc import Generator
from pathlib import Path
from typing import Any

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]


def bron_kerbosch(
    r: set[str], p: set[str], x: set[str], adj_list: dict[str, set[str]]
) -> Generator[set[str], Any, None]:
    if not p and not x:
        yield r
    while p:
        v = p.pop()
        yield from bron_kerbosch(
            r.union({v}),
            p.intersection(adj_list[v]),
            x.intersection(adj_list[v]),
            adj_list,
        )
        x.add(v)


adj_list: dict[str, set[str]] = {}

for line in lines:
    pc1, pc2 = line.split("-")

    adj_list.setdefault(pc1, set()).add(pc2)
    adj_list.setdefault(pc2, set()).add(pc1)

cliques = list(bron_kerbosch(set(), set(adj_list.keys()), set(), adj_list))

max_clique_size = max(len(c) for c in cliques)

max_clique = next(c for c in cliques if len(c) == max_clique_size)

password = ",".join(sorted(max_clique))

print(f"Result: {password}")  # Result: aw,fk,gv,hi,hp,ip,jy,kc,lk,og,pj,re,sr
