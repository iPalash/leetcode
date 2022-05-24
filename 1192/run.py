from collections import defaultdict
class Solution:
    def criticalConnections(self, n:int, connections: list[list[int]]) -> list[list[int]]:
        print(n,connections)

        conns = defaultdict(list)
        edges = dict()

        for [a,b] in connections:
            conns[a].append(b)
            conns[b].append(a)
            edges[(min(a,b),max(a,b))]=1
        #print(edges)

        rank = [n+1 for _ in range(n)]
        

        def dfs(i,curr):
            if rank[i]!=n+1:
                return rank[i]
            rank[i]=curr
            mn = curr+1

            for adj in conns[i]:
                # Skip immediately going back
                if rank[adj]==curr-1:
                    continue
                child = dfs(adj,curr+1)
                if child<=curr:
                    a,b =i,adj
                    if a>b:
                        a,b=b,a
                    del edges[(a,b)]
                mn = min(mn,child)

            return mn

        dfs(0,0)

        return [[a,b] for (a,b) in edges.keys()]

n = int(input())
connections = [[int(s) for s in el.split(',')] for el in input()[2:-2].split("],[")]

print(Solution().criticalConnections(n,connections))

