import sys
import itertools
import math
import functools
from bisect import bisect_right
import collections

first_star=False
if first_star:
    count = 0
    with open(sys.argv[1], "r") as f:
        coords = []
        for line in f.readlines():
            coords.append([int(x) for x in line.split(",")])
        dists = {}
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                dist = math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2 + (coords[i][2] - coords[j][2]) ** 2)
                if dist in dists:
                    print("fuck")
                    exit(1)
                dists[dist]=(i, j)
        connected = range(len(coords))

        connection_count_left = 1000
        for item in sorted(dists.items()):
            if connection_count_left == 0:
                break

            a = item[1][0]
            b = item[1][1]
            a_grp = connected[a]
            b_grp = connected[b]
            connected = [x if (x != a_grp and x != b_grp) else min(a_grp, b_grp) for x in connected]
            connection_count_left -= 1
        counts = sorted(collections.Counter(connected).values())
        print(counts[-1] * counts[-2] * counts[-3])
else:
    count = 0
    with open(sys.argv[1], "r") as f:
        coords = []
        for line in f.readlines():
            coords.append([int(x) for x in line.split(",")])
        dists = {}
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                dist = math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2 + (
                            coords[i][2] - coords[j][2]) ** 2)
                if dist in dists:
                    print("fuck")
                    exit(1)
                dists[dist] = (i, j)
        connected = range(len(coords))

        for item in sorted(dists.items()):

            a = item[1][0]
            b = item[1][1]
            a_grp = connected[a]
            b_grp = connected[b]
            connected = [x if (x != a_grp and x != b_grp) else min(a_grp, b_grp) for x in connected]
            if a_grp != b_grp:
                if len(list(itertools.dropwhile(lambda x: x == 0, connected))) == 0:
                    print(coords[a][0] * coords[b][0])
                    exit(0)
