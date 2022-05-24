import math.inf
class Solution:
    def minNode(self, nodes):
        mn = math.inf
        idx = -1
        for i,n in enumerate(nodes):
            if mn>self.ins[n]:
                mn=self.ins[n]
                idx = i
        return nodes[idx]

    def visit(self, node, pathLen):
        self.visited.add(node)
        for neighbours in graph[node]:


    def shortestPathLength(self, graph: list[list[int]]) -> int:
        print(graph)
        self.graph = graph
        self.n = len(graph)
        self.visited = set()
        self.ins = list(map(len,graph))
        start = minNode(list(range(n)))
        return self.visit(start, 1)


        



graph = [[int(el) for el in s.split(',')] for s in input()[2:-2].split("],[")]

print(Solution().shortestPathLength(graph))
