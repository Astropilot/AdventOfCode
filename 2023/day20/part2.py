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

    @abstractmethod
    def is_original_state(self) -> bool:
        raise NotImplementedError("")


@dataclass
class FlipFlopModule(Module):
    active: bool = False

    def handle_signal(self, source: str, signal: int) -> int | None:
        if signal == 1:
            return None
        self.active = not self.active

        return 1 if self.active else 0

    def is_original_state(self) -> bool:
        return self.active is False


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

    def is_original_state(self) -> bool:
        return all(m == 0 for m in self.memory.values())


@dataclass
class BroadcasterModule(Module):
    def handle_signal(self, source: str, signal: int) -> int | None:
        return signal

    def is_original_state(self) -> bool:
        return True


@dataclass
class ButtonModule(Module):
    def handle_signal(self, source: str, signal: int) -> int | None:
        return 0

    def is_original_state(self) -> bool:
        return True


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


def fewest_button_press_for_module(module: Module) -> int:
    return 0
