#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

lg = linegroups()

dirs = lg[0][0]

moves = list(map(
    pchain(
        pre(r'(\w+) = \((\w+), (\w+)\)')),
    lg[1]))

print(dirs)
print(moves)

tbl = {}
for s, l, r in moves:
    tbl[(s, "L")] = l
    tbl[(s, "R")] = r

starts = list(x[0] for x in moves if x[0].endswith("A"))

def findseq(cur):
    n = 0

    states = []
    seen = {} # (pos, inoff) = n
    while True:
        for i, step in enumerate(dirs):
            at = (cur, i)
            if at in seen:
                lastN = seen[at]
                return lastN, states[lastN:]

            states.append(cur)
            seen[at] = n

            cur = tbl[(cur, step)]
            n += 1

seqs = [findseq(start) for start in starts]

mods = []
rems = []
for off, states in seqs:
    mod = len(states)
    mods.append(mod)
    rem = set()
    for i, state in enumerate(states):
        if state.endswith("Z"):
            rem.add((off + i) % mod)
    rems.append(rem)

print(mods, rems)

lcm = 1
for mod in mods:
    lcm = lcm * mod // math.gcd(lcm, mod)

print(lcm)
exit(0)

maxIdx, maxLen = None, None
for i, (_, states) in enumerate(seqs):
    if maxLen is None or maxLen < len(states):
        maxIdx, maxLen = i, len(states)

maxMod, maxRem = mods[maxIdx], rems[maxIdx]
n = 0
while True:
    for rem in maxRem:
        ok = True
        for i, otherRem in enumerate(rems):
            mod = mods[i]
            if (n+rem) % mod not in otherRem:
                ok = False
                break
        if ok:
            print(n)
    print(n)
    n += maxMod
    # for rem in
