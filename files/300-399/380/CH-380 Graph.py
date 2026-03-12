import pandas as pd
import networkx as nx

path = "300-399/380/CH-380 Matrix Calculation.xlsx"
input_df = pd.read_excel(path, usecols="B:G", skiprows=2, nrows=5, index_col=0)
test = pd.read_excel(path, usecols="J:K", skiprows=2, nrows=5)

edges = (
    input_df.stack()
    .reset_index(name="value")
    .query("value == 1")
    [["Edge", "level_1"]]
    .rename(columns={"level_1": "to"})
)

G = nx.DiGraph()
G.add_edges_from(edges.itertuples(index=False, name=None))

result = (
    pd.DataFrame({"Factor": list(nx.topological_sort(G))})
    .reset_index(names="Rank")
    .assign(Rank=lambda df: df["Rank"] + 1)
)

print(result.equals(test))
# True