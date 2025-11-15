def read(inp: str):
    ar = []
    for line in inp.splitlines():
        ar.append([c == "#" for c in line.rstrip("\n")])
    return ar


def part_1(inp: str, debug: bool):
    ar = read(inp)
    n = len(ar)
    m = len(ar[0])
    mm = set()
    for i in range(n):
        for j in range(m):
            if ar[i][j]:
                mm.add((i, j))
    dd = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dd2 = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (-1, -1), (1, -1)]
    dd3 = []
    for d in dd:
        dd3.append(
            [
                (d[0] + (1 - abs(d[0])), d[1] + (1 - abs(d[1]))),
                d,
                (d[0] - (1 - abs(d[0])), d[1] - (1 - abs(d[1]))),
            ]
        )

    # print(dd3)
    def test_move_around(a):
        for d in dd2:
            if (a[0] + d[0], a[1] + d[1]) in mm:
                return True
        return False

    def try_move(a, i):
        for d in dd3[i]:
            if (a[0] + d[0], a[1] + d[1]) in mm:
                return False
        return True

    ii = 0
    for _ in range(10):
        move = {}
        cc = {}
        # print([e for e in mm if test_move_around(e)])
        for e in mm:
            if test_move_around(e):
                for i in range(ii, ii + 4):
                    pos = try_move(e, i % 4)
                    if pos:
                        ne = (e[0] + dd[i % 4][0], e[1] + dd[i % 4][1])
                        move[e] = ne
                        if ne in cc:
                            cc[ne] += 1
                        else:
                            cc[ne] = 1
                        break
        # print(move, cc)
        for e, ne in move.items():
            if cc[ne] == 1:
                mm.remove(e)
                mm.add(ne)
        # for i in range(n):
        #     print(''.join('#' if (i, j) in mm else '.' for j in range(m)))
        # print('')
        ii += 1

    oo = 10**16
    mnx, mny, mxx, mxy = oo, oo, -oo, -oo
    for i, j in mm:
        mnx = min(mnx, i)
        mny = min(mny, j)
        mxx = max(mxx, i)
        mxy = max(mxy, j)
    # print(mnx, mny, mxx, mxy)
    ans = (mxy - mny + 1) * (mxx - mnx + 1) - len(mm)
    print(ans)


def part_2(inp: str, debug: bool):
    ar = read(inp)
    n = len(ar)
    m = len(ar[0])
    mm = set()
    for i in range(n):
        for j in range(m):
            if ar[i][j]:
                mm.add((i, j))
    dd = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dd2 = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (-1, -1), (1, -1)]
    dd3 = []
    for d in dd:
        dd3.append(
            [
                (d[0] + (1 - abs(d[0])), d[1] + (1 - abs(d[1]))),
                d,
                (d[0] - (1 - abs(d[0])), d[1] - (1 - abs(d[1]))),
            ]
        )

    # print(dd3)
    def test_move_around(a):
        for d in dd2:
            if (a[0] + d[0], a[1] + d[1]) in mm:
                return True
        return False

    def try_move(a, i):
        for d in dd3[i]:
            if (a[0] + d[0], a[1] + d[1]) in mm:
                return False
        return True

    ii = 0
    while True:
        move = {}
        cc = {}
        # print([e for e in mm if test_move_around(e)])
        for e in mm:
            if test_move_around(e):
                for i in range(ii, ii + 4):
                    pos = try_move(e, i % 4)
                    if pos:
                        ne = (e[0] + dd[i % 4][0], e[1] + dd[i % 4][1])
                        move[e] = ne
                        if ne in cc:
                            cc[ne] += 1
                        else:
                            cc[ne] = 1
                        break
        # print(move, cc)
        done = True
        for e, ne in move.items():
            if cc[ne] == 1:
                done = False
                mm.remove(e)
                mm.add(ne)
        # for i in range(n):
        #     print(''.join('#' if (i, j) in mm else '.' for j in range(m)))
        # print('')
        ii += 1
        if done:
            break
    print(ii)
