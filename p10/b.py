#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

inp = parsegrid(lines())

ends = {
    "|": {north, south},
    "-": {east, west},
    "L": {north, east},
    "J": {north, west},
    "7": {south, west},
    "F": {south, east},
    ".": {}
}

s = [pt for (pt, t) in inp.itertiles() if t == "S"][0]

print(s)

poss = {"|", "-", "L", "J", "7", "F"}
for d in [north, south, east, west]:
    t = inp.at(s + d.gvec(), '.')
    if d.turn(2) in ends[t]: # connected on that side
        poss = set(t for t in poss if d in ends[t])
    else:
        poss = set(t for t in poss if d not in ends[t])

print(poss)

inp.set(s, poss.pop())

seen = set()
visit = deque([s])
while len(visit) > 0:
    n = visit.popleft()
    t = inp.at(n)
    for d in ends[t]:
        n2 = n + d.gvec()
        if n2 not in seen:
            seen.add(n2)
            visit.append(n2)

for pt, t in inp.itertiles():
    if pt not in seen:
        inp.set(pt, '.')

print(inp.render())
print()

cont = 0
rs, cs = inp.size()
for r in range(rs):
    ins = False
    cross = None
    for c in range(cs):
        pt = P(r, c)
        t = inp.at(pt, '.')

        if pt in seen:
            for d in ends[t]:
                if d == north or d == south:
                    if cross is None:
                        cross = d
                    else:
                        if cross != d:
                            ins = not ins
                        cross = None
        elif ins:
            cont += 1
            inp.set(pt, 'I')

print(inp.render())
print(cont)
