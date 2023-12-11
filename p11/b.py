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
for r, row in inp.iterrows():
    if not any(t == '#' for t in row):
        bigrows.add(r)
for c, col in inp.itercols():
    if not any(t == '#' for t in col):
        bigcols.add(c)

# cd[i] = dist from 0 to i exclusive
cd, rd = [0], [0]
for r in range(1, rs+1):
    rd.append(rd[r-1] + (1000000 if r-1 in bigrows else 1))
for c in range(1, cs+1):
    cd.append(cd[c-1] + (1000000 if c-1 in bigcols else 1))

print(cd)
print(rd)

gs = set(inp.find("#"))
print(gs)

td = 0
for a, b in itertools.combinations(gs, 2):
    d = abs(rd[a[0]]-rd[b[0]]) + abs(cd[a[1]]-cd[b[1]])
    td += d

print(td)
