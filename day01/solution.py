def read(inp: str):
    elfs = [[]]
    for line in inp.splitlines():
        line = line.strip()
        if len(line) == 0:
            elfs.append([])
        else:
            elfs[-1].append(int(line))
    return elfs


def part_1(inp: str, debug: bool):
    mx = 0
    elfs = read(inp)
    for e in elfs:
        mx = max(sum(e), mx)
    print(mx)


def part_2(inp: str, debug: bool):
    elfs = read(inp)
    es = [sum(e) for e in elfs]
    ans = sum(sorted(es)[-3:])
    print(ans)
