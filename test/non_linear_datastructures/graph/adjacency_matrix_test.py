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

    def test_add_edge(self):
        total_vertices = 5
        list_of_edges = [(0, 1), (1, 3), (2, 3), (3, 3), (3, 4), (4, 1)]

        adj_list = AdjacencyMatrix(total_vertices)
        for edge in list_of_edges:
            adj_list.add_edge(*edge)

        assert adj_list.matrix == [[0, 1, 0, 0, 0], [1, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 1, 1, 1], [0, 1, 0, 1, 0]]
        assert adj_list.total_vertices == total_vertices

    def test_remove_edge(self):
        total_vertices = 5
        list_of_edges = [(0, 1), (1, 3), (2, 3), (3, 3), (3, 4), (4, 1)]

        adj_list = AdjacencyMatrix(total_vertices)
        for edge in list_of_edges:
            adj_list.add_edge(*edge)
        adj_list.remove_edge(0, 1)
        adj_list.remove_edge(3, 4)
        adj_list.remove_edge(4, 1)

        assert adj_list.matrix == [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
        assert adj_list.total_vertices == total_vertices
