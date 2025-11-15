class Monkey:
    def __init__(self):
        self.items = []
        self.operation = None
        self.test = 1
        self.restrue = 0
        self.resfalse = 0

    def __repr__(self):
        return " ".join(
            [
                str(self.items),
                str(self.operation),
                str(self.test),
                str(self.restrue),
                str(self.resfalse),
            ]
        )


def read(inp: str):
    monkeys = []
    cur = Monkey()
    for line in inp.splitlines():
        a = line.strip().split()
        if len(a) == 0:
            monkeys.append(cur)
            cur = Monkey()
        elif a[0] == "Monkey":
            pass
        elif a[0] == "Starting":
            cur.items = [int(b.strip(",")) for b in a[2:]]
        elif a[0] == "Operation:":
            cur.operation = eval("lambda old: " + "".join(a[3:]))
        elif a[0] == "Test:":
            cur.test = int(a[3])
        elif a[0] == "If":
            if a[1] == "true:":
                cur.restrue = int(a[-1])
            elif a[1] == "false:":
                cur.resfalse = int(a[-1])
    monkeys.append(cur)
    return monkeys


def part_1(inp: str, debug: bool):
    monkeys = read(inp)
    # for m in monkeys: print(m)
    mitems = [m.items for m in monkeys]
    ins = [0 for _ in monkeys]
    # print(mitems)
    for r in range(20):
        mnitems = [[] for _ in monkeys]
        for i, m in enumerate(monkeys):
            for j, it in enumerate(mitems[i]):
                # print(i, j, it)
                it = m.operation(it)
                it //= 3
                # print(it)
                if it % m.test == 0:
                    if m.restrue < i:
                        mnitems[m.restrue].append(it)
                    else:
                        mitems[m.restrue].append(it)
                else:
                    if m.resfalse < i:
                        mnitems[m.resfalse].append(it)
                    else:
                        mitems[m.resfalse].append(it)
                ins[i] += 1
        mitems = mnitems
        # if r <= 3: print(mitems)
        # if r == 0: break

    # print(ins)
    a, b = sorted(ins)[-2:]
    ans = a * b
    print(ans)


def part_2(inp: str, debug: bool):
    monkeys = read(inp)
    # for m in monkeys: print(m)
    div = [m.test for m in monkeys]

    def conv(it):
        return [it % d for d in div]

    mitems = [[conv(it) for it in m.items] for m in monkeys]
    ins = [0 for _ in monkeys]
    # print(mitems)
    for r in range(10000):
        mnitems = [[] for _ in monkeys]
        for i, m in enumerate(monkeys):
            for j, itt in enumerate(mitems[i]):
                # print(i, j, it)
                # print(itt)
                cur = [m.operation(it) % div[k] for k, it in enumerate(itt)]
                if cur[i] % m.test == 0:
                    if m.restrue < i:
                        mnitems[m.restrue].append(cur)
                    else:
                        mitems[m.restrue].append(cur)
                else:
                    if m.resfalse < i:
                        mnitems[m.resfalse].append(cur)
                    else:
                        mitems[m.resfalse].append(cur)
                ins[i] += 1
        mitems = mnitems
        # if r <= 3: print(mitems)
        # if r == 0: break

    # print(ins)
    a, b = sorted(ins)[-2:]
    ans = a * b
    print(ans)
