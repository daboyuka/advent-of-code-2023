#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

tiles = {
    '|': {
        north: [north],
        south: [south],
        east: [north, south],
        west: [north, south],
    },
    '-': {
        north: [east, west],
        south: [east, west],
        east: [east],
        west: [west],
    },
    '/': {
        north: [east],
        south: [west],
        east: [north],
        west: [south],
    },
    '\\': {
        north: [west],
        south: [east],
        east: [south],
        west: [north],
    }
}

inp = parsegrid(lines())

def check(ipt, id):
    active = defaultdict(lambda: set())  # [tile] -> set of dirs

    next = deque()  # (pt, dir)
    next.append((ipt, id))

    while len(next) > 0:
        pt, d = next.popleft()
        if not inp.inbounds(pt):
            continue
        if pt in active and d in active[pt]:
            continue

        active[pt].add(d)
        t = inp.at(pt)

        if t == '.':
            next.append((pt + d.gvec(), d))
        else:
            for d2 in tiles[t][d]:
                next.append((pt + d2.gvec(), d2))
    return len(active)

rs, cs = inp.size()

print(max(
    max(check(P(0, c), south) for c in trange(cs)),
    max(check(P(rs-1, c), north) for c in trange(cs)),
    max(check(P(r, 0), east) for r in trange(rs)),
    max(check(P(r, cs-1), west) for r in trange(rs)),
))
