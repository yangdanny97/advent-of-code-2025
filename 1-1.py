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
    if dir == "L":
        pos = (pos - n) % 100
    else:
        pos = (pos + n) % 100

    if pos == 0:
        count += 1
print(count)
