
class AdjacencyMatrix:
    def __init__(self, total_vertices):
        self.total_vertices = total_vertices
        self.matrix = [[0] * total_vertices for _ in range(total_vertices)]

    def add_edge(self, vertex1, vertex2):
        if vertex1 == vertex2:
            print("Same vertex %d and %d" % (vertex1, vertex2))
        self.matrix[vertex1][vertex2] = 1
        self.matrix[vertex2][vertex1] = 1

