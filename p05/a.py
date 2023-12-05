#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
import re

inp = linegroups()

print(inp[0])
seeds = list(map(int, inp[0][0].split(" ")[1:]))

print(seeds)

layers = []

for m in inp[1:]:
    layer = []
    for m2 in m[1:]:
        a, b, l = map(int, m2.split(" "))
        layer.append((a, b, l))
    layers.append(layer)

minLoc = None

for seed in seeds:
    id = seed
    print("input", id)
    for layer in layers:
        nextId = id
        for intv in layer:
            if intv[1] <= id <= intv[1] + intv[2]:
                nextId = id + intv[0] - intv[1]
                break
        print(id, "->", nextId)
        id = nextId
    if minLoc == None or minLoc > id:
        minLoc = id

print(minLoc)
