import re
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
class Particle:
    id: int
    position: Vec3
    velocity: Vec3
    acceleration: Vec3

    def update(self) -> None:
        self.velocity = self.velocity.add_vec(self.acceleration)
        self.position = self.position.add_vec(self.velocity)

    @property
    def distance(self) -> int:
        return abs(self.position.x) + abs(self.position.y) + abs(self.position.z)


with Path(Path(__file__).parent, "input").open() as f:
    particles_raw = [line.rstrip("\n") for line in f]

particles: list[Particle] = []

for id, particle_raw in enumerate(particles_raw):
    m = re.match(r"p=<([0-9-,]+)>, v=<([0-9-,]+)>, a=<([0-9-,]+)>", particle_raw)
    assert m is not None
    px, py, pz = [int(n) for n in m.group(1).split(",")]
    vx, vy, vz = [int(n) for n in m.group(2).split(",")]
    ax, ay, az = [int(n) for n in m.group(3).split(",")]
    particles.append(Particle(id, Vec3(px, py, pz), Vec3(vx, vy, vz), Vec3(ax, ay, az)))

for _ in range(5000):
    for particle in particles:
        particle.update()

closest_particle = sorted(particles, key=lambda p: p.distance)[0].id

print(f"Result: {closest_particle}")
