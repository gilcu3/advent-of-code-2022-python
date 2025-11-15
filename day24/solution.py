from math import lcm


def read(inp: str):
    ar = []
    for line in inp.splitlines():
        ar.append(line.rstrip("\n"))
    return ar


def bfs(init, fin, n, m, rows, cols):
    que = []
    lc = lcm(m, n)
    dd = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
    dp = set((0, init))
    que.append((0, init))
    front = 0
    while front < len(que):
        ct, cv = que[front]
        front += 1
        for d in dd:
            nv = (cv[0] + d[0], cv[1] + d[1])
            if (nv[0] <= 0 or nv[0] >= n - 1 or nv[1] <= 0 or nv[1] >= m - 1) and (
                nv != init and nv != fin
            ):
                continue
            crash = False
            for r, rd in rows[nv[0]]:
                if (r - 1 + (ct + 1) * rd) % (m - 2) + 1 == nv[1]:
                    crash = True
                    break
            if crash:
                continue
            for c, cd in cols[nv[1]]:
                if (c - 1 + (ct + 1) * cd) % (n - 2) + 1 == nv[0]:
                    crash = True
                    break
            if crash:
                continue
            ns = ((ct + 1) % lc, nv)
            if ns not in dp:
                if nv == fin:
                    return ct + 1
                dp.add(ns)
                que.append((ct + 1, nv))
    return -1


def part_1(inp: str, debug: bool):
    ar = read(inp)
    n = len(ar)
    m = len(ar[0])
    rows = [[] for _ in range(n)]
    cols = [[] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if ar[i][j] == "<":
                rows[i].append((j, -1))
            elif ar[i][j] == ">":
                rows[i].append((j, 1))
            elif ar[i][j] == "^":
                cols[j].append((i, -1))
            elif ar[i][j] == "v":
                cols[j].append((i, 1))
    ans = bfs((0, 1), (n - 1, m - 2), n, m, rows, cols)
    print(ans)


def bfs2(init, fin, n, m, rows, cols):
    que = []
    lc = lcm(m, n)
    dd = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
    dp = set((0, 0, init))
    que.append((0, 0, init))
    front = 0
    while front < len(que):
        ct, ctrip, cv = que[front]
        front += 1
        for d in dd:
            nv = (cv[0] + d[0], cv[1] + d[1])
            if (nv[0] <= 0 or nv[0] >= n - 1 or nv[1] <= 0 or nv[1] >= m - 1) and (
                nv != init and nv != fin
            ):
                continue
            crash = False
            for r, rd in rows[nv[0]]:
                if (r - 1 + (ct + 1) * rd) % (m - 2) + 1 == nv[1]:
                    crash = True
                    break
            if crash:
                continue
            for c, cd in cols[nv[1]]:
                if (c - 1 + (ct + 1) * cd) % (n - 2) + 1 == nv[0]:
                    crash = True
                    break
            if crash:
                continue

            ntrip = ctrip
            if nv == fin:
                if ctrip == 0:
                    ntrip = 1
                elif ctrip == 2:
                    return ct + 1
            elif nv == init:
                if ctrip == 1:
                    ntrip = 2
            ns = ((ct + 1) % lc, ntrip, nv)
            if ns not in dp:
                dp.add(ns)
                que.append((ct + 1, ntrip, nv))
    return -1


def part_2(inp: str, debug: bool):
    ar = read(inp)
    n = len(ar)
    m = len(ar[0])
    rows = [[] for _ in range(n)]
    cols = [[] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if ar[i][j] == "<":
                rows[i].append((j, -1))
            elif ar[i][j] == ">":
                rows[i].append((j, 1))
            elif ar[i][j] == "^":
                cols[j].append((i, -1))
            elif ar[i][j] == "v":
                cols[j].append((i, 1))
    ans = bfs2((0, 1), (n - 1, m - 2), n, m, rows, cols)
    print(ans)
