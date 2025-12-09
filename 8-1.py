instructions = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

N_CONNECTIONS = 10

circuits = {}
for idx, line in enumerate(instructions.split()):
    circuits[idx + 1] = tuple([int(x) for x in line.split(",")])

distances = []
items = list(circuits.items())

for i in range(len(items)):
    circuit, (x, y, z) = items[i]
    for j in range(i + 1, len(items)):
        circuit2, (x2, y2, z2) = items[j]
        if circuit == circuit2:
            continue
        distance = (x - x2) ** 2 + (y - y2) ** 2 + (z - z2) ** 2
        distances.append((circuit, circuit2, distance))

sorted_distances = sorted(distances, key=lambda x: x[2])
sorted_distances = sorted_distances[:N_CONNECTIONS]

n = 0
id_to_group = {}
group_to_id = {}
for c1, c2, _ in sorted_distances:
    if c1 in id_to_group and c2 in id_to_group:
        c1_g = id_to_group[c1]
        c2_g = id_to_group[c2]
        if c1_g == c2_g:
            continue
        for c in group_to_id[c2_g]:
            id_to_group[c] = c1_g
        group_to_id[c1_g] = group_to_id[c1_g].union(group_to_id[c2_g])
        del group_to_id[c2_g]
    elif c1 in id_to_group:
        id_to_group[c2] = id_to_group[c1]
        group_to_id[id_to_group[c1]].add(c2)
    elif c2 in id_to_group:
        id_to_group[c1] = id_to_group[c2]
        group_to_id[id_to_group[c2]].add(c1)
    else:
        id_to_group[c1] = n
        id_to_group[c2] = n
        group_to_id[n] = {c1, c2}
        n += 1

group_sizes = sorted([len(n) for n in group_to_id.values()], reverse=True)
print(group_sizes[0] * group_sizes[1] * group_sizes[2])
