#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

inp = linegroups()
inp = tmap(parsegrid, inp)

def diff(a, b):
    d = 0
    for x, y in zip(a, b):
        if x != y:
            d += 1
    return d

# def findreflect(g, rows, cols, rposs, cposs, thresh):
#     rdim, cdim = g.size()
#
#     origr, origc = None, None
#     for r in rposs:
#         if sum(diff(rows[r-i-1], rows[r+i]) for i in range(0,min(r,rdim-r))) == thresh:
#             origr = r
#             break
#     for c in cposs:
#         if sum(diff(cols[c-i-1], cols[c+i]) for i in range(0,min(c,cdim-c))) == thresh:
#             origc = c
#             break


total = 0
for g in inp:
    rdim, cdim = g.size()

    rows, cols = [], []
    rposs, cposs = [], []
    rprev, cprev = None, None
    for r, row in g.iterrows():
        row = tuple(row)
        rows.append(row)
        if rprev is not None and diff(rprev, row) <= 1:
            rposs.append(r)
        rprev = row
    for c, col in g.itercols():
        col = tuple(col)
        cols.append(col)
        if cprev is not None and diff(cprev, col) <= 1:
            cposs.append(c)
        cprev = col

    origr, origc = None, None
    for r in rposs:
        if all(rows[r-i-1] == rows[r+i] for i in range(0,min(r,rdim-r))):
            origr = r
            break
    for c in cposs:
        if all(cols[c-i-1] == cols[c+i] for i in range(0,min(c,cdim-c))):
            origc = c
            break

    print("orig", origr, origc)
    for r in rposs:
        if r != origr and sum(diff(rows[r-i-1], rows[r+i]) for i in range(0, min(r, rdim-r))) == 1:
            print("row", r, origr)
            total += 100*r
    for c in cposs:
        print(c)
        if c != origc and sum(diff(cols[c-i-1], cols[c+i]) for i in range(0, min(c, cdim-c))) == 1:
            print("col", c, origc)
            total += c

print(total)
