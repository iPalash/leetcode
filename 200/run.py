class Solution:
    def numIslands(self, grid:list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands=0
        #print(grid)
        visited = [[0 for el in range(n)] for _ in range(m)]
        queue = []
        for r in range(m):
            for c in range(n):
                if grid[r][c]=='1' and visited[r][c]==0:
                    queue.append((r,c))
                    islands+=1
                    while len(queue)>0:
                        (x,y)=queue.pop()
                        if visited[x][y]==0:
                            visited[x][y]=1
                            #Visit neighbours if 1:
                            if x-1>=0:
                                if grid[x-1][y]=='1' and visited[x-1][y]==0:
                                    queue.append((x-1,y))
                            if x+1<m:
                                if grid[x+1][y]=='1' and visited[x+1][y]==0:
                                    queue.append((x+1,y))
                            if y-1>=0:
                                if grid[x][y-1]=='1' and visited[x][y-1]==0:
                                    queue.append((x,y-1))
                            if y+1<n:
                                if grid[x][y+1]=='1' and visited[x][y+1]==0:
                                    queue.append((x,y+1))
        return islands



                    


        return islands

grid = [[s for s in el[1:-1].split('","')] for el in input()[2:-2].split("],[")]
print(Solution().numIslands(grid))
