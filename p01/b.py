#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
import re

names = {
    # "zero":0,
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
}

def repnum(s):
    out = ""
    i = 0
    while i < len(s):
        found = False
        for k, v in names.items():
            if s[i:].startswith(k):
                out += str(v)
                i += 1
                found = True
                break
        if not found:
            out += s[i]
            i += 1
    return out


inp = lines(repnum)
print("\n".join(inp))

sum = 0
for line in inp:
    first, last = None, None
    for c in line:
        if c < "0" or c > "9":
            continue
        i = int(c)
        if first is None:
            first = i
        last = i
    val = first * 10 + last
    print(val)
    sum += val

print(sum)
