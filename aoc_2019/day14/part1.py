import typing as t
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

required_materials: list[MaterialT] = []
stock_materials: dict[str, int] = {}
ore_required = 0

materials_fuel = next(v for k, v in reactions.items() if k.name == "FUEL")
required_materials.extend(materials_fuel)

while len(required_materials) > 0:
    material = required_materials.pop()
    needed_qty = material.quantity - stock_materials.setdefault(material.name, 0)

    if needed_qty <= 0:
        stock_materials[material.name] -= material.quantity
        continue

    produced_material, needed_materials = next(
        (k, v) for k, v in reactions.items() if k.name == material.name
    )

    quantifier = 1
    while produced_material.quantity * quantifier < needed_qty:
        quantifier += 1
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

print(f"Result: {ore_required}")
