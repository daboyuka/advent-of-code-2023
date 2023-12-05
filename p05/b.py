#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
import re

inp = linegroups()

seeds = pchain(pre1("seeds: (.*)"), pdelim(" ", int))(inp[0][0])

layers = tmap(
    pchain(
        lambda lg: lg[1:],
        pmap(
            pdelim(" ", int),
            lambda e: (intv(e[1], e[1]+e[2]), e[0] - e[1]),
        ),
    ),
    inp[1:])

mapped = list(map(
    lambda e: intv(e[0], e[0] + e[1]),
    part(seeds, 2),
))

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

print(min(map(lambda i: i[0], mapped)))
