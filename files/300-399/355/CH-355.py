import pandas as pd
import networkx as nx

path = "300-399/355/CH-355 Graph Calculation.xlsx"
input1 = pd.read_excel(path, usecols="B:H", skiprows=2, nrows=6)
input2 = pd.read_excel(path, usecols="K:L", skiprows=2, nrows=4)
test = pd.read_excel(path, usecols="M", skiprows=2, nrows=4)

i1 = input1.melt(id_vars=['Edge'], var_name='To', value_name='Dist').dropna()

g = nx.DiGraph()
for _, row in i1.iterrows():
    g.add_edge(row['Edge'], row['To'], weight=row['Dist'])

def define_shortest_path(g, from_node, to_node):
    try:
        shortest_path = nx.shortest_path(g, source=from_node, target=to_node, weight='weight')
        shortest_path_nodes = ",".join(shortest_path)
        return shortest_path_nodes
    except nx.NetworkXNoPath:
        return None

result = input2.copy()
result['result'] = input2.apply(lambda row: define_shortest_path(g, row['From'], row['To']), axis=1)

print(result['result'].equals(test['Shortest Path']))