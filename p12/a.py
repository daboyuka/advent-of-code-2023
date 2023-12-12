#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re


inp = lines(
    pdelim(),
    ptuple(
        str,
        pchain(
            pdelim(","),
            pmap(int)
        )
    )
)

def check(s):
    spr = []
    on = False
    for c in s:
        if c == "#":
            if not on:
                spr.append(0)
                on = True
            spr[-1] += 1
        else:
            on = False
    return spr

def combos(s):
    combo = idict() # (springs, on) -> n
    combo[(tuple(), False)] = 1
    for c in s:
        combo2 = idict()
        if c != ".":
            for (spr, on), n in combo.items():
                if not on:
                    spr = spr + (1,)
                    on = True
                else:
                    spr = spr[:-1] + (spr[-1] + 1,)
                combo2[(spr, on)] += n
        if c != "#":
            for (spr, on), n in combo.items():
                on = False
                combo2[(spr, on)] += n
        combo = combo2

    return combo

total = 0
for spr, expect in inp:
    c = combos(spr)
    n = c[(tuple(expect), False)] + c[(tuple(expect), True)]
    total += n

print(total)
