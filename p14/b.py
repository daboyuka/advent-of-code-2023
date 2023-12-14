#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

inp = parsegrid(lines())

def roll(g, pt, d):
    if g.at(pt) != 'O':
        return
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

def spin():
    for pt, _ in inp.itertiles(south):
        roll(inp, pt, north)
    for pt, _ in inp.itertiles(east):
        roll(inp, pt, west)
    for pt, _ in inp.itertiles(north):
        roll(inp, pt, south)
    for pt, _ in inp.itertiles(west):
        roll(inp, pt, east)


states = idict()
wstates = dict()

offset, period = None, None
for i in trange(0, 100000):
    cur = inp.render()
    if cur in states:
        offset, period = states[cur], i - states[cur]
        break
    states[cur] = i
    wstates[i] = weight(inp)
    spin()

print(offset, period)
rem = (1000000000 - offset) % period

print(wstates[offset + rem])
