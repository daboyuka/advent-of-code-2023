#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

inp = lines(pdelim(","))[0]
print(inp)

def hash(x):
    v = 0
    for c in x:
        v += ord(c)
        v *= 17
        v %= 256
    return v

m = ldict() # (hash) -> [(label, focal)]
for v in inp:
    if "-" in v:
        l = v.split("-")[0]
        b = hash(l)
        m[b] = [(l2, n) for l2, n in m[b] if l2 != l]
    else:
        l, n = v.split("=")
        b = hash(l)
        n = int(n)
        box = m[b]
        found = False
        for i, (l2, n2) in enumerate(box):
            if l2 == l:
                found = True
                box[i] = (l2, n)
                break
        if not found:
            box.append((l, n))
    # print(m.items())

total = 0
for i, box in m.items():
    for j, (l, n) in enumerate(box):
        focus = (1+i) * (1+j) * n
        print(i, j, l, n, focus)
        total += focus

print(total)
