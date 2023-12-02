#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
import re

stepT = pchain(pdelim(" "), ptuple(int, str))  # 3 red
stepsT = pchain(pdelim(", "), ptuple(stepT)) # step, step, ...
gamesT = pchain(pdelim("; "), ptuple(stepsT)) # steps; steps; ...

inp = lines(pchain(
    pre(r'Game (\d+): (.*)'),
    ptuple(
        int,
        gamesT
    ),
))

print(inp)

cid = {"red": 0, "green": 1, "blue": 2}

thresh = (12, 13, 14)

s = 0
for id, games in inp:
    poss = True
    if not any(any(n > thresh[cid[color]] for n, color in steps) for steps in games):
        s += id

print(s)
