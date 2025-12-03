instructions = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
pos = 50
count = 0
for line in instructions.split():
    dir = line[0]
    n = int(line[1:])
    old_pos = pos
    if dir == "L":
        count += n // 100
        pos = (pos - n) % 100
        if (pos > old_pos and old_pos != 0) or pos == 0:
            count += 1
    else:
        count += n // 100
        pos = (pos + n) % 100
        if pos < old_pos or pos == 0:
            count += 1
print(count)
