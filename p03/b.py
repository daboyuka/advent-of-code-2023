#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
import re

inp = lines()

g = parsegrid(inp)

rows, cols = g.size()

def scannum(pt):
    numStr = ""
    for i in range(cols):
        t = g.at(pt + P(0, i), '.')
        if t < "0" or t > "9":
            break
        numStr += t
    return int(numStr), len(numStr)

def scanborder(pt, l):
    out = []
    def check(pt, out):
        t = g.at(pt, '.')
        if t == "*":
            out.append(pt)

    for i in range(l+2):
        check(pt + P(-1, i-1), out)
        check(pt + P(1, i-1), out)
    check(pt + P(0, -1), out)
    check(pt + P(0, l), out)
    return out


gearAdjs = collections.defaultdict(lambda: [])

for row in range(rows):
    col = 0
    while col < cols:
        pt = P(row, col)
        t = g.at(pt)
        if t >= "0" and t <= "9":
            n, skip = scannum(pt)

            for gearPt in scanborder(pt, skip):
                gearAdjs[gearPt].append(n)

            col += skip
        else:
            col += 1

ans = 0
for gearPt, adjs in gearAdjs.items():
    if len(adjs) == 2:
       ans += adjs[0] * adjs[1]

print(ans)
