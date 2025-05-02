import pandas as pd
import networkx as nx

input = pd.read_excel("CH-037 Connected people.xlsx", sheet_name="Sheet1", usecols="B:C", skiprows=1, nrows=25)
test  = pd.read_excel("CH-037 Connected people.xlsx", sheet_name="Sheet1", usecols="E:F", skiprows=1, nrows=4)

G = nx.Graph()
for _, row in input.iterrows():
    G.add_edge(row['Caller'], row['Respondant'])
subgraphs = list(nx.connected_components(G))
nodes_per_subgraph = [list(subgraph) for subgraph in subgraphs]
result = pd.DataFrame()
result['People'] = nodes_per_subgraph
result['People'] = result['People'].apply(lambda x: sorted(x))

print(result)