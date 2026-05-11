import networkx as nx

used = {"a2", "a5", "c2"}
cols = "abcdefgh"

def diag(s):
    c, r = cols.index(s[0]) + 1, int(s[1])
    return f"L{c+r}", f"R{c-r}"

busy = set().union(*(diag(s) for s in used))

board = [f"{c}{r}" for c in cols for r in range(1, 9)]
free = [s for s in board if s not in used and set(diag(s)).isdisjoint(busy)]

G = nx.Graph()
left = set()

for s in free:
    a, b = diag(s)
    left.add(a)
    G.add_edge(a, b, pos=s)

m = nx.bipartite.maximum_matching(G, top_nodes=left)

add = [
    G[a][b]["pos"]
    for a, b in m.items()
    if a in left
]

result = sorted(used | set(add), key=lambda x: (cols.index(x[0]), int(x[1])))

result