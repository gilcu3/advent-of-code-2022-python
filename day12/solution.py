def read(inp: str):
    mat = []
    s, e = (-1, -1), (-1, -1)
    for i, line in enumerate(inp.splitlines()):
        cur = []
        for j, c in enumerate(line.strip()):
            if c == "S":
                s = (i, j)
                cur.append(ord("a") - ord("a"))
            elif c == "E":
                e = (i, j)
                cur.append(ord("z") - ord("a"))
            else:
                cur.append(ord(c) - ord("a"))
        mat.append(cur)
    return mat, s, e


moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(b, fe, mat, fmat):
    n, m = len(mat), len(mat[0])
    dis = [[None] * m for _ in range(n)]
    que = []
    que.append(b)
    dis[b[0]][b[1]] = 0
    front = 0
    ans = -1
    while front < len(que):
        cx, cy = que[front]
        front += 1
        if fe((cx, cy)):
            ans = dis[cx][cy]
            break
        for dx, dy in moves:
            nx, ny = cx + dx, cy + dy
            if (
                nx >= 0
                and nx < n
                and ny >= 0
                and ny < m
                and dis[nx][ny] is None
                and fmat((cx, cy), (nx, ny))
            ):
                dis[nx][ny] = dis[cx][cy] + 1
                que.append((nx, ny))

    return ans


def part_1(inp: str, debug: bool):
    mat, b, e = read(inp)
    # for l in mat: print(l)
    # print(b, e)
    ans = bfs(
        b,
        lambda x: e[0] == x[0] and e[1] == x[1],
        mat,
        lambda cxy, nxy: mat[nxy[0]][nxy[1]] <= mat[cxy[0]][cxy[1]] + 1,
    )
    print(ans)


def part_2(inp: str, debug: bool):
    mat, _, e = read(inp)
    # for l in mat: print(l)
    # print(b, e)
    ans = bfs(
        e,
        lambda x: mat[x[0]][x[1]] == 0,
        mat,
        lambda cxy, nxy: mat[cxy[0]][cxy[1]] <= mat[nxy[0]][nxy[1]] + 1,
    )
    print(ans)
