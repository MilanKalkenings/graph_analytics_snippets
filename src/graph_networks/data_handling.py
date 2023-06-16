from typing import List
import torch


class Graph:
    def __init__(self, vertex_features: torch.Tensor, adjacency_mat: torch.Tensor):
        self.vertex_features = vertex_features
        self.adjacency_mat = adjacency_mat

    def degree_mat(self):
        return torch.diag(torch.sum(self.adjacency_mat, dim=1))

    def laplacian_mat(self) -> torch.Tensor:
        return self.degree_mat() - self.adjacency_mat


class GraphClusters:
    def __init__(self,
                 adjacency_mat: torch.Tensor,
                 vertex_features: torch.Tensor,
                 clusters_members: List[List[int]]):
        self.graph = Graph(adjacency_mat=adjacency_mat, vertex_features=vertex_features)
        clusters = []
        for cluster_members in clusters_members:
            clusters.append(self.create_subgraph(cluster_members=cluster_members))
        self.clusters = clusters

    def create_subgraph(self, cluster_members: List[int]) -> Graph:
        vertex_feats = self.graph.vertex_features[cluster_members]
        adj_mat = self.graph.adjacency_mat[cluster_members][:, cluster_members]
        return Graph(vertex_features=vertex_feats, adjacency_mat=adj_mat)
