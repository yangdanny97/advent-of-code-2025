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
        ix, iy = tiles[i]
        jx, jy = tiles[j]
        area = (abs(ix - jx) + 1) * (abs(iy - jy) + 1)
        if area <= max_area:
            continue
        left, right = min(ix, jx), max(ix, jx)
        bottom, top = min(iy, jy), max(iy, jy)

        def check_intersection(k):
            kx, ky = tiles[k % len(tiles)]
            lx, ly = tiles[(k + 1) % len(tiles)]
            if kx == lx:
                if kx <= left or kx >= right:
                    return True
                min_y, max_y = min(ky, ly), max(ky, ly)
                if min_y < top and max_y >= top:
                    return False
                elif min_y <= bottom and max_y > bottom:
                    return False
                else:
                    return True
            elif ky == ly:
                if ky <= bottom or ky >= top:
                    return True
                min_x, max_x = min(kx, lx), max(kx, lx)
                if min_x < right and max_x >= right:
                    return False
                elif min_x <= left and max_x > left:
                    return False
                else:
                    return True
            assert False
        ok = True
        for k in range(i + 1, j):
            if not check_intersection(k):
                ok = False
                break
        if not ok:
            continue
        for k in range(j + 1, j + (len(tiles) + i - j - 1)):
            if not check_intersection(k):
                ok = False
                break
        if not ok:
            continue
        max_area = area
print(max_area)
