import torch
import torch.nn as nn
from data_handling import Graph

class DLCBlock(nn.Module):
    """
    deep locally connected
    """
    def __init__(self, in_feats: int, out_feats: int):
        super().__init__()
        self.non_linear = nn.Sigmoid()
        self.weight = nn.Parameter(data=torch.rand(size=[out_feats, in_feats]))

    def forward(self, cluster_vertex_features: torch.Tensor):
        """
        same as (but faster):
        intermediate_results = []
        for vertex_features in cluster_vertex_features:
            intermediate_results.append(self.tanh(self.weight @ vertex_features.T))
        return torch.sum(torch.cat(intermediate_results), dim=1)

        :param cluster_vertex_features:
        :return:
        """
        return torch.sum(self.non_linear(self.weight @ cluster_vertex_features.T), dim=1)


class SpectralBlock(nn.Module):
    def __init__(self, graph: Graph, feats_out: int):
        super().__init__()
        self.feats_out  = feats_out

        num_vertices = graph.vertex_features.size(0)
        self.feats_in = graph.vertex_features.size(1)
        self.vertex_features = graph.vertex_features
        self.laplacian_mat = graph.laplacian_mat()
        self.non_linear = nn.Tanh()
        self.weight = nn.Parameter(data=torch.rand(size=[self.feats_out, self.feats_in, num_vertices]))

    def forward(self) -> torch.Tensor:
        q = torch.svd(self.laplacian_mat).U  # eigenvector matrix of laplacian
        out = []
        for f_out in range(self.feats_out):
            linear = 0
            for f_in in range(self.feats_in):
                linear += q @ torch.diag(self.weight[f_out, f_in]) @ q.T @self.vertex_features[:, f_in]
            out.append(self.non_linear(linear).unsqueeze(0))
        return torch.cat(out, dim=0)
