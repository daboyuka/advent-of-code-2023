#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
import re

inp = lines()

g = parsegrid(inp)

rows, cols = g.size()


def scannum(pt):
    numStr = ""
    for i in range(cols):
        t = g.at(pt + P(0, i), '.')
        if t < "0" or t > "9":
            break
        numStr += t
    return int(numStr), len(numStr)

def scanborder(pt, l):
    for i in range(l+2):
        if checkpt(pt + P(-1, i-1)) or checkpt(pt + P(1, i-1)):
            return True
    if checkpt(pt + P(0, -1)) or checkpt(pt + P(0, l)):
        return True
    return False

def checkpt(pt):
    t = g.at(pt, '.')
    return (t < "0" or t > "9") and t != "."

ans = 0
for row in range(rows):
    col = 0
    while col < cols:
        pt = P(row, col)
        t = g.at(pt)
        if t >= "0" and t <= "9":
            n, skip = scannum(pt)
            if scanborder(pt, skip):
                ans += n
                print(n, "PART")
            else:
                print(n)

            col += skip
        else:
            col += 1

print(ans)
