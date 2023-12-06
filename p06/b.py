#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
import re

inp = lines(
    pre1(r'\w+:\s+(\d+.*)'),
    predelim(),
)

t = int("".join(inp[0]))
d = int("".join(inp[1]))

print(t, d)

m = math.sqrt(float(t)**2 - 4 * float(d)) / 2
l, r = math.ceil(t - m), math.floor(t + m)

print(r - l + 1)
