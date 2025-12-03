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
ranges = []
with open(fn, 'r') as f:
    lines = [line.strip() for line in f]
    for line in lines:
        for r in line.split(','):
            if not r:
                continue
            ranges.append(tuple(map(int, r.split('-'))))
print(ranges)

# Parts
def part1():
    print("=== PART 1 ===")
    count = 0
    for rhs, lhs in ranges:
        print("range", rhs, lhs)
        for i in range(rhs, lhs + 1):
            s = str(i)
            l = len(s)
            if l % 2:
                continue
            half = int(l/2)
            if s[0:half] == s[half:]:
                count += i
    print("ANSWER: ", count)

def part2():
    print("=== PART 2 ===")
    count = 0
    for rhs, lhs in ranges:
        for i in range(rhs, lhs + 1):
            s = str(i)
            l = len(s)
            half = int(l/2)
            for h in range(1, half + 1):
                if len(set(itertools.batched(s, n=h))) == 1:
                    count += i
                    break
    print("ANSWER: ", count)

# Run parts
part = args.part
if part == 1 or part < 0:
    part1()
if part == 2 or part < 0:
    part2()
