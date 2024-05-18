import pytest

from datastructures.non_linear_datastructures.graph.adjacency_list import AdjacencyList


class TestAdjacencyList:

    @pytest.mark.parametrize("total_vertices", [0, 10])
    def test_init(self, total_vertices):
        adj_list = AdjacencyList(total_vertices)
        assert adj_list.total_vertices == total_vertices
        assert len(adj_list.list_) == len(adj_list.list_)

