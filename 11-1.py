instructions = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

graph = {}
for line in instructions.splitlines():
    if not line.strip():
        continue
    parts = line.split()
    graph[parts[0][:-1]] = parts[1:]

paths = 0


def search(curr):
    global paths
    if curr == "out":
        paths += 1
    else:
        next = graph[curr]
        for n in next:
            search(n)


search("you")
print(paths)
