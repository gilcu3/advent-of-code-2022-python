def read(inp: str):
    ar = []
    for line in inp.splitlines():
        a, b = line.strip().split()
        ar.append((a, int(b)))
    return ar


def part_1(inp: str, debug: bool):
    ar = read(inp)
    hx, hy = 0, 0
    tx, ty = 0, 0
    vis = set()
    vis.add((tx, ty))
    for a, b in ar:
        for _ in range(b):
            if a == "U":
                hy += 1
                if hy > ty + 1:
                    ty += 1
                    tx += 1 if hx > tx else (-1 if hx < tx else 0)
            elif a == "D":
                hy -= 1
                if hy < ty - 1:
                    ty -= 1
                    tx += 1 if hx > tx else (-1 if hx < tx else 0)
            elif a == "R":
                hx += 1
                if hx > tx + 1:
                    tx += 1
                    ty += 1 if hy > ty else (-1 if hy < ty else 0)
            elif a == "L":
                hx -= 1
                if hx < tx - 1:
                    tx -= 1
                    ty += 1 if hy > ty else (-1 if hy < ty else 0)
            vis.add((tx, ty))
    print(len(vis))


def part_2(inp: str, debug: bool):
    n = 10
    rope = [(0, 0) for _ in range(n)]
    ar = read(inp)

    def upd_head(a, h):
        (hx, hy) = h
        if a == "U":
            hy += 1
        elif a == "D":
            hy -= 1
        elif a == "R":
            hx += 1
        elif a == "L":
            hx -= 1
        return (hx, hy)

    def upd(t, h):
        tx, ty = t
        hx, hy = h
        if hy > ty + 1:
            ty += 1
            tx += 1 if hx > tx else (-1 if hx < tx else 0)
        elif hy < ty - 1:
            ty -= 1
            tx += 1 if hx > tx else (-1 if hx < tx else 0)
        elif hx > tx + 1:
            tx += 1
            ty += 1 if hy > ty else (-1 if hy < ty else 0)
        elif hx < tx - 1:
            tx -= 1
            ty += 1 if hy > ty else (-1 if hy < ty else 0)
        return (tx, ty)

    vis = set()
    vis.add(rope[-1])
    for a, b in ar:
        for _ in range(b):
            rope[0] = upd_head(a, rope[0])
            for i in range(1, n):
                rope[i] = upd(rope[i], rope[i - 1])
            vis.add(rope[-1])
    print(len(vis))
