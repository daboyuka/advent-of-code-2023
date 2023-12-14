#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

inp = parsegrid(lines())

def roll(g, pt, d):
    start = pt
    while True:
        pt2 = pt + d.gvec()
        if g.at(pt2) != '.':  # incl oob
            g.set(start, '.')
            g.set(pt, 'O')
            return
        pt = pt2

def weight(g):
    rs, _ = g.size()
    return sum(rs - pt[0] for pt, t in g.itertiles() if t == 'O')

for pt, t in inp.itertiles():
    if t == 'O':
        roll(inp, pt, north)

print(inp.render())

print(weight(inp))

