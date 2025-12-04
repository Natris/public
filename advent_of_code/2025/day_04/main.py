import sys
import itertools

def read_lines(f):
    #0 = empty, 1 = zavinac, 2 = removed
    size = 0
    for line in f.readlines():
        line = line.strip()
        if size < len(line):
            size = len(line)
            yield [0 for _ in range(size + 2)]
        yield [0] + [1 if x == '@' else 0 for x in line] + [0]

    yield [0 for _ in range(size + 2)]
    return

count = 0
part2 = 1 # first or second star?
with open(sys.argv[1], "r") as f:
        array = list(read_lines(f))
        total_count = 0
        while True:
            line_nr = -1
            count = 0
            for x in range(0, len(array) - 2):
                for y in range(0, len(array[x]) - 2):
                    if array[x+1][y+1] == 1:
                        tmp_list = [x[y: y + 3] for x in array[x: x+3]]
                        flat_tmp_list = [item for sublist in tmp_list for item in sublist]
                        res = sum([1 for ch in flat_tmp_list if ch == 1])
                        if res < 5:
                            count = count + 1
                            array[x+1][y+1] = 2
            if count == 0 or not part2:
                break
            total_count += count

        print(total_count)

