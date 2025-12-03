import sys


with open(sys.argv[1], "r") as f:
        sum = 0
        line = f.read()
        for r in line.split(","):
            beg, end = r.split("-")
            beg, end = int(beg), int(end)
            for i in range(beg,end+1):
                i_str = str(i)
                for rep in range(2, len(i_str) + 1):
                    if len(i_str) % rep == 0:
                        count = len(i_str) // rep
                        match = True
                        for index in range(count, len(i_str), count):
                            if i_str[0:count] != i_str[index:index + count]:
                                match = False
                                break
                        if match:
                            sum += i
                            break
        print(sum)

