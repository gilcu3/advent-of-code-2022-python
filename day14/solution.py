def read(inp: str):
    ar = []
    for line in inp.splitlines():
        cur = []
        line = line.strip()
        for a in line.split("->"):
            x, y = a.strip().split(",")
            cur.append((int(x), int(y)))
        ar.append(cur)
    return ar


def part_1(inp: str, debug: bool):
    ar = read(inp)
    mat = set()

    for cur in ar:
        last = cur[0]
        for nxt in cur[1:]:
            dir = [nxt[0] - last[0], nxt[1] - last[1]]
            ll = (abs(dir[0]) + 1) * (abs(dir[1]) + 1)
            if abs(dir[0]) > 0:
                dir[0] = 1 if dir[0] > 0 else -1
            if abs(dir[1]) > 0:
                dir[1] = 1 if dir[1] > 0 else -1
            t = last
            for _ in range(ll):
                mat.add((t[0], t[1]))
                t = (t[0] + dir[0], t[1] + dir[1])
            last = nxt
    mxy = -1
    for x, y in mat:
        mxy = max(mxy, y)

    # print(len(mat), mxy)
    def sim():
        init = [500, 0]
        while init[1] <= mxy:
            if (init[0], init[1] + 1) not in mat:
                init[1] += 1
            elif (init[0] - 1, init[1] + 1) not in mat:
                init[1] += 1
                init[0] -= 1
            elif (init[0] + 1, init[1] + 1) not in mat:
                init[1] += 1
                init[0] += 1
            else:
                mat.add((init[0], init[1]))
                return True
        # print(init)
        return False

    ans = 0
    # print(mat)
    while sim():
        ans += 1
    # print(mat)
    print(ans)


def part_2(inp: str, debug: bool):
    ar = read(inp)
    mat = set()

    for cur in ar:
        last = cur[0]
        for nxt in cur[1:]:
            dir = [nxt[0] - last[0], nxt[1] - last[1]]
            ll = (abs(dir[0]) + 1) * (abs(dir[1]) + 1)
            if abs(dir[0]) > 0:
                dir[0] = 1 if dir[0] > 0 else -1
            if abs(dir[1]) > 0:
                dir[1] = 1 if dir[1] > 0 else -1
            t = last
            for _ in range(ll):
                mat.add((t[0], t[1]))
                t = (t[0] + dir[0], t[1] + dir[1])
            last = nxt
    mxy = -1
    for x, y in mat:
        mxy = max(mxy, y)

    # print(len(mat), mxy)
    def sim():
        init = [500, 0]
        if (init[0], init[1]) in mat:
            return False
        while True:
            if init[1] + 1 == 2 + mxy:
                mat.add((init[0], init[1]))
                return True
            elif (init[0], init[1] + 1) not in mat:
                init[1] += 1
            elif (init[0] - 1, init[1] + 1) not in mat:
                init[1] += 1
                init[0] -= 1
            elif (init[0] + 1, init[1] + 1) not in mat:
                init[1] += 1
                init[0] += 1
            else:
                mat.add((init[0], init[1]))
                return True
        # print(init)
        # return False

    ans = 0
    # print(mat)
    while sim():
        ans += 1
    # print(mat)
    print(ans)
