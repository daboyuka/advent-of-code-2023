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

cid = {"red": 0, "green": 1, "blue": 2}

s = 0
for id, games in inp:
    s += prod(
        max(
            max(
                (n for n, color in steps if cid[color] == whichcolor),
                default=0
            ) for steps in games
        ) for whichcolor in [0, 1, 2]
    )

print(s)
