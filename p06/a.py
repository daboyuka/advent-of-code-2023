#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
import re

inp = lines(
    pre1(r'\w+:\s+(\d+.*)'),
    predelim(),
    ptuple(int),
)

times, dists = inp
print()

ans = 1
for t, d in zip(times, dists):
    wins = 0
    for hold in range(1, t):
        d2 = hold * (t - hold)
        if d2 > d:
            wins += 1
    if wins > 0:
        ans *= wins

print(ans)
