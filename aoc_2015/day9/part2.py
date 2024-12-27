from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    paths = [line.rstrip("\n") for line in f]

NEIGHBORS: dict[str, dict[str, int]] = {}

for path in paths:
    mapping, distance_raw = path.split(" = ")
    city_from, city_to = mapping.split(" to ")
    distance = int(distance_raw)

    d = NEIGHBORS.setdefault(city_from, {})
    d[city_to] = distance

    d = NEIGHBORS.setdefault(city_to, {})
    d[city_from] = distance


def shortest_distance(city: str, cities: frozenset[str]) -> int:
    neighbors = frozenset(NEIGHBORS[city].keys())
    neighbors = neighbors.intersection(cities)

    distances: list[int] = []

    for neighbor in neighbors:
        available_cities = cities.difference([city, neighbor])

        distances.append(
            NEIGHBORS[city][neighbor] + shortest_distance(neighbor, available_cities)
        )

    return max(distances) if len(distances) > 0 else 0


cities = frozenset(NEIGHBORS.keys())

result = max(shortest_distance(city, cities) for city in cities)

print(f"Result: {result}")
