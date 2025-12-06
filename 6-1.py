instructions = """
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""

lines = instructions.strip().splitlines()
nums = [[int(x) for x in line.split()] for line in lines[:-1]]
ops = lines[-1].split()
total = 0
for i, op in enumerate(ops):
    n = 1 if op == "*" else 0
    for row in nums:
        if op == "*":
            n *= row[i]
        else:
            n += row[i]
    total += n
print(total)
