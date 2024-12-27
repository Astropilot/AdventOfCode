from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")


@dataclass
class Module(ABC):
    name: str
    destinations: list[str]

    @abstractmethod
    def handle_signal(self, source: str, signal: int) -> int | None:
        raise NotImplementedError("")


@dataclass
class FlipFlopModule(Module):
    active: bool = False

    def handle_signal(self, source: str, signal: int) -> int | None:
        if signal == 1:
            return None
        self.active = not self.active

        return 1 if self.active else 0


@dataclass
class ConjunctionModule(Module):
    memory: dict[str, int] = field(default_factory=dict)

    def add_source_in_memory(self, source: str) -> None:
        self.memory[source] = 0

    def handle_signal(self, source: str, signal: int) -> int | None:
        self.memory[source] = signal

        if all(s == 1 for s in self.memory.values()):
            return 0
        return 1


@dataclass
class BroadcasterModule(Module):
    def handle_signal(self, source: str, signal: int) -> int | None:
        return signal


@dataclass
class ButtonModule(Module):
    def handle_signal(self, source: str, signal: int) -> int | None:
        return 0


modules: dict[str, Module] = {}

for line in lines:
    module_raw, dest_raw = line.split(" -> ")
    destinations = dest_raw.split(", ")

    if module_raw[0] == "%":
        module_name = module_raw[1:]
        modules[module_name] = FlipFlopModule(module_name, destinations)
    elif module_raw[0] == "&":
        module_name = module_raw[1:]
        modules[module_name] = ConjunctionModule(module_name, destinations)
    else:  # Broadcaster
        modules["broadcaster"] = BroadcasterModule("broadcaster", destinations)

modules["button"] = ButtonModule("button", ["broadcaster"])

# Fill conjunction
for conjunction_module in [
    m for m in modules.values() if isinstance(m, ConjunctionModule)
]:
    for module in modules.values():
        if conjunction_module.name in module.destinations:
            conjunction_module.add_source_in_memory(module.name)

low_signal_count = 0
high_signal_count = 0
i = 1

while i < 1000 + 1:
    job_queue: list[tuple[str, int, str]] = [("button", 0, "broadcaster")]

    while len(job_queue) > 0:
        job = job_queue.pop(0)

        if job[1] == 0:
            low_signal_count += 1
        else:
            high_signal_count += 1

        if job[2] not in modules:  # Edge case for sample2 with untyped module
            continue

        module = modules[job[2]]

        signal = module.handle_signal(job[0], job[1])

        if signal is None:
            continue

        for destination in module.destinations:
            job_queue.append((module.name, signal, destination))

    i += 1

print(f"Result: {low_signal_count * high_signal_count}")
