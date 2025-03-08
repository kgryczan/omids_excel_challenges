import pandas as pd
import networkx as nx

path = "CH-200People Connection.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=9)
test = pd.read_excel(path, usecols="E:M", skiprows=1, nrows=9)

G = nx.from_pandas_edgelist(input, source='Person 1', target='Person 2', create_using=nx.Graph())

all_people = sorted(set(input['Person 1']).union(set(input['Person 2'])))
all_com = pd.DataFrame([(a1, a2) for a1 in all_people for a2 in all_people], columns=['a1', 'a2'])

def shortest_path(a1, a2, G):
    if a1 == a2:
        return "-"
    try:
        path = nx.shortest_path(G, source=a1, target=a2)
        if len(path) <= 2:
            return "1"
        nodes_between = path[1:-1]
        return "-".join(nodes_between)
    except nx.NetworkXNoPath:
        return "1"

all_com['path'] = all_com.apply(lambda row: shortest_path(row['a1'], row['a2'], G), axis=1)
result = all_com.pivot(index='a2', columns='a1', values='path')
print(result)
print(test)