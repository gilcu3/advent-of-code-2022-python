def read(inp: str):
    ar = {}
    for line in inp.splitlines():
        words = line.strip().split()
        o = words[1]
        rate = int(words[4].strip(";").split("=")[1])
        de = [w.strip()[-2:] for w in line.split(";")[1].split(",")]
        # print(o, rate, de)
        ar[o] = (rate, de)
    return ar


top = 30
dp = {}


def rec(t, v, opened, ar):
    if t == top:
        return 0
    if (t, v, tuple(sorted(opened))) in dp:
        return dp[(t, v, tuple(sorted(opened)))]

    mx = 0
    if v not in opened and ar[v][0] > 0:
        opened.add(v)
        cur = rec(t + 1, v, opened, ar) + ar[v][0] * (top - t - 1)
        opened.remove(v)
        if cur > mx:
            mx = cur

    for nv in ar[v][1]:
        cur = rec(t + 1, nv, opened, ar)
        if cur > mx:
            mx = cur
    dp[(t, v, tuple(sorted(opened)))] = mx
    return mx


def part_1(inp: str, debug: bool):
    ar = read(inp)
    ans = rec(0, "AA", set(), ar)
    print(ans)


dp2 = {}


def rec2(t, v, opened, notopened, ar):
    if t == 2 * top:
        return 0
    if t == top:
        v = 0
        t += 4
        notopened = 0
    if dp2[t][v][opened] is not None:
        return dp2[t][v][opened]

    mx = 0
    nno = notopened
    if ar[v][0] > 0 and ((opened & (1 << v)) == 0):
        if ar[v][0] < notopened:
            pos = False
        else:
            nno = ar[v][0]
            pos = True

    for nv in ar[v][1]:
        if nv is None:
            if (((1 << v) & opened) == 0) and pos:
                cur = rec2(t + 1, v, opened + (1 << v), notopened, ar) + ar[v][0] * (
                    top - t % top - 1
                )
            else:
                cur = 0
        else:
            cur = rec2(t + 1, nv, opened, nno, ar)

        if cur > mx:
            mx = cur

    dp2[t][v][opened] = mx
    return mx


def part_2(inp: str, debug: bool):
    # global dp2,best
    global dp2
    ar = read(inp)
    dd = {}
    dd["AA"] = 0
    ids = 1
    ari = [None] * len(ar)
    # ss = 0
    for v in ar:
        if ar[v][0] > 0:
            # ss += ar[v][0]
            dd[v] = ids
            ids += 1
    tot = len(dd)
    for v in ar:
        if v not in dd:
            dd[v] = ids
            ids += 1

    for v in ar:
        ari[dd[v]] = (ar[v][0], [dd[nv] for nv in ar[v][1]])
        if ar[v][0] > 0:
            ari[dd[v]][1].append(None)

    # dp2 = [ [ [ {} for _ in range(ids)] for _ in range(ids)]  for _ in range(top)]
    # best = 0
    # ans = rec2(4, dd['AA'], dd['AA'], 0, ari, 0, ss)
    # print(ans)

    dp2 = [[[None] * (1 << tot) for _ in range(ids)] for _ in range(2 * top)]
    ans = rec2(4, 0, 0, 0, ari)
    print(ans)
