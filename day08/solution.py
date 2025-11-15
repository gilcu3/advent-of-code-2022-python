def read(inp: str):
    ar = []
    for line in inp.splitlines():
        ar.append([int(c) for c in line.strip()])
    return ar


def part_1(inp: str, debug: bool):
    ar = read(inp)
    n = len(ar)
    m = len(ar[0])
    vis0 = [[[0, 0] for _ in range(m)] for _ in range(n)]
    vis1 = [[[0, 0] for _ in range(m)] for _ in range(n)]
    vis = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                vis0[i][j] = [ar[i][j], ar[i][j]]
                vis[i][j] = True
            else:
                vis0[i][j][0] = vis0[i - 1][j][0]
                if vis0[i - 1][j][0] < ar[i][j]:
                    vis0[i][j][0] = ar[i][j]
                    vis[i][j] = True
                vis0[i][j][1] = vis0[i][j - 1][1]
                if vis0[i][j - 1][1] < ar[i][j]:
                    vis0[i][j][1] = ar[i][j]
                    vis[i][j] = True
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if i == n - 1 or j == m - 1:
                vis1[i][j] = (ar[i][j], ar[i][j])
                vis[i][j] = True
            else:
                vis1[i][j][0] = vis1[i + 1][j][0]
                if vis1[i + 1][j][0] < ar[i][j]:
                    vis1[i][j][0] = ar[i][j]
                    vis[i][j] = True
                vis1[i][j][1] = vis1[i][j + 1][1]
                if vis1[i][j + 1][1] < ar[i][j]:
                    vis1[i][j][1] = ar[i][j]
                    vis[i][j] = True
    ans = 0
    for i in range(n):
        for j in range(m):
            if vis[i][j]:
                # print(i, j)
                ans += 1
    print(ans)


def part_2(inp: str, debug: bool):
    ar = read(inp)
    n = len(ar)
    m = len(ar[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            cur = 1
            ii = i - 1
            while ii >= 0 and ar[ii][j] < ar[i][j]:
                ii -= 1
            cur *= i - ii - (0 if ii >= 0 else 1)

            ii = i + 1
            while ii < n and ar[ii][j] < ar[i][j]:
                ii += 1
            cur *= ii - i - (0 if ii < n else 1)

            jj = j - 1
            while jj >= 0 and ar[i][jj] < ar[i][j]:
                jj -= 1
            cur *= j - jj - (0 if jj >= 0 else 1)

            jj = j + 1
            while jj < m and ar[i][jj] < ar[i][j]:
                jj += 1
            cur *= jj - j - (0 if jj < m else 1)

            if ans < cur:
                # print(i, j, cur)
                ans = cur

    print(ans)
