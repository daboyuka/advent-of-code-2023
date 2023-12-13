#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

inp = linegroups()
inp = tmap(parsegrid, inp)

total = 0
for g in inp:
    rdim, cdim = g.size()

    rows, cols = [], []
    rposs, cposs = [], []
    rprev, cprev = None, None
    for r, row in g.iterrows():
        row = tuple(row)
        rows.append(row)
        if rprev == row:
            rposs.append(r)
        rprev = row
    for c, col in g.itercols():
        col = tuple(col)
        cols.append(col)
        if cprev == col:
            cposs.append(c)
        cprev = col

    print(rposs, cposs)

    for r in rposs:
        if all(rows[r-i-1] == rows[r+i] for i in range(1,min(r,rdim-r))):
            total += 100*r
    for c in cposs:
        if all(cols[c-i-1] == cols[c+i] for i in range(1,min(c,cdim-c))):
            total += c

print(total)
