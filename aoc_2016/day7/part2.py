from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

ip_count = 0

for ip in lines:
    hypernet = False
    all_aba: set[str] = set()
    all_bab: set[str] = set()
    for i in range(len(ip) - 2):
        if ip[i] == "[":
            hypernet = True
            continue
        elif ip[i] == "]":
            hypernet = False
            continue
        if ip[i] == ip[i + 2] and ip[i] != ip[i + 1]:
            if hypernet:
                all_bab.add(ip[i] + ip[i + 1] + ip[i + 2])
            else:
                all_aba.add(ip[i] + ip[i + 1] + ip[i + 2])

    for aba in all_aba:
        bab = aba[1] + aba[0] + aba[1]
        if bab in all_bab:
            ip_count += 1
            break

print(f"Result: {ip_count}")
