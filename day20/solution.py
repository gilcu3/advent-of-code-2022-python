def read(inp: str):
    ar = []
    for line in inp.splitlines():
        ar.append(int(line.strip()))
    return ar


def part_1(inp: str, debug: bool):
    ar = read(inp)
    ar = [(i, v) for i, v in enumerate(ar)]
    n = len(ar)
    # print(ar)
    for i in range(n):
        w, v = -1, -1
        for j, (a, b) in enumerate(ar):
            if a == i:
                w = j
                v = b
                break
        if abs(v) > 0:
            s = v // abs(v)
            ii = w

            for _ in range(abs(v)):
                ar[ii], ar[(ii + s) % n] = ar[(ii + s) % n], ar[ii]
                ii = (ii + s) % n
        # print(ar)
    v = -1
    for j, (a, b) in enumerate(ar):
        if b == 0:
            v = j
    ans = 0
    for i in range(4):
        ans += ar[(v + i * 1000) % n][1]
    print(ans)


def part_2(inp: str, debug: bool):
    ar = read(inp)
    key = 811589153
    ar = [(i, v * key) for i, v in enumerate(ar)]
    n = len(ar)
    # print(ar)
    for _ in range(10):
        for i in range(n):
            w, v = -1, -1
            for j, (a, b) in enumerate(ar):
                if a == i:
                    w = j
                    v = b
                    break
            if abs(v) > 0:
                s = v // abs(v)
                ii = w

                for _ in range(abs(v) % (n - 1)):
                    ar[ii], ar[(ii + s) % n] = ar[(ii + s) % n], ar[ii]
                    ii = (ii + s) % n
        # print(ar)
    v = -1
    for j, (a, b) in enumerate(ar):
        if b == 0:
            v = j
    ans = 0
    for i in range(4):
        ans += ar[(v + i * 1000) % n][1]
    print(ans)
