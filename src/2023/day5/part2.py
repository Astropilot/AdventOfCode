from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

seeds_els = list(map(int, lines[0].split(": ")[1].split(" ")))

seeds_intervals: list[tuple[int, int]] = []

for i in range(0, len(seeds_els) - 1, 2):
    seeds_intervals.append((seeds_els[i], seeds_els[i] + seeds_els[i + 1]))

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


def get_destination_from_mapping(
    source: int, mapping: list[tuple[int, int, int]]
) -> int:
    for m in mapping:
        if m[0] <= source <= m[1]:
            return m[2] + (source - m[0])
    return source


def intervals_to_mapped_groups(
    intervals: list[tuple[int, int]], mapping: list[tuple[int, int, int]]
) -> list[tuple[int, int]]:
    mapped_groups: list[tuple[int, int]] = []
    for start, end in intervals:
        # Find best ranges in mapping insersect with the interval
        candidates: list[tuple[int, int, int]] = []
        for m in mapping:
            if m[0] <= end and start <= m[1]:
                candidates.append(m)
        candidates.sort(key=lambda m: min(end, m[1]) - max(start, m[0]), reverse=True)

        sub_intervals = [(start, end)]
        for m in candidates:
            i = 0
            while i < len(sub_intervals):
                sub_i = sub_intervals[i]
                if m[0] <= sub_i[1] and sub_i[0] <= m[1]:
                    intersect = (max(sub_i[0], m[0]), min(sub_i[1], m[1]))
                    mapped_groups.append(
                        (m[2] + (intersect[0] - m[0]), m[2] + (intersect[1] - m[0]))
                    )
                    sub_intervals.pop(i)
                    if sub_i[0] < intersect[0]:
                        sub_intervals.append((sub_i[0], intersect[0] - 1))
                    if sub_i[1] > intersect[1]:
                        sub_intervals.append((intersect[1] + 1, sub_i[1]))
                    i = 0
                else:
                    i += 1
        for sub_i in sub_intervals:
            mapped_groups.append(sub_i)
    return mapped_groups


soils = intervals_to_mapped_groups(seeds_intervals, seed_to_soil_mapping)
fertilizers = intervals_to_mapped_groups(soils, soil_to_fertilizer_mapping)
waters = intervals_to_mapped_groups(fertilizers, fertilizer_to_water_mapping)
lights = intervals_to_mapped_groups(waters, water_to_light_mapping)
temperatures = intervals_to_mapped_groups(lights, light_to_temperature_mapping)
humiditys = intervals_to_mapped_groups(temperatures, temperature_to_humidity_mapping)
locations = intervals_to_mapped_groups(humiditys, humidity_to_location_mapping)

min_location = -1
for h_i in locations:
    if min_location == -1 or h_i[0] < min_location:
        min_location = h_i[0]

print(f"Result: {min_location}")  # Result: 27992443
