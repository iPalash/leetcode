from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        print(matrix)
        m = len(matrix)
        n = len(matrix[0])

        visited = [[False for _ in range(n)] for _ in range(m)]
        mx = 1
        @lru_cache(maxsize=None)
        def dfs(i,j):
            l = 1
            for [x,y] in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
                if 0<=x<m and 0<=y<n and matrix[x][y]>matrix[i][j]:
                    l = max(l,dfs(x,y)+1)
            return l
        for i in range(m):
            for j in range(n):
                mx= max(mx,dfs(i,j))

        return mx

matrix=[[int(el) for el in row.split(',')] for row in input()[2:-2].split('],[')]

print(Solution().longestIncreasingPath(matrix))
