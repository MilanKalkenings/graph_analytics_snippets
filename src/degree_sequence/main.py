"""
import sys
import subprocess

subprocess.check_call([sys.executable, "-m", "pip", "install", "networkx"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
"""

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

monitoring_path = "../monitoring"
data_path = "../data"

# 1.
G = nx.karate_club_graph()
nx.draw_circular(G, with_labels=True)
plt.savefig(monitoring_path + "/karate")
print(G.degree())
# -> (vertex_nr, vertex_degree)


# 2.
degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
plt.plot(degree_sequence, "b-", marker="o")
plt.savefig(monitoring_path + "/degree_sequence")
# as expected, decreasing (non strictly monotonically)

# 3.
plt.clf()
H = nx.erdos_renyi_graph(len(G.nodes()), nx.density(G))
degree_sequence = sorted((d for n, d in H.degree()), reverse=True)
plt.plot(degree_sequence, "b-", marker="o")
plt.savefig(monitoring_path + "/degree_sequence2")
# -> same amount of vertices and same density, but different degree sequence

# 4.
facebook = pd.read_csv(data_path + "/facebook_combined.txt",
                       sep=" ",
                       names=["start_node", "end_node"])
G = nx.from_pandas_edgelist(facebook, "start_node", "end_node")

degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
plt.plot(degree_sequence, "b-", marker="o")
plt.savefig(monitoring_path + "/degree_sequence_karate")
# few with very many connections, many with very few connections, highly skewed

plt.clf()
H = nx.erdos_renyi_graph(len(G.nodes()), nx.density(G))
degree_sequence = sorted((d for n, d in H.degree()), reverse=True)
plt.plot(degree_sequence, "b-", marker="o")
plt.savefig(monitoring_path + "/degree_sequence_karate2")
# -> normal distribution (few with very many and few with very few connections, many with around mean connections
