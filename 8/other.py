from math import prod
from operator import itemgetter

import numpy as np
from scipy.spatial.distance import pdist, squareform

with open("input.txt") as f:
    coords = [[int(i) for i in x.split(",")] for x in f]

n_nodes = len(coords)
distances = sorted(np.ndenumerate(squareform(pdist(coords))), key=itemgetter(1))[n_nodes::2]

clustering = [{i} for i in range(n_nodes)]
for idx, ((n1, n2), _) in enumerate(distances):
    curr = []
    s1 = None
    s2 = None
    for s in clustering:
        if n1 in s or n2 in s:
            if n1 in s:
                s1 = s
            if n2 in s:
                s2 = s
        else:
            curr.append(s)
    if s1 == s2:
        curr.append(s1)
    else:
        curr.append(s1.union(s2))
    if idx == 1000:
        print(prod(sorted([len(c) for c in clustering])[-3:]))
    clustering = curr
    if len(clustering) == 1:
        print(coords[n1][0] * coords[n2][0])
        break
