pieces = """
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""


def read(inp: str):
    ar = [(True if c == ">" else False) for c in inp.strip()]
    pp = []
    for p in pieces.strip().split("\n\n"):
        a = p.split("\n")
        b = []
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[len(a) - i - 1][j] == "#":
                    b.append((i, j))
        pp.append(b)

    return ar, pp


def part_1(inp: str, debug: bool):
    ar, pp = read(inp)
    high = 0
    t = 0
    space = [[False] * 9]
    for i in range(2022):
        s = (high + 4, 3)
        cp = [(s[0] + c[0], s[1] + c[1]) for c in pp[i % len(pp)]]
        for c in cp:
            assert not (c[1] > 7 or c[1] <= 0 or c[0] <= 0)
        while True:
            #  gas
            d = (0, 1) if ar[t % len(ar)] else (0, -1)
            t += 1
            pos = True
            for c in cp:
                nc = (c[0] + d[0], c[1] + d[1])
                if nc[1] > 7 or nc[1] <= 0 or nc[0] <= 0:
                    pos = False
                    break
                if nc[0] < len(space) and space[nc[0]][nc[1]]:
                    pos = False
                    break
            if pos:
                cp = [(c[0] + d[0], c[1] + d[1]) for c in cp]
            d = (-1, 0)
            pos = True
            for c in cp:
                nc = (c[0] + d[0], c[1] + d[1])
                if nc[1] > 7 or nc[1] <= 0 or nc[0] <= 0:
                    pos = False
                    break
                if nc[0] < len(space) and space[nc[0]][nc[1]]:
                    pos = False
                    break
            if pos:
                cp = [(c[0] + d[0], c[1] + d[1]) for c in cp]
            else:
                chigh = max([c[0] for c in cp])
                if chigh > high:
                    for _ in range(chigh - high):
                        space.append([False] * 9)
                    high = chigh
                for c in cp:
                    space[c[0]][c[1]] = True
                break
    print(high)


def part_2(inp: str, debug: bool):
    ar, pp = read(inp)
    top = 10**12
    high = 0
    t = 0
    space = [[False] * 9]
    i = 0
    dep = 5
    dp = [[{} for _ in range(len(ar))] for _ in range(len(pp))]

    def hs(a):
        mask = 0
        for i in range(dep):
            for j in range(1, 7 + 1):
                if a[i][j]:
                    mask += 1 << (i * 7 + (j - 1))
        return mask

    extra = 0
    fin = False
    while i < top:
        if fin is False and len(space) > dep:
            mask = hs(space[-dep:])
            if mask in dp[i % len(pp)][t % len(ar)]:
                pi, phigh = dp[i % len(pp)][t % len(ar)][mask]
                high - phigh
                extra = (top - i) // (i - pi) * (high - phigh)
                i += (top - i) // (i - pi) * (i - pi)
                fin = True
                continue
            else:
                dp[i % len(pp)][t % len(ar)][mask] = (i, high)
        s = (high + 4, 3)
        cp = [(s[0] + c[0], s[1] + c[1]) for c in pp[i % len(pp)]]
        while True:
            #  gas
            d = (0, 1) if ar[t % len(ar)] else (0, -1)
            t += 1
            pos = True
            for c in cp:
                nc = (c[0] + d[0], c[1] + d[1])
                if nc[1] > 7 or nc[1] <= 0 or nc[0] <= 0:
                    pos = False
                    break
                if nc[0] < len(space) and space[nc[0]][nc[1]]:
                    pos = False
                    break
            if pos:
                cp = [(c[0] + d[0], c[1] + d[1]) for c in cp]
            d = (-1, 0)
            pos = True
            for c in cp:
                nc = (c[0] + d[0], c[1] + d[1])
                if nc[1] > 7 or nc[1] <= 0 or nc[0] <= 0:
                    pos = False
                    break
                if nc[0] < len(space) and space[nc[0]][nc[1]]:
                    pos = False
                    break
            if pos:
                cp = [(c[0] + d[0], c[1] + d[1]) for c in cp]
            else:
                chigh = max([c[0] for c in cp])
                if chigh > high:
                    for _ in range(chigh - high):
                        space.append([False] * 9)
                    high = chigh
                for c in cp:
                    space[c[0]][c[1]] = True
                break
        i += 1
    print(high + extra)
