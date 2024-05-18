import pytest

from datastructures.non_linear_datastructures.graph.adjacency_list import AdjacencyList


class TestAdjacencyList:

    @pytest.mark.parametrize("total_vertices", [0, 10])
    def test_init(self, total_vertices):
        adj_list = AdjacencyList(total_vertices)

        assert adj_list.total_vertices == total_vertices
        assert len(adj_list.list_) == len(adj_list.list_)

    def test_add_edge(self):
        total_vertices = 5
        list_of_edges = [(0, 1), (1, 3), (2, 3), (3, 3), (3, 4), (4, 1)]

        adj_list = AdjacencyList(total_vertices)
        for edge in list_of_edges:
            adj_list.add_edge(*edge)

        assert adj_list.list_ == [[1], [0, 3, 4], [3], [1, 2, 3, 4], [3, 1]]
        assert adj_list.total_vertices == total_vertices

    def test_add_undirected_edge(self):
        total_vertices = 5
        list_of_edges = [(0, 1), (1, 3), (2, 3), (3, 3), (3, 4), (4, 1)]

        adj_list = AdjacencyList(total_vertices)
        for edge in list_of_edges:
            adj_list.add_undirected_edge(*edge)

        assert adj_list.list_ == [[1], [0, 3, 4], [3], [1, 2, 3, 4], [3, 1]]
        assert adj_list.total_vertices == total_vertices

    def test_add_directed_edge(self):
        total_vertices = 5
        list_of_edges = [(0, 1), (1, 3), (2, 3), (3, 3), (3, 4), (4, 1)]

        adj_list = AdjacencyList(total_vertices)
        for edge in list_of_edges:
            adj_list.add_directed_edge(*edge)

        assert adj_list.list_ == [[1], [3], [3], [3, 4], [1]]
        assert adj_list.total_vertices == total_vertices

    def test_remove_edge(self):
        total_vertices = 5
        list_of_edges = [(0, 1), (1, 3), (2, 3), (3, 3), (3, 4), (4, 1)]

        adj_list = AdjacencyList(total_vertices)
        for edge in list_of_edges:
            adj_list.add_directed_edge(*edge)
        adj_list.remove_edge(0, 1)
        adj_list.remove_edge(3, 4)
        adj_list.remove_edge(4, 1)

        assert adj_list.list_ == [[], [3], [3], [3], []]
        assert adj_list.total_vertices == total_vertices
