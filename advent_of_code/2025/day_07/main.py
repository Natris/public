import sys
import itertools
import functools
from bisect import bisect_right

first_star=False
if first_star:
    count = 0
    with open(sys.argv[1], "r") as f:
        lines = [line.strip() for line in f.readlines()]
        beams=[0 for i in range(len(lines[0]))]
        for line in lines:
            new_beams=[0 for i in range(len(lines[0]))]
            for column in range(len(line)):
                if line[column] == 'S' or line[column] != '^' and beams[column] == 1:
                    new_beams[column]= 1
                if line[column] == '^' and beams[column] == 1:
                    count += 1
                    if column > 0:
                        new_beams[column-1] = 1
                    if column < len(lines)-1:
                        new_beams[column+1] = 1
            beams = new_beams
    print(count)
else:
    count = 0
    with open(sys.argv[1], "r") as f:
        lines = [line.strip() for line in f.readlines()]
        beams = [0 for i in range(len(lines[0]))]
        for line in lines:
            new_beams = [0 for i in range(len(lines[0]))]
            for column in range(len(line)):
                if line[column] == 'S':
                    new_beams[column] = 1
                if line[column] != '^' and beams[column] > 0:
                    new_beams[column] += beams[column]
                if line[column] == '^' and beams[column] > 0:
                    if column > 0:
                        new_beams[column - 1] += beams[column]
                    if column < len(lines) - 1:
                        new_beams[column + 1] += beams[column]
            beams = new_beams
    print(sum(beams))
