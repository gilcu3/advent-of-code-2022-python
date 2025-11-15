def read(inp: str):
    g = {"/": set()}
    ss = {}
    cw = None
    for line in inp.splitlines():
        coms = line.strip().split()
        if coms[0] == "$":
            if coms[1] == "cd":
                d = coms[2]
                if cw is None:
                    assert d == "/"
                    cw = "/"
                elif d == "..":
                    cw = "/".join(cw.split("/")[:-2]) + "/"
                else:
                    if d in g[cw]:
                        cw = cw + d + "/"
                    else:
                        g[cw].add(d)
                        cw = cw + d + "/"
                        g[cw] = set()
            elif coms[1] == "ls":
                pass
        elif coms[0] == "dir":
            pass
        else:
            s = int(coms[0])
            fn = coms[1]
            ss[cw + fn] = s
    return g, ss


def part_1(inp: str, debug: bool):
    g, ss = read(inp)

    def parent(f):
        if f[-1] == "/":
            return "/".join(f.split("/")[:-2]) + "/"
        else:
            return "/".join(f.split("/")[:-1]) + "/"

    ds = {}
    for d in g.keys():
        ds[d] = 0
    for fn in ss:
        ds[parent(fn)] += ss[fn]
    for d in reversed(sorted(g.keys())):
        ds[parent(d)] += ds[d]
    ans = 0
    for d, s in ds.items():
        if s <= 10**5:
            ans += s
    print(ans)


def part_2(inp: str, debug: bool):
    g, ss = read(inp)

    def parent(f):
        if f[-1] == "/":
            return "/".join(f.split("/")[:-2]) + "/"
        else:
            return "/".join(f.split("/")[:-1]) + "/"

    ds = {}
    for d in g.keys():
        ds[d] = 0
    for fn in ss:
        ds[parent(fn)] += ss[fn]
    for d in reversed(sorted(g.keys())):
        if d != "/":
            ds[parent(d)] += ds[d]
    tot = 70000000
    need = 30000000
    used = ds["/"]
    ans = tot
    for d, s in ds.items():
        # print(tot, used, need, s)
        if tot - (used - s) >= need and ans > s:
            ans = s
    print(ans)
