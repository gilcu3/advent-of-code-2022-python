from fractions import Fraction as F


def read(inp: str):
    ar = []
    for line in inp.splitlines():
        line = line.strip().split(":")
        m0 = line[0]
        mm = line[1].strip().split()
        if len(mm) == 1:
            ar.append((m0, (int(mm[0]),)))
        else:
            ar.append((m0, (mm[0], mm[2], mm[1])))
    return ar


def part_1(inp: str, debug: bool):
    ar = read(inp)
    ar = {a: b for a, b in ar}
    dd = {}

    def rec(m):
        if len(ar[m]) == 1:
            return ar[m][0]
        if m in dd:
            return dd[m]
        ans = -1
        # print(m, ar[m][2])
        if ar[m][2] == "+":
            ans = rec(ar[m][0]) + rec(ar[m][1])
        elif ar[m][2] == "-":
            ans = rec(ar[m][0]) - rec(ar[m][1])
        elif ar[m][2] == "*":
            ans = rec(ar[m][0]) * rec(ar[m][1])
        elif ar[m][2] == "/":
            ans = rec(ar[m][0]) // rec(ar[m][1])
        dd[m] = ans
        return ans

    ans = rec("root")
    print(ans)


class num:
    def __init__(self, a0=0, a1=0):
        self.n = (F(a0), F(a1))

    def __add__(self, other):
        return num(self.n[0] + other.n[0], self.n[1] + other.n[1])

    def __sub__(self, other):
        return num(self.n[0] - other.n[0], self.n[1] - other.n[1])

    def __mul__(self, other):
        assert other.n[1] == F(0) or self.n[1] == F(0)
        if self.n[1] == F(0):
            return num(other.n[0] * self.n[0], other.n[1] * self.n[0])
        return num(self.n[0] * other.n[0], self.n[1] * other.n[0])

    def __truediv__(self, other):
        assert other.n[1] == F(0)
        return num(self.n[0] / other.n[0], self.n[1] / other.n[0])

    def __repr__(self):
        return str(self.n[0]) + " " + str(self.n[1])


def part_2(inp: str, debug: bool):
    ar = read(inp)
    ar = {a: b for a, b in ar}
    dd = {}

    def check(m):
        if m == "humn":
            return num(0, 1)
        if m == "root":
            return check(ar[m][0]), check(ar[m][1])
        if len(ar[m]) == 1:
            return num(ar[m][0], 0)
        if m in dd:
            return dd[m]
        ans = -1
        # print(m, ar[m][2])
        if ar[m][2] == "+":
            ans = check(ar[m][0]) + check(ar[m][1])
        elif ar[m][2] == "-":
            ans = check(ar[m][0]) - check(ar[m][1])
        elif ar[m][2] == "*":
            ans = check(ar[m][0]) * check(ar[m][1])
        elif ar[m][2] == "/":
            ans = check(ar[m][0]) / check(ar[m][1])
        dd[m] = ans
        return ans

    a, b = check("root")
    a, b = a.n, b.n
    x = (a[0] - b[0]) / -(a[1] - b[1])
    print(x)
