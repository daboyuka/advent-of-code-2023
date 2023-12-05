#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
import re

inp = linegroups()

print(inp[0])
seeds = list(map(int, inp[0][0].split(" ")[1:]))

layers = []

for m in inp[1:]:
    layer = []
    for m2 in m[1:]:
        a, b, l = map(int, m2.split(" "))
        layer.append((intv(b, b+l), a - b))
    layers.append(layer)

mapped = []
for i in range(0, len(seeds), 2):
    mapped.append(intv(seeds[i], seeds[i] + seeds[i+1]))

print(mapped)

for layer in layers:
    toMaps = mapped
    mapped = []
    for intv, offset in layer:
        toMapsNew = []
        for toMap in toMaps:
            if intv.intersects(toMap):
                inMap = intv.intersect(toMap)
                outMap = inMap.shift(offset)
                print(inMap, "->", outMap, "by", intv, offset)
                mapped.append(outMap)
                new1, new2 = toMap.sub(intv)
                if not new1.degen():
                    toMapsNew.append(new1)
                if not new2.degen():
                    toMapsNew.append(new2)
            else:
                toMapsNew.append(toMap)
        toMaps = toMapsNew
    mapped.extend(toMaps)
    print(mapped)

print(min(map(lambda i: i[0], mapped)))
