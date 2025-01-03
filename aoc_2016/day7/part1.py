from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

ip_count = 0

for ip in lines:
    hypernet = False
    has_abba = False
    has_abba_hypernet = False
    for i in range(len(ip) - 3):
        if ip[i] == "[":
            hypernet = True
            continue
        elif ip[i] == "]":
            hypernet = False
            continue
        if ip[i] != ip[i + 1] and ip[i] == ip[i + 3] and ip[i + 1] == ip[i + 2]:
            if hypernet:
                has_abba_hypernet = True
            else:
                has_abba = True

    if has_abba and not has_abba_hypernet:
        ip_count += 1

print(f"Result: {ip_count}")
