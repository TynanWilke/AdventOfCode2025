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

# Parts
def part1():
    print("=== PART 1 ===")
    jolt = 0
    for line in lines:
        print("line", line)
        sline = sorted(line[:-1], reverse=True)
        print("sline", sline)
        a, b = sline[:2]
        print("top", a, b)
        ma = a + max(line[line.index(a) + 1:])
        mb = b + max(line[line.index(b) + 1:])
        print("ma mb", ma, mb)
        best = max(ma, mb)
        jolt += int(best)
        print("jolt", jolt)
    print("ANSWER: ", jolt)

def part2():
    print("=== PART 2 ===")
    max_len = 12
    jolt = 0
    for line in lines:
        best = ""
        for i in range(0, max_len):
            print("line", line)
            remain = max_len - i
            print("remain", remain)
            if remain > 1:
                opts = line[:1 - remain]
            else:
                opts = line
            print("opts", opts)
            b = max(opts)
            print("b", b)
            best += b
            print("best", best)
            line = line[line.index(b) + 1:]
        print("jolt", best)
        jolt += int(best)

    print("ANSWER: ", jolt)

# Run parts
part = args.part
if part == 1 or part < 0:
    part1()
if part == 2 or part < 0:
    part2()
