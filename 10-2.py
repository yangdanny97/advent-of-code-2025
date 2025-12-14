from ortools.linear_solver.pywraplp import Solver
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
    goal = tuple([int(x) for x in parts[-1][1:-1].split(",")])
    buttons = [{int(y) for y in x[1:-1].split(",")} for x in parts[1:-1]]
    parsed_instructions.append((goal, buttons))

total = 0

# https://mlabonne.github.io/blog/posts/2022-03-02-Linear_Programming.html
for (goal, buttons) in parsed_instructions:
    solver = Solver('Minimize button presses', Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    vars = [solver.IntVar(0, solver.infinity(), str(idx)) for idx, _ in enumerate(buttons)]
    counters_to_buttons = [[] for _ in goal]
    for b_idx, counters in enumerate(buttons):
        for counter in counters:
            counters_to_buttons[counter].append(b_idx)
    for counter, bs in enumerate(counters_to_buttons):
        solver.Add(sum([vars[b] for b in bs]) == goal[counter])
    solver.Minimize(sum(vars))
    status = solver.Solve()
    assert status == Solver.OPTIMAL
    total += solver.Objective().Value()
print(total)
