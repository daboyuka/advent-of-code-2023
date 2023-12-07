#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

cards = {"A":13,"K":12,"Q":11,"J":1,"T":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}

inp = lines(
    pre(r'(.{5}) (\d+)'),
    ptuple(str, int),
)

def stren(hand):
    j = 0
    suits = idict()
    for s in hand:
        if s == "J":
            j += 1
        else:
            suits[s] += 1

    counts = []
    for _, c in suits.items():
        counts.append(c)
    while len(counts) < 2:
        counts.append(0)

    counts = list(sorted(counts, reverse=True))
    print(hand, counts, j)

    if counts[0]+j >= 5:
        return 7
    elif counts[0]+j >= 4:
        return 6
    elif counts[0]+j >= 3:
        jl = j-(3-counts[0])
        if counts[1]+jl >= 2:
            return 5
        else:
            return 4
    elif counts[0]+j >= 2:
        jl = j-(2-counts[0])
        if counts[1]+jl >= 2:
            return 3
        else:
            return 2
    else:
        return 1


def cmp(h1, h2):
    s1, s2 = stren(h1), stren(h2)
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    for i, s1 in enumerate(h1):
        s2 = h2[i]
        r1, r2 = cards[s1], cards[s2]
        if r1 < r2:
            return -1
        elif r1 > r2:
            return 1
    return 0


def cmpentry(e1, e2):
    h1, _ = e1
    h2, _ = e2
    print(e1, e2, h1, h2)
    return cmp(h1, h2)


for e in inp:
    print(e[0],"->",stren(e[0]))

s = sorted(inp, key=cmp_to_key(cmpentry))

ans = 0
for i, x in enumerate(s):
    bid = x[1]
    print(i, bid)
    ans += (i+1)*bid
print(ans)
