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
    # retain possibilities with an open end iff there's a matching open end
    poss = set(t2 for t2 in poss if (d in ends[t2]) == (d.turn(2) in ends[t]))

print(poss)

inp.set(s, poss.pop())

dist = inp.flood(s, 0, lambda pt, t, v, vals: [(pt + d.gvec(), v+1) for d in ends[t]])

print(max(dist.values()))
