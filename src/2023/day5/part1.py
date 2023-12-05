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

line_pos = 2

assert lines[line_pos] == "seed-to-soil map:"

line_pos += 1
while len(lines[line_pos]):
    seed_to_soil = list(map(int, lines[line_pos].split(" ")))
    seed_to_soil_mapping.append(
        (seed_to_soil[1], seed_to_soil[1] + (seed_to_soil[2] - 1), seed_to_soil[0])
    )
    line_pos += 1

line_pos += 1

assert lines[line_pos] == "soil-to-fertilizer map:"

line_pos += 1
while len(lines[line_pos]):
    soil_to_fertilizer = list(map(int, lines[line_pos].split(" ")))
    soil_to_fertilizer_mapping.append(
        (
            soil_to_fertilizer[1],
            soil_to_fertilizer[1] + (soil_to_fertilizer[2] - 1),
            soil_to_fertilizer[0],
        )
    )
    line_pos += 1

line_pos += 1

assert lines[line_pos] == "fertilizer-to-water map:"

line_pos += 1
while len(lines[line_pos]):
    fertilizer_to_water = list(map(int, lines[line_pos].split(" ")))
    fertilizer_to_water_mapping.append(
        (
            fertilizer_to_water[1],
            fertilizer_to_water[1] + (fertilizer_to_water[2] - 1),
            fertilizer_to_water[0],
        )
    )
    line_pos += 1

line_pos += 1

assert lines[line_pos] == "water-to-light map:"

line_pos += 1
while len(lines[line_pos]):
    water_to_light = list(map(int, lines[line_pos].split(" ")))
    water_to_light_mapping.append(
        (
            water_to_light[1],
            water_to_light[1] + (water_to_light[2] - 1),
            water_to_light[0],
        )
    )
    line_pos += 1

line_pos += 1

assert lines[line_pos] == "light-to-temperature map:"

line_pos += 1
while len(lines[line_pos]):
    light_to_temperature = list(map(int, lines[line_pos].split(" ")))
    light_to_temperature_mapping.append(
        (
            light_to_temperature[1],
            light_to_temperature[1] + (light_to_temperature[2] - 1),
            light_to_temperature[0],
        )
    )
    line_pos += 1

line_pos += 1

assert lines[line_pos] == "temperature-to-humidity map:"

line_pos += 1
while len(lines[line_pos]):
    temperature_to_humidity = list(map(int, lines[line_pos].split(" ")))
    temperature_to_humidity_mapping.append(
        (
            temperature_to_humidity[1],
            temperature_to_humidity[1] + (temperature_to_humidity[2] - 1),
            temperature_to_humidity[0],
        )
    )
    line_pos += 1

line_pos += 1

assert lines[line_pos] == "humidity-to-location map:"

line_pos += 1
while line_pos < len(lines):
    humidity_to_location = list(map(int, lines[line_pos].split(" ")))
    humidity_to_location_mapping.append(
        (
            humidity_to_location[1],
            humidity_to_location[1] + (humidity_to_location[2] - 1),
            humidity_to_location[0],
        )
    )
    line_pos += 1

# print("seeds", seeds)
# print("seed_to_soil", seed_to_soil_mapping)
# print("soil_to_fertilizer", soil_to_fertilizer_mapping)
# print("fertilizer_to_water", fertilizer_to_water_mapping)
# print("water_to_light", water_to_light_mapping)
# print("light_to_temperature", light_to_temperature_mapping)
# print("temperature_to_humidity", temperature_to_humidity_mapping)
# print("humidity_to_location", humidity_to_location_mapping)


def get_destination_from_mapping(
    source: int, mapping: list[tuple[int, int, int]]
) -> int:
    for m in mapping:
        if m[0] <= source <= m[1]:
            return m[2] + (source - m[0])
    return source


locations: list[int] = []

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

    locations.append(location)

    # print(f"seed {seed}")
    # print(f"\tsoil: {soil}")
    # print(f"\tfertilizer: {fertilizer}")
    # print(f"\twater: {water}")
    # print(f"\tlight: {light}")
    # print(f"\ttemperature: {temperature}")
    # print(f"\thumidity: {humidity}")
    # print(f"\tlocation: {location}")

print(locations)
print(f"Result: {min(locations)}")
