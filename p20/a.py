#!/usr/bin/env python3
from helpers import *
from itertools import *
from collections import *
from functools import *
from tqdm import *
import re

inp = lines(
    pre(r"([^ ]+)\s+->\s+(.*)"),
    ptuple(
        str,
        predelim(r",\s+"),
    )
)

print(inp)

kinds = dict() # name -> kind
g = ldict()  # name -> outputs
ginv = ldict()  # name -> inputs

for name, outputs in inp:
    if name == "broadcaster":
        kinds[name] = name
    elif name.startswith("%"):
        name = name[1:]
        kinds[name] = "%"
    elif name.startswith("&"):
        name = name[1:]
        kinds[name] = "&"
    g[name] = outputs
    for output in outputs:
        ginv[output].append(name)

for name in ginv.keys():
    if name not in kinds:
        kinds[name] = ""

# order = []
# visit = set()
# def dft(at):
#     if at in visit:
#         return
#     visit.add(at)
#     for output in g[at]:
#         dft(output)
#     order.append(at)
# dft("broadcaster")

nameorder = []
idxmap = idict()
for i, name in enumerate(kinds.keys()):
    nameorder.append(name)
    idxmap[name] = i

states = dict()  # name -> state
for name, kind in kinds.items():
    if kind == "%":
        states[name] = False
    elif kind == "&":
        states[name] = bdict()
        for input in ginv[name]:
            states[name][input] = False
    else:
        states[name] = None

def freezestate(state):
    if type(state) != bool and state is not None:
        return tuple(state[name] for name in nameorder if name in state)
    else:
        return state

def freezestates():
    return tuple((freezestate(states[name])) for name in nameorder)


def run():
    low, high = 0, 0

    q = deque([("button", "broadcaster", False)])  # (from, name, pulse)
    while len(q) > 0:
        src, name, pulse = q.popleft()
        if pulse:
            high += 1
        else:
            low += 1

        #print("pulse", pulse, "at", src, "->", name, "state", states[name])
        k = kinds[name]
        inputs = ginv[name]
        outputs = g[name]
        if k == "broadcaster":
            for output in outputs:
                q.append((name, output, pulse))
        elif k == "%":
            if not pulse:
                v = not states[name]
                states[name] = v
                for output in outputs:
                    q.append((name, output, v))
        elif k == "&":
            states[name][src] = pulse #not states[name][src]
            v = not all(states[name].values())
            for output in outputs:
                q.append((name, output, v))
    return low, high


offset, period = None, None

seqidx = dict()  # state -> (idx, total)

total = P(0, 0)
offsetSum, periodSum = None, None

for i in range(1000):
    fs = freezestates()
    if fs in seqidx:
        offset, pretotal = seqidx[fs]
        period = i - offset
        offsetSum, periodSum = pretotal, total - pretotal
        break
    seqidx[fs] = (i, total)
    low, high = run()
    total += P(low, high)
    print(i, low, high, fs)

print(offset, period, offsetSum, periodSum)

if offset == None:
    print(total)
    print(total[0] * total[1])
    exit(0)

cycles = (1000 - offset) // period
rem = (1000 - offset) % period

remtotal = P(0, 0)
for i in range(rem):
    remtotal += P(run())

final = offsetSum + periodSum * cycles + remtotal
print(final)
print(final[0] * final[1])
