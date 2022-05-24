from collections import defaultdict,Counter
class Solution:
    def makeConnected(self, n:int, connections: list[list[int]]) -> int :
        print(n, connections)

        conns = defaultdict(list)


        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]
        self.ans = n
        def find(i):
            if i==parent[i]:
                return i
            else:
                parent[i]=find(parent[i])
                return parent[i]


        def union(self,i,j):
            pi = find(i)
            pj = find(j)
            if pi!=pj:
                self.ans-=1
                if size[pi]>=size[pj]:
                    parent[pj]=pi
                    size[pi]+=size[pj]
                else:
                    parent[pi]=pj
                    size[pj]+=size[pi]

        for [a,b] in connections:
           # print(a,b,parent)
            union(self,a,b)
          #  print("After",parent)
         #   print()
        #for i in range(n):
        #    # This is needed since we are being lazy while updating
        #    find(i)
        sets = Counter(parent)
        edgesReq = 0
        comp = 0
        for parent,nodes in sets.items():
            edgesReq += nodes-1
            comp+=1

        if len(connections)>=n-1:
            return self.ans-1

        return -1

n = int(input())

connections = [[int(el) for el in row.split(',')] for row in input()[2:-2].split('],[')]

print(Solution().makeConnected(n,connections))
