#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

inp = parsegrid(lines())

rs, cs = inp.size()

bigrows, bigcols = set(), set()

for r in range(rs):
    if not any(inp.at(P(r, c)) == '#' for c in range(cs)):
        bigrows.add(r)

for c in range(cs):
    if not any(inp.at(P(r, c)) == '#' for r in range(rs)):
        bigcols.add(c)

# cd[i] = dist from 0 to i exclusive
cd, rd = [0], [0]
for r in range(1, rs+1):
    rd.append(rd[r-1] + (2 if r-1 in bigrows else 1))
for c in range(1, cs+1):
    cd.append(cd[c-1] + (2 if c-1 in bigcols else 1))

print(cd)
print(rd)

gs = set()
for pt, t in inp.itertiles():
    if t == "#":
        gs.add(pt)

print(gs)

td = 0
for a in sorted(gs):
    for b in sorted(gs):
        if a == b:
            continue
        d = abs(a[0]-b[0]) + abs(a[1]-b[1])

        lb, ub = bounds([a, b])
        for r in range(lb[0], ub[0]):
            if r in bigrows:
                d += 1
        for c in range(lb[1], ub[1]):
            if c in bigcols:
                d += 1
        td += d

print(td/2)
