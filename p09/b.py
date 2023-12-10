#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

inp = lines(pdelim(), pmap(int))

def diffseq(x):
    return [b-a for (a, b) in itertools.pairwise(x)]

total = 0
for seq in inp:
    s = 0
    neg = 1
    while any(x != 0 for x in seq):
        s += seq[0] * neg
        neg *= -1
        seq = diffseq(seq)
    print(s)
    total += s

# print(inp)
print(total)

