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

total_parts = 0
for ratings in parts_lines.split("\n"):
    rating: dict[str, int] = {}

    for t in ratings[1:-1].split(","):
        rating[t[0]] = int(t[2:])

    status = None
    current_workflow = workflows["in"]

    while status is None:
        for rule in current_workflow:
            if rule[0] is None:
                if rule[1] in ["A", "R"]:
                    status = rule[1]
                    break
                else:
                    current_workflow = workflows[rule[1]]
                    break
            else:
                ra = rating[rule[0][0]]
                if rule[0][1] == "<" and ra < int(rule[0][2:]):
                    if rule[1] in ["A", "R"]:
                        status = rule[1]
                        break
                    else:
                        current_workflow = workflows[rule[1]]
                        break
                elif rule[0][1] == ">" and ra > int(rule[0][2:]):
                    if rule[1] in ["A", "R"]:
                        status = rule[1]
                        break
                    else:
                        current_workflow = workflows[rule[1]]
                        break

    if status == "A":
        for v in rating.values():
            total_parts += v

print(f"Result: {total_parts}")
