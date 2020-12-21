data = open("day10.txt")
data = data.read()
data = data.split("\n")

from collections import defaultdict
# if you sort them, you will only need to take differences

adaptors = [int(j) for j in data]
adaptors = [0] + sorted(adaptors)
# adding the device joltage
adaptors.append(adaptors[-1]+3)

diff = defaultdict(int)
count = []
for a, b in zip(adaptors[1:], adaptors):
    diff[a-b] += 1
    count.append(a-b)

print(diff[1]*diff[3])
print(count)


# PART 2

aggregate = []
len_count = 0
for c in count:
    if c == 1:
        len_count += 1
    else:
        aggregate.append(len_count)
        len_count = 0

aggregate = [c for c in aggregate if c > 0]

combinations = 1
for c in aggregate:
    if c == 1:
        combinations = combinations*1
    if c == 2:
        combinations = combinations*2
    if c == 3:
        combinations = combinations*4
    if c == 4:
        combinations = combinations*7

print(combinations)
diffs = defaultdict(int)
counts = defaultdict(int, {0: 1})        
for a, b in zip(adaptors[1:], adaptors):
    diffs[a - b] += 1
    # number of ways to reach i'th adapter from previous three possible ones
    counts[a] = counts[a - 3] + counts[a - 2] + counts[a - 1]

print(diffs[1] * diffs[3])
print(counts)
