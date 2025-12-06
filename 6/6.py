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
with open(fn, 'r') as f:
    lines = [line.strip() for line in f]
    vals, ops = [list(map(int, line.split())) for line in lines[:-1]], [x for x in lines[-1].split()]
    print(f"{vals=}")
    print(f"{ops=}")

# Parts
def part1():
    print("=== PART 1 ===")
    ans = 0
    for c in range(0, len(ops)):
        op = sum if ops[c] == '+' else math.prod
        ans += op([r[c] for r in vals])

    print("ANSWER: ", ans)

def part2():
    print("=== PART 2 ===")
    print("ANSWER: ", "HERE")

# Run parts
part = args.part
if part == 1 or part < 0:
    part1()
if part == 2 or part < 0:
    part2()
