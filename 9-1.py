instructions = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

tiles = [tuple([int(x) for x in line.split(",")])
         for line in instructions.split()]
max_area = 0
for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        area = (abs(tiles[i][0] - tiles[j][0]) + 1) * \
            (abs(tiles[i][1] - tiles[j][1]) + 1)
        max_area = max(area, max_area)
print(max_area)
