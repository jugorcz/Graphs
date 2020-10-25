
class Graph:
    def __init__(self, vertices_num, edges_num, edges_list, is_directed):
        self.edges = edges_num
        self.vertices = vertices_num
        self.is_directed = is_directed
        self.adjacency_matrix = self.create_adjacency_matrix(edges_list)

    def create_adjacency_matrix(self, edges_list):
        matrix = [[0 for x in range(self.vertices)]
                  for y in range(self.vertices)]
        for (a, b) in edges_list:
            matrix[a][b] = 1
            if not self.is_directed:
                matrix[b][a] = 1
        return matrix

    def display_matrix(self):
        print("--ADJACENCY MATRIX--\n   ", end="")
        for i in range(self.vertices):
            print("[{}]".format(i), end="")
        print("")
        for i in range(self.vertices):
            print("[{}]".format(i), end="")
            for j in range(self.vertices):
                print(" {} ".format(self.adjacency_matrix[i][j]), end="")
            print("")


def DFS():
    print('DFS')


def main():
    edges_list = [(0, 1), (1, 2), (2, 3), (3, 0), (1, 4), (3, 4)]
    graph = Graph(5, 6, edges_list, False)
    graph.display_matrix()


if __name__ == '__main__':
    main()
