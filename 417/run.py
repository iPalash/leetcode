class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
            print(heights)

            m = len(heights)
            n = len(heights[0])

            pac = [[0 for _ in range(n)] for _ in range(m)]

            # Reachable by top and left sides
            q = []
            for i in range(m):
                pac[i][0]=1
                q.append((i,0))
            for j in range(n):
                pac[0][j]=1
                q.append((0,j))

            # Bfs for mark all reachable

            def bfs(visited, q):
                while len(q)>0:
                    a,b = q.pop()
                    neighbours = [(a-1,b),(a+1,b),(a,b-1),(a,b+1)]
                    for (x,y) in neighbours:
                        if 0<=x<m and 0<=y<n and visited[x][y]==0 and heights[a][b]<=heights[x][y]:
                            visited[x][y]=1
                            q.append((x,y))
            bfs(pac,q)


            atl = [[0 for _ in range(n)] for _ in range(m)]

            #Reachable by bot and right sides

            q = []
            for i in range(m):
                atl[i][n-1]=1
                q.append((i,n-1))
            for j in range(n):
                atl[m-1][j]=1
                q.append((m-1,j))
            

            bfs(atl,q)

            ans = []

            for i in range(m):
                for j in range(n):
                    if atl[i][j]==pac[i][j]==1:
                        ans.append([i,j])

                

            return ans

heights = [[int(el) for el in row.split(',')] for row in input()[2:-2].split('],[')]

print(Solution().pacificAtlanctic(heights))

