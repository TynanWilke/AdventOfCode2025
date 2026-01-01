#!/usr/bin/python3

import math
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
    jbs = [tuple(map(int, line.split(','))) for line in lines]
    print(f"{jbs=}")

# Parts
def part1():
    print("=== PART 1 ===")
    def link_dist(link):
        (x1, y1, z1), (x2, y2, z2) = link
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

    max_connections = 10 if fn == 'test.txt' else 1000
    links = itertools.combinations(jbs, 2)
    dists = {link: link_dist(link) for link in links}
    sdists = [x[0] for x in sorted(dists.items(), key=lambda x: x[1])]
    slinks = sdists[:max_connections]

    circuits = []
    while slinks:
        link = slinks[-1]
        slinks.pop()
        print(f"{link=}")

        rhs, lhs = link
        circuit = set()
        circuit.add(rhs)
        circuit.add(lhs)
        for clink in copy.copy(slinks):
            clhs, crhs = clink
            for jb in copy.copy(circuit):
                if jb == clhs or jb == crhs:
                    circuit.add(clhs)
                    circuit.add(crhs)
                    slinks.remove(clink)
                    break
        circuits.append(circuit)
    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    top3 = circuits[:3]
    pprint.pprint(top3)

    n = math.prod(len(circuit) for circuit in top3)
    print("ANSWER: ", n)

def part2():
    print("=== PART 2 ===")
    print("ANSWER: ", "HERE")

# Run parts
part = args.part
if part == 1 or part < 0:
    part1()
if part == 2 or part < 0:
    part2()
