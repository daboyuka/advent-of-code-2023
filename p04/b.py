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

print(inp)

total = 0
nextDups = deque()

for id, wins, haves in inp:
    winTable = defaultdict(lambda: False)
    for win in wins:
        winTable[win] = True

    matches = 0
    for have in haves:
        if winTable[have]:
            matches += 1

    copies = 1
    if len(nextDups) > 0:
        copies += nextDups.popleft()

    if matches > 0:
        while len(nextDups) < matches:
            nextDups.append(0)
        for i in range(matches):
            nextDups[i] += copies

    total += copies

    print(id, copies, matches, nextDups)

print(total)
