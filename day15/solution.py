def read(inp: str):
    ar = []
    for line in inp.splitlines():
        line = line.strip()
        for c in "x=y,":
            line = line.replace(c, "")

        l1, l2 = line.split(":")

        s1 = list(map(int, l1.split()[2:]))
        s2 = list(map(int, l2.split()[4:]))
        ar.append((s1, s2))
    return ar


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part_1(inp: str, debug: bool):
    y = 10
    y = 2000000
    ar = read(inp)
    ans = set()
    beacons = set()
    for s, b in ar:
        top = dist(s, b) - abs(s[1] - y)
        if b[1] == y:
            beacons.add(b[0])
        if top >= 0:
            # print(s, b, -top + s[0], top + s[0])
            for x in range(-top + s[0], top + s[0] + 1):
                ans.add(x)

    print(len(ans) - len(beacons))


def part_2(inp: str, debug: bool):
    # ttop = 20
    ttop = 4000000
    ar = read(inp)
    dsb = [dist(s, b) for s, b in ar]
    fx, fy = None, None

    for y in range(0, ttop + 1):
        cur = []
        mx = 0
        for i, (s, b) in enumerate(ar):
            top = dsb[i] - abs(s[1] - y)
            if top >= 0:
                cur.append((s[0] - top, True))
                cur.append((s[0] + top + 1, False))
                mx = max(mx, s[0] + top + 1)
        on = 0
        for ni, b in sorted(cur):
            if b:
                if on == 0 and ni - 1 >= 0 and ni - 1 <= ttop:
                    fx = ni - 1
                    fy = y
                    break
                on += 1
            else:
                on -= 1
        if mx <= ttop:
            fx = top
            fy = y
        if fx is not None:
            break

    ans = fx * 4000000 + fy
    print(ans)
