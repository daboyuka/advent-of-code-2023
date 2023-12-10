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
    sum = 0
    while any(x != 0 for x in seq):
        sum += seq[-1]
        seq = diffseq(seq)
    print(sum)
    total += sum

# print(inp)
print(total)
