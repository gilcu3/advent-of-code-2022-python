def read(inp: str):
    elfs = []
    for line in inp.splitlines():
        a, b = line.strip().split()
        a, b = ord(a) - ord("A") + 1, ord(b) - ord("X") + 1
        elfs.append((a, b))
    return elfs


def part_1(inp: str, debug: bool):
    elfs = read(inp)
    ans = 0
    for a, b in elfs:
        ans += b
        if b % 3 == (a + 1) % 3:
            ans += 6
        elif b == a:
            ans += 3
    print(ans)


def part_2(inp: str, debug: bool):
    elfs = read(inp)
    ans = 0
    for a, b in elfs:
        if b == 1:
            ans += (a + 1) % 3 + 1
        elif b == 2:
            ans += a + 3
        else:
            ans += a % 3 + 1 + 6
    print(ans)
