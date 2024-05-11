
class AdjacencyMatrix:
    def __init__(self, total_vertices):
        self.total_vertices = total_vertices
        self.matrix = [[0] * total_vertices for _ in range(total_vertices)]
