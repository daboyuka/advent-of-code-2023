#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
import re

inp = lines()

power = 0

for l in inp:
    game, steps = l.split(": ", 2)
    id = int(game[5:])

    mcubes = [0,0,0]
    for step in steps.split("; "):
        items = step.split(", ")
        v = [0,0,0]
        for item in items:
            n, color = ptuple(int, str)(item.split(" "))
            if color == "red" and n > mcubes[0]:
                mcubes[0] = n
            elif color == "green" and n > mcubes[1]:
                mcubes[1] = n
            elif color == "blue" and n > mcubes[2]:
                mcubes[2] = n

    power += mcubes[0] * mcubes[1] * mcubes[2]

print(power)
