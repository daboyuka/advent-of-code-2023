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

seen = inp.flood(s, True, lambda pt, t, v, vals: [(pt + d.gvec(), True) for d in ends[t]])

cont = 0
crossed = bdict()
for pt, t in inp.itertiles():
    if pt in seen.keys():
        for d in ends[t]:
            crossed[d] = not crossed[d]
    elif crossed[north] and crossed[south]:
        cont += 1
        inp.set(pt, 'I')

print(inp.render())
print(cont)
