#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

def deb(v):
    return v

rules, inp = linegroups(
    pchain(
        pre(r"(\w+)\{([^}]+)\}"),
        ptuple(
            str,
            pdelim(",", deb, pre(r"(?:(.)(.)(\d+):)?(\w+)")),
        ),
    ),
    pchain(
        pre1(r"\{(.*)\}"),
        pdelim(",",
               pre(r"(.)=(\d+)"),
               ptuple(str, int)),
    ),
)

flows = dict()
for n, steps in rules:
    flows[n] = steps

def intersect(bb, idx, a, b):
    up = (max(a, bb[idx][0]), min(b, bb[idx][1]))
    if up[0] >= up[1]:
        return None
    return bb[:idx] + (up,) + bb[idx+1:]

idxs = {"x":0,"m":1,"a":2,"s":3}

# bbs = [ ((a0, b0), (a1, b1), ...) ]
def combos(steps, bbs):
    out = ldict()
    rem = bbs
    for cond, cmp, thresh, to in steps:
        if cond is None:
            out[to].extend(rem)
            continue

        thresh = int(thresh)
        idx = idxs[cond]

        rem2 = []
        def apply(bb):
            if cmp == "<":
                out[to].append(intersect(bb, idx, 1, thresh))
                rem2.append(intersect(bb, idx, thresh, 4001))
            elif cmp == ">":
                out[to].append(intersect(bb, idx, thresh+1, 4001))
                rem2.append(intersect(bb, idx, 1, thresh+1))
            elif cmp == "=":
                out[to].append(intersect(bb, idx, thresh, thresh+1))
                rem2.append(intersect(bb, idx, 1, thresh))
                rem2.append(intersect(bb, idx, thresh+1, 4001))

        for bb in rem:
            apply(bb)
        rem = rem2

    print(bbs, "->", list(out.items()))
    return out

start = [
    ((1, 4001), (1, 4001), (1, 4001), (1, 4001))
]

accept = []
todo = [("in", start)]
while len(todo) > 0:
    at, bbs = todo.pop()
    print(at, bbs)
    if at == "A":
        accept.extend(bbs)
    elif at == "R":
        continue
    else:
        out = combos(flows[at], bbs)
        todo.extend(out.items())

def interbb(a, b):
    c = a
    for idx in range(4):
        c = intersect(c, idx, *b[idx])
        if c is None:
            return None
    return c

# a - b
def diffbb(a, b):
    x = interbb(a, b)
    if x is None:
        return [a]

    def tripart(bb, idx):
        for lb, ub in [(1, x[idx][0]), (x[idx][0], x[idx][1]), (x[idx][1], 4001)]:
            yield intersect(bb, idx, lb, ub)

    print(a, "//", b)
    out = []
    for idx in range(4):
        al, a, ar = tripart(a, idx)
        _, b, _ = tripart(b, idx)
        out.append(al)
        out.append(ar)

    return [bb for bb in out if bb is not None]

final = []
for bb in accept:
    toadd = [bb]
    for existing in final:
        toadd2 = []
        for part in toadd:
            toadd2.extend(newpart for newpart in diffbb(part, existing) if newpart is not None)
        toadd = toadd2
        if len(toadd) == 0:
            break
    final.extend(toadd)

size = 0
for bb in final:
    size += prod(b - a for a, b in bb)
print(size)
