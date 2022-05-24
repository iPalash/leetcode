class Solution:

    def inBounds(self, m, n, i, j):
        return (0<=i<m and 0<=j<n)


    def adjacent(self, m, n, i, j):
        # m, i
        # n, j columns
        points = [[i-1,j],[i-1,j-1],[i-1,j+1],[i+1,j],[i+1,j-1],[i+1,j+1],[i,j-1],[i,j+1]]
        return filter(lambda x:self.inBounds(m,n,x[0],x[1]), points)

    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int :
        #print(grid)
        m,n = len(grid),len(grid[0])
        if grid[0][0]==0 and grid[m-1][n-1]==0:
            if m==1 and n==1:
                return 1
            queue = []
            queue.append((0,0,1))
            visited = {}
            toVisit = {}
            toVisit[0]=True 
            while len(queue)>0:
                r,c,l = queue.pop(0)
                visited[r*n+c] = True
                print(r,c,l)
                for near in self.adjacent(m,n,r,c):
                    if grid[near[0]][near[1]]==0 and near[0]==m-1 and near[1]==n-1:
                        return l+1
                    if grid[near[0]][near[1]]==0 and (near[0]*n+near[1] not in visited) and (near[0]*n + near[1] not in toVisit):
                        queue.append((near[0],near[1],l+1))
                        toVisit[near[0]*n+near[1]]=True
        return -1



grid = [[int(e) for e in l.split(',')] for l in input()[2:-2].split('],[')]
print(Solution().shortestPathBinaryMatrix(grid))
