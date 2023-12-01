#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
import re

inp = lines()

sum = 0
for line in inp:
    first, last = None, None
    for c in line:
        if c < "0" or c > "9":
            continue
        i = int(c)
        if first is None:
            first = i
        last = i
    val = first * 10 + last
    sum += val

print(sum)
