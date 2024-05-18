import pytest

from datastructures.non_linear_datastructures.graph.adjacency_matrix import AdjacencyMatrix


class TestAdjacencyMatrix:
    @pytest.mark.parametrize("total_vertices", [0, 10])
    def test_init(self, total_vertices):
        adj_matrix = AdjacencyMatrix(total_vertices)
        assert adj_matrix.total_vertices == total_vertices
        assert len(adj_matrix.matrix) == total_vertices
        if total_vertices > 0:
            assert len(adj_matrix.matrix[0]) == total_vertices
        else:
            assert adj_matrix.matrix == []
