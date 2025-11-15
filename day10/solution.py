def read(inp: str):
    ar = []
    for line in inp.splitlines():
        a = line.strip().split()
        if a[0] == "noop":
            ar.append(None)
        else:
            ar.append(int(a[1]))
    return ar


def part_1(inp: str, debug: bool):
    ar = read(inp)
    x = 1
    cc = 1
    ans = 0
    for i, v in enumerate(ar):
        if v is None:
            # print(cc, x)
            if (cc - 20) % 40 == 0:
                ans += cc * x
            cc += 1
        else:
            if (cc - 20) % 40 == 0:
                ans += cc * x
            # print(cc, x)
            cc += 1
            if (cc - 20) % 40 == 0:
                ans += cc * x
            # print(cc, x)
            cc += 1
            x += v
    print(ans)


def part_2(inp: str, debug: bool):
    ar = read(inp)
    x = 1
    cc = 1
    screen = [["."] * 40 for _ in range(6)]
    sprite = 0
    for i, v in enumerate(ar):
        if v is None:
            # print(cc, x)
            if x + 1 >= sprite % 40 >= x - 1:
                screen[sprite // 40][sprite % 40] = "#"
            cc += 1
            sprite += 1
        else:
            if x + 1 >= sprite % 40 >= x - 1:
                screen[sprite // 40][sprite % 40] = "#"
            # print(cc, x)
            cc += 1
            sprite += 1
            if x + 1 >= sprite % 40 >= x - 1:
                screen[sprite // 40][sprite % 40] = "#"
            # print(cc, x)
            cc += 1
            sprite += 1
            x += v

    for i in range(6):
        print("".join(screen[i]))
