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

dirs = {0:east,1:south,2:west,3:north}

pt = P(0,0)
lines = []
for _, _, color in inp:
    d = dirs[color % 16]
    dist = color // 16
    pt1, pt2 = pt, pt + d.gvec(dist)
    pt = pt2

    if pt1[0] > pt2[0]:
        pt1, pt2 = pt2, pt1
    if pt1[1] > pt2[1]:
        pt1, pt2 = pt2, pt1

    lines.append((pt1, pt2))

lines = list(sorted(lines))


volume = 1
cross = []
r = None
for l in lines:
    a, b = l
    if a[1] == b[1]:  # vert line
        continue
    r2 = a[0]
    if r is None:
        r = r2
    elif r2 != r:
        volume += sum(v[1] - v[0] + 1 for v in cross) * (r2 - r)
        r = r2

    iv = intv(a[1], b[1])

    print(r, iv)

    found = False
    for i, jv in enumerate(cross):
        if iv.intersects(jv):
            found = True
            cross.pop(i)
            cross.extend(nv for nv in jv.sub(iv) if not nv.degen())
            cross.sort()

    if not found:
        volume += iv[1] - iv[0]

        cross.append(iv)
        cross.sort()

        cross2 = []
        x = cross[0]
        for y in cross[1:]:
            x, y = x.union(y)
            if not y.degen():
                cross2.append(x)
                x = y
        if not x.degen():
            cross2.append(x)

        cross = cross2

    print("CROSS", cross)

print(volume)
