def read(inp: str):
    elfs = []
    for line in inp.splitlines():
        s = line.strip()
        elfs.append(s)
    return elfs


def val(c):
    if c.islower():
        return ord(c) - ord("a") + 1
    else:
        return ord(c) - ord("A") + 27


def part_1(inp: str, debug: bool):
    elfs = read(inp)
    ans = 0
    for e in elfs:
        a, b = e[: len(e) // 2], e[len(e) // 2 :]
        dd = set()
        for c in a:
            dd.add(c)
        common = None
        for c in b:
            if c in dd:
                common = c
                break
        ans += val(common)
    print(ans)


def part_2(inp: str, debug: bool):
    elfs = read(inp)
    ans = 0
    for i in range(0, len(elfs), 3):
        dd = {}
        for c in elfs[i]:
            dd[c] = 1
        for c in elfs[i + 1]:
            if c in dd and dd[c] == 1:
                dd[c] = 2
        for c in elfs[i + 2]:
            if c in dd and dd[c] == 2:
                dd[c] = 3
        for a, b in dd.items():
            if b == 3:
                ans += val(a)
                break
    print(ans)
