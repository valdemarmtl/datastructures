

class AdjacencyList:
    def __init__(self, total_vertices: int):
        self.total_vertices = total_vertices
        self.list_ = [[] for _ in range(total_vertices)]

    def add_edge(self, vertex1: int, vertex2: int):
        self.add_undirected_edge(vertex1, vertex2)

    def add_directed_edge(self, vertex1: int, vertex2: int):
        try:
            self.list_[vertex1].index(vertex2)
            print("Edge (%d,%d) is already present" % (vertex1, vertex2))
        except ValueError:
            self.list_[vertex1].append(vertex2)

    def add_undirected_edge(self, vertex1: int, vertex2: int):
        self.add_directed_edge(vertex1, vertex2)
        self.add_directed_edge(vertex2, vertex1)

    def remove_edge(self, vertex1: int, vertex2: int):
        try:
            self.list_[vertex1].remove(vertex2)
        except ValueError:
            print("No edge between %d and %d" % (vertex1, vertex2))

    def display(self):
        for vertex in range(self.total_vertices):
            print(vertex, end=' -> ')
            for neighbor in self.list_[vertex]:
                print(neighbor, end=' ')
            print()

