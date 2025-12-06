import sys
import itertools
import functools
from bisect import bisect_right

first_star=False
if first_star:
    def strip_empty(l):
        return list(itertools.filterfalse(lambda x: x == "", l))

    count = 0
    with open(sys.argv[1], "r") as f:

        lines = [strip_empty([x.strip() for x in line.split(" ")]) for line in f.readlines()]
        for column in range(len(lines[-1])):
            op_mul = lines[-1][column] == '*'
            if op_mul:
                l = lambda prev,v: prev * int(v[column])
                init = 1
            else:
                l = lambda prev,v: prev + int(v[column])
                init = 0
            res = functools.reduce(l, lines[:-1], initial=init)
            count += res
    print(count)
else:
    count = 0
    with open(sys.argv[1], "r") as f:
        raw_lines =  [x.strip("\n") for x in f.readlines()]
        for col_index in range(len(raw_lines[0])):
            column =list(map(lambda x: x[col_index], raw_lines))
            if column[-1] != " ":
                op_mul = column[-1] == '*'
                if op_mul:
                    v = 1
                else:
                    v = 0
            column[-1] = " "
            digits = list(itertools.filterfalse(lambda x: x == " ", column))
            if len(digits) == 0:
                count += v
            else:
                number = int(functools.reduce(lambda prev, v: prev * 10 + int(v), digits, initial=0))
                if op_mul:
                    v = v * number
                else:
                    v = v + number
        count += v
        print(count)