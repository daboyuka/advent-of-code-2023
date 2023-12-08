#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

lg = linegroups()

dirs = lg[0][0]

moves = list(map(
    pchain(
    pre(r'(\w+) = \((\w+), (\w+)\)')),
    lg[1]))

print(dirs)
print(moves)

tbl = {}
for s, l, r in moves:
    tbl[(s, "L")] = l
    tbl[(s, "R")] = r

n = 0
cur = "AAA"
while True:
    for step in dirs:
        cur = tbl[(cur, step)]
        n += 1
        if cur == "ZZZ":
            print(n)
            exit(0)
