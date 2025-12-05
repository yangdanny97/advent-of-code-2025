instructions = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

ranges = []
ids = []
for line in instructions.split():
    if "-" in line:
        start, end = line.split("-")
        ranges.append((int(start), int(end)))
    else:
        ids.append(int(line))

ranges = sorted(ranges)
merged = [list(ranges[0])]
for r in ranges[1:]:
    if r[0] > merged[-1][1] + 1:
        merged.append(list(r))
    else:
        if r[1] > merged[-1][1]:
            merged[-1][1] = r[1]

fresh = 0
for i in ids:
    for r in merged:
        if i >= r[0] and i <= r[1]:
            fresh += 1
            break
print(fresh)
