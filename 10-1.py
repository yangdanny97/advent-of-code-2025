instructions = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

parsed_instructions = []
for line in instructions.splitlines():
    if line.strip() == "":
        continue
    parts = line.split()
    goal = tuple([(x == "#") for x in parts[0][1:-1]])
    buttons = [{int(y) for y in x[1:-1].split(",")} for x in parts[1:-1]]
    parsed_instructions.append((goal, buttons))

total = 0

for (goal, buttons) in parsed_instructions:
    start = tuple([False for _ in goal])
    lookup = {}
    stack = [(start, 0)]

    def search(curr, step):
        for b in buttons:
            nxt = tuple([(not x if idx in b else x)
                        for idx, x in enumerate(curr)])
            if nxt not in lookup or lookup[nxt] > step + 1:
                lookup[nxt] = step + 1
                stack.append((nxt, step + 1))
    while stack:
        search(*stack.pop())
    total += lookup[goal]
print(total)
