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
    low, high, ok, highs = 0, 0, False, set()

    q = deque([("button", "broadcaster", False)])  # (from, name, pulse)
    while len(q) > 0:
        src, name, pulse = q.popleft()
        if pulse:
            high += 1
        else:
            low += 1
        if name == "rx" and not pulse:
            ok = True
        if name == "bq" and pulse:
            highs.add(src)

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
    return low, high, ok, highs


# offset, period = None, None

# seqidx = dict()  # state -> (idx, total)

# total = P(0, 0)
# offsetSum, periodSum = None, None

allhighs = dict()
for i in range(1000000000000):
    # fs = freezestates()
    # if fs in seqidx:
    #     offset, pretotal = seqidx[fs]
    #     period = i - offset
    #     offsetSum, periodSum = pretotal, total - pretotal
    #     break
    # seqidx[fs] = (i, total)
    _, _, ok, highs = run()
    for hname in highs:
        if hname in allhighs:
            allhighs[hname].append(i)
        else:
            allhighs[hname] = [i]

    if len(highs) > 0:
        print(list(sorted((n, l[0], len(l), l[-1]) for n, l in allhighs.items())))

    if ok:
        print(i)
        exit(0)
    # print(i, low, high, fs)

# gc = i*4001-1
# kp = i*3929-1
# tx = i*3769-1
# vg = i*4027-1

# i % 4001 = -1

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
