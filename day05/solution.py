def read(inp: str):
    lines = []
    lines2 = []
    s2 = False
    for line in inp.splitlines():
        if len(line.strip()) == 0:
            s2 = True
            continue
        if not s2:
            lines.append(line.rstrip())
        else:
            lines2.append(line.rstrip())

    n = len(lines[-1].split())
    mat = [[] for _ in range(n)]
    for i, ll in enumerate(lines[-2 : -len(lines) - 1 : -1]):
        for j in range(0, 4 * n, 4):
            c = ll[j : j + 3].strip()
            if len(c) > 0:
                mat[j // 4].append(c[1])
    coms = []
    for line in lines2:
        _, n, _, a, _, b = line.strip().split()
        coms.append((int(a) - 1, int(b) - 1, int(n)))
    return mat, coms


def part_1(inp: str, debug: bool):
    mat, coms = read(inp)
    for a, b, n in coms:
        mat[b] += mat[a][-n:][::-1]
        mat[a] = mat[a][:-n]
    ans = "".join(m[-1] for m in mat)
    print(ans)


def part_2(inp: str, debug: bool):
    mat, coms = read(inp)
    for a, b, n in coms:
        mat[b] += mat[a][-n:]
        mat[a] = mat[a][:-n]
    ans = "".join(m[-1] for m in mat)
    print(ans)
