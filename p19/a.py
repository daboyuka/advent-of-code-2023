#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

def deb(v):
    return v

rules, inp = linegroups(
    pchain(
        pre(r"(\w+)\{([^}]+)\}"),
        ptuple(
            str,
            pdelim(",", deb, pre(r"(?:(.)(.)(\d+):)?(\w+)")),
        ),
    ),
    pchain(
        pre1(r"\{(.*)\}"),
        pdelim(",",
               pre(r"(.)=(\d+)"),
                ptuple(str, int)),
    ),
)

flows = dict()
for n, steps in rules:
    flows[n] = steps

def dorule(steps, vals):
    for cond, cmp, thresh, to in steps:
        if cond is None:
            return to
        v = vals[cond]
        if cmp == "<":
            tst = v < int(thresh)
        elif cmp == ">":
            tst = v > int(thresh)
        elif cmp == "=":
            tst = v == int(thresh)
        # print(cond, cmp, thresh, to, v, tst)
        if tst:
            return to

total = 0
for vals in inp:
    d = dict()
    for k, v in vals:
        d[k] = v

    at = "in"
    while at != "A" and at != "R":
        at = dorule(flows[at], d)
        # print(at)
    if at == "A":
        total += sum(d.values())
    print(vals, "->", at)

print(total)
