from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
workflows_lines, parts_lines = contents.split("\n\n")

workflows: dict[str, list[tuple[str | None, str]]] = {}

for wf_line in workflows_lines.split("\n"):
    label, rules_line = wf_line.split("{")
    rules_line = rules_line[:-1]
    rules_raw = rules_line.split(",")
    rules: list[tuple[str | None, str]] = []

    for r in rules_raw:
        data = r.split(":")

        if len(data) == 2:
            rules.append((data[0], data[1]))
        else:
            rules.append((None, data[0]))

    workflows[label] = rules


def constraints_to_perms(constraints: dict[str, tuple[int, int]]) -> int:
    return (
        (constraints["x"][1] - constraints["x"][0] + 1)
        * (constraints["m"][1] - constraints["m"][0] + 1)
        * (constraints["a"][1] - constraints["a"][0] + 1)
        * (constraints["s"][1] - constraints["s"][0] + 1)
    )


def search_permutations(
    constraints: dict[str, tuple[int, int]], rules: list[tuple[str | None, str]]
) -> int:
    permutations = 0
    constraints_copy = constraints.copy()

    for rule in rules:
        if rule[0] is None:  # Is last default rule?
            if rule[1] == "A":
                permutations += constraints_to_perms(constraints_copy)
            elif rule[1] != "R":
                permutations += search_permutations(
                    constraints_copy, workflows[rule[1]]
                )
        else:
            key = rule[0][0]
            val_compare = int(rule[0][2:])
            rule_constraints = constraints_copy.copy()

            if rule[0][1] == "<":
                rule_constraints[key] = (rule_constraints[key][0], val_compare - 1)
                constraints_copy[key] = (val_compare, constraints_copy[key][1])
            else:
                rule_constraints[key] = (val_compare + 1, rule_constraints[key][1])
                constraints_copy[key] = (constraints_copy[key][0], val_compare)

            if rule[1] == "A":
                permutations += constraints_to_perms(rule_constraints)
            elif rule[1] != "R":
                permutations += search_permutations(
                    rule_constraints, workflows[rule[1]]
                )

    return permutations


start: dict[str, tuple[int, int]] = {
    "x": (1, 4000),
    "m": (1, 4000),
    "a": (1, 4000),
    "s": (1, 4000),
}

result = search_permutations(start, workflows["in"])

print(f"Result: {result}")
