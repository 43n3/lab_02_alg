class Graph:
    """
    Неориентированный граф.
    Представление: матрица смежности и матрица инцидентности.
    Алгоритмы обхода: DFS и BFS.
    """

    def __init__(self, vertices):
        self.vertices = vertices
        self.n = len(vertices)
        self.index = {v: i for i, v in enumerate(vertices)}
        self.edges = []
        self.adj_matrix = [[0] * self.n for _ in range(self.n)]

    def add_edge(self, v1, v2):
        """Добавить ребро между v1 и v2."""
        self.edges.append((v1, v2))
        i, j = self.index[v1], self.index[v2]
        self.adj_matrix[i][j] = 1
        self.adj_matrix[j][i] = 1

    def get_incidence_matrix(self):
        """Построить матрицу инцидентности n x m."""
        m = len(self.edges)
        inc = [[0] * m for _ in range(self.n)]
        for col, (v1, v2) in enumerate(self.edges):
            inc[self.index[v1]][col] = 1
            inc[self.index[v2]][col] = 1
        return inc

    def print_adjacency_matrix(self):
        """Вывести матрицу смежности."""
        print("\nМатрица смежности:")
        print("     " + "  ".join(str(v) for v in self.vertices))
        print("    " + "--" * self.n * 2)
        for i, v in enumerate(self.vertices):
            row = "  ".join(str(self.adj_matrix[i][j]) for j in range(self.n))
            print(f"  {v} | {row}")

    def print_incidence_matrix(self):
        """Вывести матрицу инцидентности."""
        inc = self.get_incidence_matrix()
        labels = [f"e{i+1}" for i in range(len(self.edges))]
        print("\nМатрица инцидентности:")
        print("     " + "  ".join(labels))
        print("    " + "--" * len(self.edges) * 2)
        for i, v in enumerate(self.vertices):
            row = "  ".join(str(inc[i][j]) for j in range(len(self.edges)))
            print(f"  {v} | {row}")
        print("\n  Рёбра:")
        for i, (v1, v2) in enumerate(self.edges):
            print(f"    e{i+1} = ({v1}, {v2})")

    def dfs(self, start):
        """
        Обход в глубину (DFS).
        Сложность: O(V + E)
        """
        visited = set()
        order = []

        def _dfs(v):
            visited.add(v)
            order.append(v)
            i = self.index[v]
            for j in range(self.n):
                neighbor = self.vertices[j]
                if self.adj_matrix[i][j] == 1 and neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        return order

    def bfs(self, start):
        """
        Обход в ширину (BFS).
        Сложность: O(V + E)
        """
        visited = {start}
        queue = [start]
        order = []

        while queue:
            v = queue.pop(0)
            order.append(v)
            i = self.index[v]
            for j in range(self.n):
                neighbor = self.vertices[j]
                if self.adj_matrix[i][j] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def find_connected_components(self):
        """
        Найти компоненты связности через DFS.
        Сложность: O(V + E)
        """
        visited = set()
        components = []
        for v in self.vertices:
            if v not in visited:
                component = self.dfs(v)
                components.append(component)
                visited.update(component)
        return components