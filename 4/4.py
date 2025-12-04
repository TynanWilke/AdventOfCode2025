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
rolls = {}
with open(fn, 'r') as f:
    lines = [line.strip() for line in f if line.strip()]
    rolls = [(r, c)
             for r, line in enumerate(lines)
             for c, x in enumerate(line) if x == '@']
print("rolls", rolls, len(rolls))

# Parts
def part1():
    print("=== PART 1 ===")
    offs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    bs = {roll: [(roll[0] + off[0], roll[1] + off[1]) for off in offs if (roll[0] + off[0], roll[1] + off[1]) in rolls] for roll in rolls}
    pprint.pprint(bs)
    good_rolls = [roll for roll, b in bs.items() if len(b) < 4]
    print("good_rolls", good_rolls)

    print("ANSWER: ", len(good_rolls))

def part2():
    print("=== PART 2 ===")
    print("ANSWER: ", "HERE")

# Run parts
part = args.part
if part == 1 or part < 0:
    part1()
if part == 2 or part < 0:
    part2()
