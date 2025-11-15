def read(inp: str):
    ar = []
    dd = {"ore": 0, "clay": 1, "obsidian": 2, "geode": 3}
    for line in inp.splitlines():
        t = line.split(".")
        cur = [tuple()] * 4
        for j, r in enumerate(t):
            rr = r.strip(".").split()
            now = False
            cc = [0, 0, 0, 0]
            for i, w in enumerate(rr):
                if w == "robot":
                    now = True
                if now and w in dd.keys():
                    cc[dd[w]] = int(rr[i - 1])
            if now:
                cur[j] = tuple(cc)
        ar.append(cur)

    return ar


dp = {}
best = 0


def rec(t, cur, crobot, price):
    global best
    if t == 0:
        best = max(cur[3], best)
        return cur[3]

    if t * (t - 1) // 2 + crobot[3] * t + cur[3] <= best:
        return 0
    if min(crobot[j] >= price[3][j] for j in range(4)) and min(
        cur[j] >= price[3][j] for j in range(4)
    ):
        return t * (t - 1) // 2 + crobot[3] * t + cur[3]
    if (t, cur, crobot) in dp:
        return dp[(t, cur, crobot)]

    ans = 0
    for i in range(3, -1, -1):
        if min([cur[j] >= price[i][j] for j in range(4)]):
            cans = rec(
                t - 1,
                tuple(cur[j] - price[i][j] + crobot[j] for j in range(4)),
                tuple(crobot[j] + (1 if j == i else 0) for j in range(4)),
                price,
            )
            if cans > ans:
                ans = cans
    # no new robot
    cans = rec(t - 1, tuple(cur[i] + crobot[i] for i in range(4)), crobot, price)
    if cans > ans:
        ans = cans

    dp[(t, cur, crobot)] = ans
    return ans


def rec_(t, cur, crobot, price):
    global best
    if t == 0:
        best = max(cur[3], best)
        return cur[3]

    if t * (t - 1) // 2 + cur[3] <= best:
        return 0
    if min(crobot[j] >= price[3][j] for j in range(3)) and min(
        cur[j] >= price[3][j] for j in range(3)
    ):
        return t * (t - 1) // 2 + cur[3]
    if (t, cur[:3], crobot[:3]) in dp:
        best = max(dp[(t, cur[:3], crobot[:3])] + cur[3], best)
        return dp[(t, cur[:3], crobot[:3])] + cur[3]

    ans = 0
    for i in range(3, -1, -1):
        nt = 0
        for j in range(3):
            if crobot[j] == 0:
                nt = max(nt, 10**9 if price[i][j] > cur[j] else 0)
            else:
                nt = max(nt, (price[i][j] - cur[j] + crobot[j] - 1) // crobot[j])
        if i <= 2:
            if min(crobot[i] >= price[j][i] for j in range(4)):
                break
        if nt >= 0 and nt < t:
            cans = rec_(
                t - nt - 1,
                tuple(
                    (cur[j] + (nt + 1) * crobot[j] - price[i][j])
                    if j < 3
                    else (cur[j] + ((t - nt - 1) if j == i else 0))
                    for j in range(4)
                ),
                tuple(crobot[j] + (1 if j == i else 0) for j in range(4)),
                price,
            )
            if cans > ans:
                ans = cans
    # no new robot
    cans = cur[3]
    if cans > ans:
        ans = cans

    dp[(t, cur[:3], crobot[:3])] = ans - cur[3]
    return ans


def part_1(inp: str, debug: bool):
    global best
    ar = read(inp)
    tot = 24
    ans = 0
    for i, b in enumerate(ar):
        dp.clear()
        best = 0
        cur = rec_(tot, (0, 0, 0, 0), (1, 0, 0, 0), b)
        ans += cur * (i + 1)
    print(ans)


def part_2(inp: str, debug: bool):
    global best
    ar = read(inp)
    tot = 32
    ans = 1
    for i, b in enumerate(ar[:3]):
        dp.clear()
        best = 0
        cur = rec_(tot, (0, 0, 0, 0), (1, 0, 0, 0), b)
        ans *= cur
    print(ans)
