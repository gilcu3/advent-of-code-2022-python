def read(inp: str):
    elfs = []
    for line in inp.splitlines():
        a, b = line.strip().split(",")
        a = tuple(map(int, a.split("-")))
        b = tuple(map(int, b.split("-")))
        elfs.append([a, b])
    return elfs


def part_1(inp: str, debug: bool):
    elfs = read(inp)
    ans = 0
    for [(a1, a2), (b1, b2)] in elfs:
        if a2 >= b2 and a1 <= b1:
            ans += 1
        elif a2 <= b2 and a1 >= b1:
            ans += 1
    print(ans)


def part_2(inp: str, debug: bool):
    elfs = read(inp)
    ans = 0
    for [(a1, a2), (b1, b2)] in elfs:
        if a2 >= b2 and a1 <= b2:
            ans += 1
        elif a2 <= b2 and a2 >= b1:
            ans += 1
        elif a1 <= b2 and a1 >= b1:
            ans += 1
    print(ans)
