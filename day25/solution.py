def read(inp: str):
    ar = []
    for line in inp.splitlines():
        ar.append(line.rstrip("\n"))
    return ar


def snafu2dec(a):
    b = 0
    order = ["=", "-", "0", "1", "2"]
    for i in a:
        for j in range(5):
            if i == order[j]:
                i = j - 2
                break
        b = 5 * b + i
    return b


def dec2snafu(a):
    order = ["0", "1", "2", "=", "-"]
    b = ""
    while a > 0:
        b = order[a % 5] + b
        if a % 5 >= 3:
            a -= a % 5 - 5
        else:
            a -= a % 5
        a //= 5
    return b


def part_1(inp: str, debug: bool):
    ar = read(inp)
    ans = 0
    for i in ar:
        ans += snafu2dec(i)
    print(dec2snafu(ans))


def part_2(inp: str, debug: bool):
    pass
