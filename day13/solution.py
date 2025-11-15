from functools import cmp_to_key


def read(inp: str):
    ar = []
    for line in inp.splitlines():
        line = line.strip()
        if len(line) > 0:
            ar.append(eval(line))
    return ar


def deepcompare(a, b):
    if a.__class__ == b.__class__:
        if isinstance(a, int):
            return -1 if a < b else (1 if a > b else 0)
        else:
            for i in range(len(a)):
                if i >= len(b):
                    return 1
                else:
                    cur = deepcompare(a[i], b[i])
                    if cur != 0:
                        return cur
            if len(b) > len(a):
                return -1
            else:
                return 0
    else:
        if isinstance(a, int):
            return deepcompare(
                [
                    a,
                ],
                b,
            )
        else:
            return deepcompare(
                a,
                [
                    b,
                ],
            )


def part_1(inp: str, debug: bool):
    ar = read(inp)
    ans = 0
    for i in range(0, len(ar), 2):
        if deepcompare(ar[i], ar[i + 1]) == -1:
            ans += i // 2 + 1
    print(ans)


def part_2(inp: str, debug: bool):
    ar = read(inp)
    ans = 1
    p1, p2 = [[2]], [[6]]
    ar += [p1, p2]
    ar.sort(key=cmp_to_key(deepcompare))
    for i, a in enumerate(ar):
        # print(a)
        if a == [
            [
                2,
            ],
        ] or a == [
            [
                6,
            ],
        ]:
            ans *= i + 1
    print(ans)
