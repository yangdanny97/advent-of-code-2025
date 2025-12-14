instructions = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

graph = {}
for line in instructions.splitlines():
    if not line.strip():
        continue
    parts = line.split()
    graph[parts[0][:-1]] = parts[1:]

predecessors = {g: [] for g in graph}
predecessors["out"] = []
for g, succ in graph.items():
    for s in succ:
        predecessors[s].append(g)

cache = {}


def search(curr):
    global cache
    if curr in cache:
        return cache[curr]
    if curr == "svr":
        return (1, 0, 0, 0)
    n = 0
    n_with_dac = 0
    n_with_fft = 0
    n_with_dac_fft = 0
    for pred in predecessors[curr]:
        (p, p_with_dac, p_with_fft, p_with_dac_fft) = search(pred)
        if curr == "dac":
            assert p_with_dac == 0
            assert p_with_dac_fft == 0
            n_with_dac += p
            n_with_dac_fft += p_with_fft
        elif curr == "fft":
            assert p_with_fft == 0
            assert p_with_dac_fft == 0
            n_with_fft += p
            n_with_dac_fft += p_with_dac
        else:
            n += p
            n_with_dac += p_with_dac
            n_with_fft += p_with_fft
            n_with_dac_fft += p_with_dac_fft
    result = (n, n_with_dac, n_with_fft, n_with_dac_fft)
    cache[curr] = result
    return result


search("out")
print(cache["out"][-1])
