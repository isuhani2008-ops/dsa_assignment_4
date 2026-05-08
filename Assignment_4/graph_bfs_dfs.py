# ==========================================================
# GRAPH USING ADJACENCY LIST
# ==========================================================

# Operations:
# 1. Add Edge
# 2. BFS Traversal
# 3. DFS Traversal


from collections import deque


class Graph:

    def __init__(self):
        self.graph = {}


    # ------------------------------------------------------
    # ADD EDGE
    # ------------------------------------------------------

    def add_edge(self, u, v, weight):

        if u not in self.graph:
            self.graph[u] = []

        self.graph[u].append((v, weight))


    # ------------------------------------------------------
    # BFS
    # ------------------------------------------------------

    def bfs(self, start):

        visited = set()

        queue = deque([start])

        visited.add(start)

        print("BFS Traversal:")

        while queue:

            node = queue.popleft()

            print(node, end=" ")

            for neighbor, weight in self.graph.get(node, []):

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print()


    # ------------------------------------------------------
    # DFS
    # ------------------------------------------------------

    def dfs(self, start, visited=None):

        if visited is None:
            visited = set()
            print("DFS Traversal:")

        visited.add(start)

        print(start, end=" ")

        for neighbor, weight in self.graph.get(start, []):

            if neighbor not in visited:
                self.dfs(neighbor, visited)



# ==========================================================
# DRIVER CODE
# ==========================================================

g = Graph()

# Directed weighted graph
g.add_edge('A', 'B', 2)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'D', 1)
g.add_edge('C', 'D', 3)
g.add_edge('D', 'E', 5)

print("Adjacency List:")
print(g.graph)

print()

g.bfs('A')

print()

g.dfs('A')