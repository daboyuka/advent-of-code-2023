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

dist = {s: 0}
visit = deque([s])
while len(visit) > 0:
    n = visit.popleft()
    di = dist[n]
    t = inp.at(n)
    print(n, d, t)
    for d in ends[t]:
        n2 = n + d.gvec()
        if n2 not in dist:
            dist[n2] = di+1
            visit.append(n2)


print(inp.render())

for p, d in dist.items():
    inp.set(p, str(d))

print(dist)
print(inp.render())
print(max(dist.values()))
