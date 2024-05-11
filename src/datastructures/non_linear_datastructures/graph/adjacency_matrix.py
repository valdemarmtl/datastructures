'''
In python we can represent the adjacency matrix as an list of lists, 
where each cell is an number either zero or one.
We can also make an edge a set of indexes for the matrix.
'''


class AdjacencyMatrix:
    def __init__(self, total_vertices):
        self.total_vertices = total_vertices
        self.matrix = [[0] * total_vertices for _ in range(total_vertices)]

    def add_edge(self, vertex1, vertex2):
        if vertex1 == vertex2:
            print("Same vertex %d and %d" % (vertex1, vertex2))
        self.matrix[vertex1][vertex2] = 1
        self.matrix[vertex2][vertex1] = 1

    def remove_edge(self, vertex1, vertex2):
        if self.matrix[vertex1][vertex2] == 0:
            print("No edge between %d and %d" % (vertex1, vertex2))
            return
        self.matrix[vertex1][vertex2] = 0
        self.matrix[vertex2][vertex1] = 0

    def print_matrix(self):
        for row in self.matrix:
            for value in row:
                print('{:4}'.format(value), end=' ')
            print()


if __name__ == '__main__':
    list_of_edges = [(0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (2, 3), (3, 3), (3, 4)]
    adjacency_matrix = AdjacencyMatrix(5)
    for edge in list_of_edges:
        adjacency_matrix.add_edge(*edge)
    adjacency_matrix.print_matrix()
