#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
import re

inp = lines()

thresh = (12, 13, 14)
ok = 0

for l in inp:
    game, steps = l.split(": ", 2)
    id = int(game[5:])

    poss = True
    for step in steps.split("; "):
        items = step.split(", ")
        v = [0,0,0]
        for item in items:
            n, color = ptuple(int, str)(item.split(" "))
            if color == "red":
                v[0] += n
            elif color == "green":
                v[1] += n
            elif color == "blue":
                v[2] += n

        for i, x in enumerate(v):
            if x > thresh[i]:
                poss = False
                break

        if not poss:
            break

    if poss:
        print(id)
        ok += id

print(ok)
