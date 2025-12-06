instructions = """
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""
from itertools import batched

lines = instructions.strip().splitlines()
chars = [list(x) for x in lines[:-1]]
transposed = list(map(list, zip(*chars)))

nums = [[]]
for row in transposed:
    joined = "".join(row).strip()
    if not joined:
        nums.append([])
    else:
        nums[-1].append(int(joined))

ops = lines[-1].split()
total = 0
for i, col in enumerate(nums):
    op = ops[i]
    n = 1 if op == "*" else 0
    for num in col:
        if op == "*":
            n *= num
        else:
            n += num
    total += n
print(total)
