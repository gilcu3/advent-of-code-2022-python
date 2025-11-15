def read(inp: str):
    a = inp.strip()
    return a


def part_1(inp: str, debug: bool):
    s = read(inp)
    for i in range(len(s) - 3):
        ss = s[i : i + 4]
        a = set()
        for c in ss:
            a.add(c)
        if len(a) == 4:
            ans = i + 4
            break
    print(ans)


def part_2(inp: str, debug: bool):
    s = read(inp)
    for i in range(len(s) - 13):
        ss = s[i : i + 14]
        a = set()
        for c in ss:
            a.add(c)
        if len(a) == 14:
            ans = i + 14
            break
    print(ans)
