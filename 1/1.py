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
    lines = [line for line in lines if line]

# Parts
def part1():
    print("=== PART 1 ===")
    pos = 50
    zeros = 0
    for line in lines:
        dir = line[0]
        amt = int(line[1:])
        amt = amt % 100
        if not amt:
            continue
        if dir == 'L':
            amt *= -1
        pos += amt
        if pos < 0:
            pos += 100
        if pos >= 100:
            pos -= 100
        if pos == 0:
            zeros += 1
    print("ANSWER: ", zeros)

def part2():
    print("=== PART 2 ===")
    pos = 50
    zeros = 0
    for line in lines:
        dir = line[0]
        amt = int(line[1:])
        print("dir", dir)
        print("amt", amt)
        print("bpos", pos)
        for i in range(0, amt):
            if dir == 'L':
                pos -= 1
            else:
                pos += 1
            if pos == -1:
                pos = 99
            elif pos > 99:
                pos = 0
            if pos == 0:
                zeros += 1
        print("apos", pos)
    print("ANSWER: ", zeros)

# Run parts
part = args.part
if part == 1 or part < 0:
    part1()
if part == 2 or part < 0:
    part2()
