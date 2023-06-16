import torch

from data_handling import GraphClusters
from modules import DLCBlock, SpectralBlock

# create the graph and its clusters
vertex_features = torch.tensor(
    [[2., 1],
     [2, -3],
     [-2, -2],
     [-3, -3]])
adjacency_mat = torch.tensor(
    [[0., 1, 1, 0],
     [1, 0, 1, 0],
     [1, 1, 0, 1],
     [0, 0, 1, 0]])

graph_clusters = GraphClusters(
    adjacency_mat=adjacency_mat,
    vertex_features=vertex_features,
    clusters_members=[[0, 1], [2, 3]])


# deep locally connected network
vertex_features_cluster_1 = graph_clusters.clusters[0].vertex_features
vertex_features_cluster_2 = graph_clusters.clusters[1].vertex_features
dlc_block = DLCBlock(in_feats=2, out_feats=3)
print(dlc_block.forward(cluster_vertex_features=vertex_features_cluster_1))
print(dlc_block.forward(cluster_vertex_features=vertex_features_cluster_2))


# spectral network
spectral_block = SpectralBlock(graph=graph_clusters.graph, feats_out=3)
print(spectral_block())
