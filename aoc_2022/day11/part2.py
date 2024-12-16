import typing as t
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Monkey:
    items: list[int]
    operation_operator: t.Literal["*", "+"]
    operation_operand: int | None
    test: int
    test_result: dict[bool, int]
    inspections: int = 0


with Path(Path(__file__).parent, "sample").open() as f:
    lines = [line.rstrip("\n") for line in f]

monkeys: list[Monkey] = []

for i in range(0, len(lines), 7):
    _, items_list = lines[i + 1].split(": ")
    items = list(map(int, items_list.split(", ")))

    operator, operand = lines[i + 2].removeprefix("  Operation: new = old ").split(" ")

    test = int(lines[i + 3].removeprefix("  Test: divisible by "))
    test_result = {
        True: int(lines[i + 4].removeprefix("    If true: throw to monkey ")),
        False: int(lines[i + 5].removeprefix("    If false: throw to monkey ")),
    }

    monkeys.append(
        Monkey(
            items,
            operator,  # type: ignore
            None if operand == "old" else int(operand),
            test,
            test_result,
        )
    )


def reverse_operation(
    item: int, operator: t.Literal["*", "+"], operand: int | None
) -> int:
    if operator == "+":
        return item
    op = operand if operand is not None else item
    if item % op == 0:
        return item // op
    return item


for round in range(10000):
    for monkey in monkeys:
        while len(monkey.items):
            monkey.inspections += 1

            item = monkey.items.pop(0)
            op = (
                monkey.operation_operand
                if monkey.operation_operand is not None
                else item
            )
            if monkey.operation_operator == "*":
                item *= op
            else:
                item += op
            monkey_dest = monkey.test_result[item % monkey.test == 0]

            # if item % monkey.test == 0:
            #     item = monkey.test
            # else:
            #     #     item = item
            #     item = reverse_operation(
            #         item,
            #         monkeys[monkey_dest].operation_operator,
            #         monkeys[monkey_dest].operation_operand,
            #     )
            # TODO

            monkeys[monkey_dest].items.append(item)

    if round + 1 in (1, 20, 1000):
        print(f"== After round {round+1} ==")
        for idx, monkey in enumerate(monkeys):
            print(f"Monkey {idx} inspected items {monkey.inspections} times.")
    # print(f"== After round {round+1} ==")
    # for idx, monkey in enumerate(monkeys):
    #     print(f"Monkey {idx} items: {monkey.items}")

r = sorted(monkeys, key=lambda m: m.inspections, reverse=True)

print(f"Result: {r[0].inspections * r[1].inspections}")  # Result:
