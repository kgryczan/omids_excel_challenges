import pandas as pd
import numpy as np
import networkx as nx
import itertools
import matplotlib.pyplot as plt

input_df = pd.read_excel("files/CH-028 Cluster values.xlsx", usecols="B", skiprows=0, nrows=15)
test_df = pd.read_excel("files/CH-028 Cluster values.xlsx", usecols="E:F", skiprows=1, nrows=4)
test_df['Values'] = test_df['Values'].apply(lambda x: ','.join(map(str, sorted(map(int, x.split(','))))))
test = test_df['Values'].explode().tolist()

edges = input_df['Question Tables'].apply(lambda x: list(map(str.strip, x.split(',')))).explode().dropna()
combinations = edges.groupby(level=0).apply(lambda x: list(itertools.combinations(x, 2))).explode().tolist()
G = nx.Graph()
G.add_edges_from(combinations)
subgraphs = [sorted(map(str, sorted(map(int, x))), key=int) for x in nx.connected_components(G)]
subgraphs = [','.join(x) for x in subgraphs]

print(all(x in test for x in subgraphs)) # True
