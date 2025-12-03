import sys


with open(sys.argv[1], "r") as f:
        pos = 50
        res = 0
        was_zero = False
        for line in f.readlines():
            if len(line) > 1:
                mul = 1 if line[0] == 'R' else -1
            v = int(line[1:])
            res += v // 100
            v = v % 100
            begin_pos = pos if (not was_zero or mul > 0) else pos + 100
            pos_raw = begin_pos + v * mul
            pos = pos_raw % 100
            if pos_raw >= 100 or pos_raw <= 0:
                if not was_zero:
                    res += 1
            was_zero = pos == 0
        print(res)