#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
import re

inp = lines(
    pre(r"Card\s+(\d+):\s+(.*)\s+\|\s+(.*)\s*"),
    ptuple(
        int,
        predelim(" +", int),
        predelim(" +", int),
    )
)

total = 0

for id, wins, haves in inp:
    winTable = defaultdict(lambda: False)
    for win in wins:
        winTable[win] = True

    score = 0
    for have in haves:
        if winTable[have]:
            if score == 0:
                score = 1
            else:
                score *= 2

    print(id, score)
    total += score

print(total)
