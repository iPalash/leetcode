class Solution:

    def dfs(self, graph, n, c, path, d):
        if c==n-1:
            d.append(path)
        for nxt in graph[c]:
            if nxt!=-1:
                self.dfs(graph,n,nxt,path+[nxt], d)


    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        print(graph)
        n = len(graph)
        paths = []
        self.dfs(graph,n,0,[0],paths)
        return paths



def intEmpty(el):
    try:
        return int(el)
    except:
        return -1

graph = [ [intEmpty(el) for el in s.split(',')] for s in input()[2:-2].split('],[')]

print(Solution().allPathsSourceTarget(graph))
