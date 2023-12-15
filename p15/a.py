#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

inp = lines(pdelim(","))
print(inp)

def hash(x):
    v = 0
    for c in x:
        v += ord(c)
        v *= 17
        v %= 256
    return v


print(sum(hash(v) for v in inp[0]))
