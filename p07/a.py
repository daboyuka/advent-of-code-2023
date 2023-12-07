#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

cards = {"A":14,"K":13,"Q":12,"J":11,"T":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}

inp = lines(
    pre(r'(.{5}) (\d+)'),
    ptuple(str, int),
)

def stren(hand):
    suits = idict()
    for s in hand:
        suits[s] += 1

    counts = ldict()
    for s, c in suits.items():
        counts[c].append(s)

    if len(counts[5]) == 1:
        return 7
    elif len(counts[4]) == 1:
        return 6
    elif len(counts[3]) == 1 and len(counts[2]) == 1:
        return 5
    elif len(counts[3]) == 1 and len(counts[2]) == 0:
        return 4
    elif len(counts[2]) == 2:
        return 3
    elif len(counts[2]) == 1:
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


s = sorted(inp, key=cmp_to_key(cmpentry))

ans = 0
for i, x in enumerate(s):
    bid = x[1]
    print(i, bid)
    ans += (i+1)*bid
print(ans)
