import math
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        print(grid)

        m = len(grid)
        n = len(grid[0])
        
        costMem = [[math.inf for _ in range(n)] for _ in range(m)]

        costMem[m-1][n-1]=0
        q = [(m-1,n-1)]

        while len(q)>0:
            (i,j)=q.pop(0)
            neighbours = [(i,j-1),(i,j+1),(i-1,j),(i+1,j)]
            for idx,(x,y) in enumerate(neighbours):
                if 0<=x<m and 0<=y<n:
                    cst = costMem[i][j] + (0 if idx+1==grid[x][y] else 1)
                    if costMem[x][y]>cst:
                        if cst>costMem[i][j]:
                            q.append((x,y))
                        else:
                            q.insert(0,(x,y))
                        costMem[x][y]=cst
        return costMem[0][0]

grid = [[int(e) for e in l.split(',')] for l in input()[2:-2].split('],[')]
# 1 - right, 2 - left, 3 - down, 4 - up
print(Solution().minCost(grid))
