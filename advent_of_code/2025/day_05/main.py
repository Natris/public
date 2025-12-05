import sys
import itertools
from array import array
from bisect import bisect_right

count = 0
fresh_section = []
with open(sys.argv[1], "r") as f:
    while True:
        line = f.readline().strip()
        if len(line) == 0:
            break
        items = [int(x) for x in line.split("-", maxsplit=2)]
        fresh_section.append((items[0], 1))
        fresh_section.append((items[1] + 1, -1))

    fresh_section.sort(key=lambda x: x[0])

    section_segments = [(x, sum([x[1] for x in y])) for (x, y) in itertools.groupby(fresh_section, lambda x: x[0])]
    prev = 0
    for i in range(len(section_segments)):
        prev = section_segments[i][1] + prev
        section_segments[i] = (section_segments[i][0], prev)
part_one=False
if part_one:

    section_segments_sorted_array =  [x[0] for x in section_segments]
    section_fresh_values_sorted_array = [x[1] for x in section_segments]

    for inv_item in [int(x.strip()) for x in f.readlines()]:
        index = bisect_right(section_segments_sorted_array, inv_item)
        if index > 0:
            if section_fresh_values_sorted_array[index - 1] > 0:
                count += 1

    print(count)
else:
    old_index = 0
    for index in [i for i, v in enumerate(section_segments) if v[1] == 0]:
        count += section_segments[index][0] - section_segments[old_index][0]
        old_index = index + 1
    print(count)
