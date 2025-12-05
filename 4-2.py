from collections import defaultdict
instructions = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

rows = instructions.split()
mapping = defaultdict(lambda: 0)
for i, row in enumerate(rows):
    for j, item in enumerate(row):
        mapping[(i, j)] = 1 if (item == "@") else 0

count = 0
entries = [x for x in mapping]
while len(entries) > 0:
    i, j = entries.pop()
    if not mapping[(i, j)]:
        continue
    search = [(i + 1, j),
              (i + 1, j + 1),
              (i + 1, j - 1),
              (i - 1, j),
              (i - 1, j + 1),
              (i - 1, j - 1),
              (i, j + 1),
              (i, j - 1)]
    n = sum([mapping[x] for x in search])
    if n < 4:
        mapping[(i, j)] = 0
        count += 1
        entries.extend(search)
print(count)
