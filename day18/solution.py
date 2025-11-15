def read(inp: str):
    ar = []
    for line in inp.splitlines():
        t = tuple(map(int, line.strip().split(",")))
        ar.append(t)
    return ar


dd = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def part_1(inp: str, debug: bool):
    ar = read(inp)
    seen = set()
    for x, y, z in ar:
        seen.add((x, y, z))
    ans = 0
    for c in ar:
        for d in dd:
            nc = (c[0] + d[0], c[1] + d[1], c[2] + d[2])
            if nc not in seen:
                ans += 1
    print(ans)


def updmx(a, b):
    if a is None or a < b:
        return b
    return a


def updmn(a, b):
    if a is None or a > b:
        return b
    return a


def part_2(inp: str, debug: bool):
    ar = read(inp)
    mn = [None, None, None]
    mx = [None, None, None]
    for p in ar:
        for i in range(3):
            mn[i] = updmn(mn[i], p[i] - 1)
            mx[i] = updmx(mx[i], p[i] + 1)
    space = [
        [[-1 for _ in range(mn[2], mx[2] + 1)] for _ in range(mn[1], mx[1] + 1)]
        for _ in range(mn[0], mx[0] + 1)
    ]

    def get_space(t):
        return space[t[0] - mn[0]][t[1] - mn[1]][t[2] - mn[2]]

    def set_space(t, v):
        space[t[0] - mn[0]][t[1] - mn[1]][t[2] - mn[2]] = v

    def bfs(s, c):
        o = get_space(s)
        que = []
        que.append(s)
        set_space(s, c)
        front = 0
        while front < len(que):
            cur = que[front]
            front += 1
            for d in dd:
                ncur = tuple(cur[i] + d[i] for i in range(3))
                pos = True
                for i in range(3):
                    if ncur[i] < mn[i] or ncur[i] > mx[i]:
                        pos = False
                if pos and get_space(ncur) == o:
                    que.append(ncur)
                    set_space(ncur, c)

    for p in ar:
        set_space(p, 0)

    bfs(mn, 1)
    ans = 0
    for t in ar:
        for d in dd:
            nt = tuple(t[i] + d[i] for i in range(3))
            if get_space(nt) == 1:
                ans += 1
    print(ans)
