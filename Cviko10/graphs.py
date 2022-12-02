class GraphTraverser:

    def __init__(self, graph):
        self.graph = graph
        self.visited = []

    def dfs(self,vertex):
        self.dfs_internal(vertex)

    def dfs_internal(self, vertex):
        print(vertex)
        self.visited.append(vertex)
        for neighbour in self.graph[vertex]:
            if neighbour not in self.visited:
                self.dfs_internal(neighbour)

    def dfs_iter(self, vertex):
        self.visited = []
        stack = [vertex]
        while True:
            while vertex in self.visited:
                if len(stack) == 0:
                    return
                vertex = stack.pop(0)
            print(vertex)
            self.visited.append(vertex)
            stack = self.graph[vertex] + stack

    def bfs_iter(self, vertex):
        self.visited = []
        queue = [vertex]
        while True:
            while vertex in self.visited:
                if len(queue) == 0:
                    return
                vertex = queue.pop(0)
            print(vertex)
            self.visited.append(vertex)
            queue = queue + self.graph[vertex] + queue




g1 = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "D": ["E"],
            "E": ["A"],
            "C": ["D", "E"]
        }

graph1 = {
  "A": ["B", "D"],
  "B": ["C", "F"],
  "C": ["E", "G", "H"],
  "G": ["E", "H"],
  "E": ["B", "F"],
  "F": ["A"],
  "D": ["F"],
  "H": ["A"]
}

tree = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "D": [],
            "E": [],
            "C": []
        }

gt = GraphTraverser(graph1)
# gt.dfs("A")
# print("-------------------")
# gt.dfs_iter("A")
gt.bfs_iter("A")
