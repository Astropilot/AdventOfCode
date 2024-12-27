from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

seeds = list(map(int, lines[0].split(": ")[1].split(" ")))
seed_to_soil_mapping: list[tuple[int, int, int]] = []
soil_to_fertilizer_mapping: list[tuple[int, int, int]] = []
fertilizer_to_water_mapping: list[tuple[int, int, int]] = []
water_to_light_mapping: list[tuple[int, int, int]] = []
light_to_temperature_mapping: list[tuple[int, int, int]] = []
temperature_to_humidity_mapping: list[tuple[int, int, int]] = []
humidity_to_location_mapping: list[tuple[int, int, int]] = []


def read_mapping(
    line_pos: int, lines: list[str], mapping: list[tuple[int, int, int]]
) -> int:
    line_pos += 1
    while line_pos < len(lines) and len(lines[line_pos]):
        mapping_line = list(map(int, lines[line_pos].split(" ")))
        mapping.append(
            (mapping_line[1], mapping_line[1] + (mapping_line[2] - 1), mapping_line[0])
        )
        line_pos += 1

    line_pos += 1
    return line_pos


line_pos = 2

line_pos = read_mapping(line_pos, lines, seed_to_soil_mapping)
line_pos = read_mapping(line_pos, lines, soil_to_fertilizer_mapping)
line_pos = read_mapping(line_pos, lines, fertilizer_to_water_mapping)
line_pos = read_mapping(line_pos, lines, water_to_light_mapping)
line_pos = read_mapping(line_pos, lines, light_to_temperature_mapping)
line_pos = read_mapping(line_pos, lines, temperature_to_humidity_mapping)
line_pos = read_mapping(line_pos, lines, humidity_to_location_mapping)


def get_destination_from_mapping(
    source: int, mapping: list[tuple[int, int, int]]
) -> int:
    for m in mapping:
        if m[0] <= source <= m[1]:
            return m[2] + (source - m[0])
    return source


min_location = -1

for seed in seeds:
    soil = get_destination_from_mapping(seed, seed_to_soil_mapping)
    fertilizer = get_destination_from_mapping(soil, soil_to_fertilizer_mapping)
    water = get_destination_from_mapping(fertilizer, fertilizer_to_water_mapping)
    light = get_destination_from_mapping(water, water_to_light_mapping)
    temperature = get_destination_from_mapping(light, light_to_temperature_mapping)
    humidity = get_destination_from_mapping(
        temperature, temperature_to_humidity_mapping
    )
    location = get_destination_from_mapping(humidity, humidity_to_location_mapping)

    if min_location == -1 or location < min_location:
        min_location = location

print(f"Result: {min_location}")
