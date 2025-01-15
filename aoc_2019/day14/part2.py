import typing as t
from math import ceil
from pathlib import Path


class MaterialT(t.NamedTuple):
    name: str
    quantity: int


with Path(Path(__file__).parent, "input").open() as f:
    rows = [line.rstrip("\n") for line in f]

reactions: dict[MaterialT, list[MaterialT]] = {}

for reaction_raw in rows:
    m_input, m_output = reaction_raw.split(" => ")
    o_qty, o_name = m_output.split(" ")

    materials = reactions.setdefault(MaterialT(o_name, int(o_qty)), [])

    for m in m_input.split(", "):
        m_qty, m_name = m.split(" ")
        materials.append(MaterialT(m_name, int(m_qty)))

ore_required = 0
fuel_count = 2940000  # Found by trial and error

# TODO: Find a better algorithm than just bruteforcing the whole thing :(

while ore_required <= 1000000000000:
    required_materials: list[MaterialT] = []
    stock_materials: dict[str, int] = {}
    ore_required = 0

    required_materials.append(MaterialT("FUEL", fuel_count))

    while len(required_materials) > 0:
        material = required_materials.pop()
        needed_qty = material.quantity - stock_materials.setdefault(material.name, 0)

        if needed_qty <= 0:
            stock_materials[material.name] -= material.quantity
            continue

        produced_material, needed_materials = next(
            (k, v) for k, v in reactions.items() if k.name == material.name
        )

        if needed_qty % produced_material.quantity == 0:
            quantifier = needed_qty // produced_material.quantity
        else:
            quantifier = ceil(needed_qty / produced_material.quantity)
        total_produced = produced_material.quantity * quantifier

        needed_materials = [
            MaterialT(m.name, m.quantity * quantifier) for m in needed_materials
        ]

        if total_produced > needed_qty:
            stock_materials[material.name] = total_produced - needed_qty
        else:
            stock_materials[material.name] = 0

        if all(m.name == "ORE" for m in needed_materials):
            ore_required += sum(m.quantity for m in needed_materials)
        else:
            required_materials.extend(needed_materials)

    fuel_count += 1

print(ore_required)
print(f"Result: {fuel_count}")
