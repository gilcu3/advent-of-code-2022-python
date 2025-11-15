def read(inp: str):
    lines = list(inp.splitlines())
    ar = []
    for i, line in enumerate(lines):
        if len(line) == 0:
            steps = lines[i + 1]
            return ar, steps
        ar.append(line.rstrip("\n"))
    assert False


def part_1(inp: str, debug: bool):
    ar, steps = read(inp)
    n = len(ar)
    m = max(len(ar[i]) for i in range(n))
    for i in range(n):
        ar[i] = ar[i] + " " * (m - len(ar[i]))
    dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    nxt = [[[(i, j) for j in range(m)] for i in range(n)] for _ in range(4)]
    for i in range(n):
        for j in range(m):
            if ar[i][j] != "#":
                for t in range(2, 4):
                    ni, nj = (i + dd[t][0]) % n, (j + dd[t][1]) % m
                    if ar[ni][nj] == " ":
                        nxt[t][i][j] = nxt[t][ni][nj]
                    else:
                        nxt[t][i][j] = (ni, nj)
    for i in range(n):
        for j in range(m):
            if ar[i][j] != "#":
                for t in range(2, 4):
                    ni, nj = (i + dd[t][0]) % n, (j + dd[t][1]) % m
                    if ar[ni][nj] == " ":
                        nxt[t][i][j] = nxt[t][ni][nj]
                    else:
                        nxt[t][i][j] = (ni, nj)
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if ar[i][j] != "#":
                for t in range(0, 2):
                    ni, nj = (i + dd[t][0]) % n, (j + dd[t][1]) % m
                    if ar[ni][nj] == " ":
                        nxt[t][i][j] = nxt[t][ni][nj]
                    else:
                        nxt[t][i][j] = (ni, nj)
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if ar[i][j] != "#":
                for t in range(0, 2):
                    ni, nj = (i + dd[t][0]) % n, (j + dd[t][1]) % m
                    if ar[ni][nj] == " ":
                        nxt[t][i][j] = nxt[t][ni][nj]
                    else:
                        nxt[t][i][j] = (ni, nj)

    def stepin(cur, curs, d):
        for _ in range(curs):
            ncur = nxt[d][cur[0]][cur[1]]
            if ar[ncur[0]][ncur[1]] != "#":
                cur = ncur
            else:
                break
        return cur

    cur = (0, 0) if ar[0][0] == "." else nxt[0][0][0]
    curs = 0
    d = 0
    for s in steps:
        if s == "R":
            if curs > 0:
                cur = stepin(cur, curs, d)
            curs = 0
            d = (d + 1) % 4
        elif s == "L":
            if curs > 0:
                cur = stepin(cur, curs, d)
            curs = 0
            d = (d - 1) % 4
        elif s == "\n":
            if curs > 0:
                cur = stepin(cur, curs, d)
        else:
            curs = curs * 10 + int(s)
    ans = 1000 * (cur[0] + 1) + 4 * (cur[1] + 1) + d
    print(ans)


def part_2(inp: str, debug: bool):
    ar, steps = read(inp)

    nn = 0
    for i in range(len(ar)):
        for j in range(len(ar[i])):
            if ar[i][j] != " ":
                nn += 1
    nn //= 6
    nn = int(nn ** (1 / 2))
    # print(nn)

    n = len(ar)
    m = max(len(ar[i]) for i in range(n))
    for i in range(n):
        ar[i] = ar[i] + (" " * (m - len(ar[i])))
    # for i, a in enumerate(ar):
    #     print('%2d' % i, a)

    dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    nxt = [[[(i, j, t) for j in range(m)] for i in range(n)] for t in range(4)]
    for i in range(n):
        for j in range(m):
            if ar[i][j] != "#":
                for t in range(2, 4):
                    ni, nj = (i + dd[t][0]) % n, (j + dd[t][1]) % m
                    if ar[ni][nj] != " ":
                        nxt[t][i][j] = (ni, nj, t)
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if ar[i][j] != "#":
                for t in range(0, 2):
                    ni, nj = (i + dd[t][0]) % n, (j + dd[t][1]) % m
                    if ar[ni][nj] != " ":
                        nxt[t][i][j] = (ni, nj, t)

    def fix(i0, di, j0, dj):
        ii = i0
        jj = j0
        ti = (di + 1) % 4
        tj = (dj - 1) % 4
        for _ in range(nn):
            # print(ii, jj)
            nxt[ti][ii[0]][ii[1]] = (jj[0], jj[1], (tj + 2) % 4)
            nxt[tj][jj[0]][jj[1]] = (ii[0], ii[1], (ti + 2) % 4)
            ii = (ii[0] + dd[di][0], ii[1] + dd[di][1])
            jj = (jj[0] + dd[dj][0], jj[1] + dd[dj][1])

    fix((1 * nn, 1 * nn), 1, (2 * nn, 0 * nn), 0)
    fix((0 * nn + nn - 1, 2 * nn), 0, (1 * nn, 1 * nn + nn - 1), 1)
    fix((3 * nn, 0 * nn), 1, (0 * nn, 1 * nn), 0)
    fix((2 * nn, 0 * nn), 1, (0 * nn + nn - 1, 1 * nn), 3)
    fix((2 * nn + nn - 1, 1 * nn + nn - 1), 3, (0 * nn, 2 * nn + nn - 1), 1)
    fix((3 * nn + nn - 1, 0 * nn + nn - 1), 3, (2 * nn + nn - 1, 1 * nn + nn - 1), 2)
    fix((3 * nn + nn - 1, 0 * nn), 0, (0 * nn, 2 * nn), 0)

    def stepin(cur, curs):
        for _ in range(curs):
            ncur = nxt[cur[2]][cur[0]][cur[1]]
            if ar[ncur[0]][ncur[1]] != "#":
                cur = ncur
            else:
                break
        return cur

    cur = (0, nn, 0)
    curs = 0
    for s in steps:
        if s == "R":
            if curs > 0:
                cur = stepin(cur, curs)
            curs = 0
            cur = (cur[0], cur[1], (cur[2] + 1) % 4)
        elif s == "L":
            if curs > 0:
                cur = stepin(cur, curs)
            curs = 0
            cur = (cur[0], cur[1], (cur[2] - 1) % 4)
        elif s == "\n":
            if curs > 0:
                cur = stepin(cur, curs)
        else:
            curs = curs * 10 + int(s)
    ans = 1000 * (cur[0] + 1) + 4 * (cur[1] + 1) + cur[2]
    print(ans)
