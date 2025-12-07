#!/usr/bin/python3

import os
import sys
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
    start = lines[0].index('S')
    splitters = [(r, c)
                 for r, line in enumerate(lines)
                 for c, x in enumerate(line)
                 if x == '^']

# Parts
def part1():
    print("=== PART 1 ===")
    tachs = set([(0, start)])
    max_r = max(r for r, _ in splitters)
    splits = 0
    for i in range(max_r):
        # Move tach down
        tachs = set([(r + 1, c) for r, c in tachs])

        # Find tachs on splitters
        for tach in copy.copy(tachs):
            r, c = tach
            if tach in splitters:
                tachs.add((r, c - 1))
                tachs.add((r, c + 1))
                tachs.remove(tach)
                splits += 1
    print("ANSWER: ", splits)

def part2():
    print("=== PART 2 ===")
    max_r = max(r for r, _ in splitters)
    memo = {}
    def num_paths(path):
        tach = path[-1]
        r, c = tach
        if r >= max_r + 1:
            return 1

        if tach in memo:
            return memo[tach]

        if tach in splitters:
            lhs_path = copy.copy(path)
            lhs_path.pop()
            lhs_path.append((r, c - 1))
            lhs = num_paths(lhs_path)

            rhs_path = copy.copy(path)
            rhs_path.pop()
            rhs_path.append((r, c + 1))
            rhs = num_paths(rhs_path)
            n = lhs + rhs
        else:
            next_path = copy.copy(path)
            next_path.append((r + 1, c))
            n = num_paths(next_path)

        memo[tach] = n
        return n

    path = [(0, start)]
    n = num_paths(path)
    print("ANSWER: ", n)

# Run parts
part = args.part
if part == 1 or part < 0:
    part1()
if part == 2 or part < 0:
    part2()
