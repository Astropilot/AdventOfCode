from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Vec3:
    x: int
    y: int
    z: int

    def add_vec(self, vec: "Vec3") -> "Vec3":
        return Vec3(self.x + vec.x, self.y + vec.y, self.z + vec.z)


@dataclass
class Moon:
    id: int
    position: Vec3
    velocity: Vec3

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
        self.velocity = self.velocity.add_vec(Vec3(delta[0], delta[1], delta[2]))

    def update_position(self) -> None:
        self.position = self.position.add_vec(self.velocity)

    @property
    def total_energy(self) -> int:
        pot = abs(self.position.x) + abs(self.position.y) + abs(self.position.z)
        kin = abs(self.velocity.x) + abs(self.velocity.y) + abs(self.velocity.z)
        return pot * kin


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

for _ in range(1000):
    for moon1 in moons:
        for moon2 in moons:
            if moon1 == moon2:
                continue
            moon1.update_velocity(moon2)
    for moon in moons:
        moon.update_position()

r = sum(moon.total_energy for moon in moons)

print(f"Result: {r}")
