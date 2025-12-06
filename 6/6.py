#!/usr/bin/python3

import os
import sys
import math
import argparse
import re
import collections
import pprint
import itertools
import functools
import datetime
import copy
import shapely

# Parse args
p = argparse.ArgumentParser()
p.add_argument('--test', default=False, action='store_true')
p.add_argument('--part', type=int, default=-1)
args = p.parse_args()

# Get input
if args.test:
    print("!!! TEST !!!")
    fn = 'test.txt'
else:
    fn = 'input.txt'

# Get data
print(f"INPUT: {fn}")

# Parts
def part1():
    print("=== PART 1 ===")
    with open(fn, 'r') as f:
        lines = [line.strip() for line in f]
        vals, ops = [list(map(int, line.split())) for line in lines[:-1]], [x for x in lines[-1].split()]
    ans = 0
    for c in range(0, len(ops)):
        op = sum if ops[c] == '+' else math.prod
        ans += op([r[c] for r in vals])

    print("ANSWER: ", ans)

def part2():
    print("=== PART 2 ===")
    with open(fn, 'r') as f:
        lines = [line for line in f]
    rows = [line for line in lines[:-1] if line.strip()]
    ops = [c for c in lines[-1].split()]

    print(f"{rows=}")
    ans = 0
    vals = collections.defaultdict(str)
    for c in range(len(rows[0])):
        print(f"{c=}")
        if all([line[c] in (' ', '\n') for line in rows]):
            print(f"BREAK {vals=}")
            op = ops[0]
            print(f"OP {op=}")
            op = sum if op == '+' else math.prod
            ops.pop(0)
            tot = op(map(int, vals.values()))
            print(f"{tot=}")
            ans += tot
            vals.clear()
            continue
        for r, line in enumerate(rows):
            vals[c] += line[c]
        print(f"inter {vals=}")

    print("ANSWER: ", ans)

# Run parts
part = args.part
if part == 1 or part < 0:
    part1()
if part == 2 or part < 0:
    part2()
