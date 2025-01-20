import typing as t
from dataclasses import dataclass
from math import lcm
from pathlib import Path


@dataclass(frozen=True)
class Vec3:
    x: int
    y: int
    z: int

    def __add__(self, other: t.Any) -> "Vec3":
        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        raise NotImplementedError("Type of other is incompatible!")

    def copy(self) -> "Vec3":
        return Vec3(self.x, self.y, self.z)


@dataclass
class Moon:
    id: int
    position: Vec3
    velocity: Vec3

    def copy(self) -> "Moon":
        return Moon(self.id, self.position.copy(), self.velocity.copy())

    def update_velocity(self, moon: "Moon") -> None:
        delta = [0, 0, 0]
        if self.position.x < moon.position.x:
            delta[0] = 1
        elif self.position.x > moon.position.x:
            delta[0] = -1
        if self.position.y < moon.position.y:
            delta[1] = 1
        elif self.position.y > moon.position.y:
            delta[1] = -1
        if self.position.z < moon.position.z:
            delta[2] = 1
        elif self.position.z > moon.position.z:
            delta[2] = -1
        self.velocity = self.velocity + Vec3(delta[0], delta[1], delta[2])

    def update_position(self) -> None:
        self.position = self.position + self.velocity


with Path(Path(__file__).parent, "input").open() as f:
    moons_raw = [line.rstrip("\n") for line in f]

moons: list[Moon] = []

for i, moon_raw in enumerate(moons_raw):
    coords_raw = moon_raw[1:-1].split(", ")

    moons.append(
        Moon(
            i,
            Vec3(
                int(coords_raw[0].split("=")[1]),
                int(coords_raw[1].split("=")[1]),
                int(coords_raw[2].split("=")[1]),
            ),
            Vec3(0, 0, 0),
        )
    )

moons_ori = [m.copy() for m in moons]
cycles_x: list[int] = [-1 for _ in range(len(moons))]
cycles_y: list[int] = [-1 for _ in range(len(moons))]
cycles_z: list[int] = [-1 for _ in range(len(moons))]
cycle = 1

while True:
    for moon1 in moons:
        for moon2 in moons:
            if moon1 == moon2:
                continue
            moon1.update_velocity(moon2)
    for moon in moons:
        moon.update_position()

    for i, moon in enumerate(moons):
        if (
            cycles_x[i] == -1
            and moon.position.x == moons_ori[i].position.x
            and all(m.velocity.x == 0 for m in moons)
        ):
            cycles_x[i] = cycle
        if (
            cycles_y[i] == -1
            and moon.position.y == moons_ori[i].position.y
            and all(m.velocity.y == 0 for m in moons)
        ):
            cycles_y[i] = cycle
        if (
            cycles_z[i] == -1
            and moon.position.z == moons_ori[i].position.z
            and all(m.velocity.z == 0 for m in moons)
        ):
            cycles_z[i] = cycle
    cycle += 1

    if (
        all(c != -1 for c in cycles_x)
        and all(c != -1 for c in cycles_y)
        and all(c != -1 for c in cycles_z)
    ):
        break

r = lcm(max(cycles_x), max(cycles_y), max(cycles_z))

print(f"Result: {r}")
