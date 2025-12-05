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
for i, j in entries:
    if not mapping[(i, j)]:
        continue
    n = (
        mapping[(i + 1, j)] + 
        mapping[(i + 1, j + 1)] +
        mapping[(i + 1, j - 1)] +
        mapping[(i - 1, j)] +
        mapping[(i - 1, j + 1)] +
        mapping[(i - 1, j - 1)] +
        mapping[(i, j + 1)] +
        mapping[(i, j - 1)]
    )
    if n < 4:
        count += 1
print(count)
