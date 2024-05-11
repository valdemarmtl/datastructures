

class AdjacencyList:
    def __init__(self, total_vertices: int):
        self.total_vertices = total_vertices
        self.list_ = [[] for _ in range(total_vertices)]
