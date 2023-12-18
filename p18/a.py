#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

inp = lines(
    pre(r"(.) (\d+) \(#(.*)\)"),
    ptuple(
        str,
        int,
        lambda x: int('0x' + x, 16),
    )
)

dirs = {"R":east,"L":west,"U":north,"D":south}

pt = P(0,0)
g = infgrid()
g2 = infgrid()
for ds, dist, color in inp:
    d = dirs[ds]
    dv = d.gvec()
    for i in range(dist):
        pt += dv
        g.set(pt, '|' if d == north or d == south else '-')
        g2.set(pt, str(color))

lb, ub = g.bounds()
lb += P(-1, -1)
ub += P(1, 1)

next = [lb]
outside = 0
while len(next) > 0:
    pt = next.pop()
    if g.at(pt) != '.':
        continue
    g.set(pt, "X")
    outside += 1
    for pt2 in pt.nbr4():
        if lb[0] <= pt2[0] < ub[0] and lb[1] <= pt2[1] < ub[1]:
            next.append(pt2)

box = (ub[0] - lb[0]) * (ub[1] - lb[1])
print(outside, box, box-outside)
print( box-outside)
