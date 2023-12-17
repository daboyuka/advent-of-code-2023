#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

g = parsegrid(lines())


next = [(0, P(0,0), east), (0, P(0,0), south)]

v = dict()  # (pt, d) -> dist

while len(next) > 0:
    dist, pt, d = heapq.heappop(next)
    if (pt, d) in v:
        continue

    v[(pt, d)] = dist

    for d2 in [d.turn(1), d.turn(3)]:
        dist2 = dist
        pt2 = pt
        for l in range(10):
            pt2 += d2.gvec()
            if not g.inbounds(pt2):
                break
            dist2 += int(g.at(pt2))
            if l >= 3:
                heapq.heappush(next, (dist2, pt2, d2))

rs, cs = g.size()

print(min(dist for (pt, d), dist in v.items() if pt == P(rs-1,cs-1)))
