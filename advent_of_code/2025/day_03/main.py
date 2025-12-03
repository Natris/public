import sys

digit_count = 12
with open(sys.argv[1], "r") as f:
        sum = 0
        for line in f.readlines():
            line = line.strip()
            accum = 0
            begin = 0
            len_line = len(line)
            for dig in range(0, digit_count):
                accum = accum * 10
                maxval=0
                maxi=0
                end = len_line - (digit_count - dig - 1)
                for i in range(begin, end):
                    val = int(line[i])
                    if val > maxval:
                        maxval = val
                        maxi = i
                begin = maxi + 1
                accum = accum + maxval
            sum += accum
        print(sum)

