import pandas as pd
import networkx as nx

path = "CH-220 Project Critical path.xlsx"
df = pd.read_excel(path, skiprows=2, usecols="B:D", nrows=9, names=["id", "duration", "pred"])

G = nx.DiGraph()
for _, r in df.iterrows():
    G.add_node(r.id, dur=int(r.duration))
    
for _, r in df.dropna(subset=['pred']).iterrows():
    for p in map(int, str(r.pred).split(',')):
        if p not in G.nodes():
            G.add_node(p, dur=0)
        G.add_edge(p, r.id)

ES, EF = {}, {}
for n in nx.topological_sort(G):
    ES[n] = 0 if G.in_degree(n)==0 else max(EF[p] for p in G.predecessors(n))
    EF[n] = ES[n] + G.nodes[n]['dur']

project_len = max(EF.values())
LF, LS = {}, {}
for n in reversed(list(nx.topological_sort(G))):
    LF[n] = project_len if G.out_degree(n)==0 else min(LS[s] for s in G.successors(n))
    LS[n] = LF[n] - G.nodes[n]['dur']

slack = {n: LS[n] - ES[n] for n in G.nodes()}
critical_path = sorted([n for n, v in slack.items() if v == 0], key=lambda n: ES[n])

print(critical_path)
