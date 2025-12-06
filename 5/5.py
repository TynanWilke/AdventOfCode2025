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
    inv, ing = f.read().split('\n\n')
    invs = [tuple(map(int, i.split('-'))) for i in inv.split('\n') if i.strip()]
    ings = [int(i) for i in ing.split('\n') if i.strip()]

# Parts
def part1():
    print("=== PART 1 ===")
    fresh = 0
    for ing in ings:
        for inv in invs:
            rhs, lhs = inv
            if rhs <= ing <= lhs:
                fresh += 1
                break
    print("ANSWER: ", fresh)

def part2():
    print("=== PART 2 ===")
    fresh = set()
    for inv in invs:
        beg, end = inv
        new_fresh = []
        for fresh in fresh:
            fbeg, fend = fresh
            # Inner
            if fbeg <= beg <= fend and fbeg <= end <= fend:
                beg = fbeg
                end = fend
                continue

            # Outer
            elif beg <= fbeg <= end and beg <= fend <= end:
                continue

            # Over right
            elif beg < fbeg and fbeg <= end <= fend:
                end = fend
                continue

            # Over left
            elif fbeg <= beg <= fend and end > fend:
                beg = fbeg
                continue

            # Add to new fresh ranges
            new_fresh.append((fbeg, fend))

        if beg and end:
            new_fresh.append((beg, end))
        fresh = new_fresh
    c = sum([1 + end - beg for beg, end in fresh])
    print("ANSWER: ", c)

# Run parts
part = args.part
if part == 1 or part < 0:
    part1()
if part == 2 or part < 0:
    part2()
