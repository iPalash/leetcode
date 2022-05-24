from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        print(matrix)
        m = len(matrix)
        n = len(matrix[0])

        # preprocess to find topo ordering to solve via dp

        # dp relation is dp[curr]= 1 + max(dp[neighbor]) for neighbor<curr

        ins = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for [a,b] in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
                    if 0<=a<m and 0<=b<n and matrix[a][b]<matrix[i][j]:
                        ins[i][j]+=1
        q = []
        for i in range(m):
            for j in range(n):
                if ins[i][j]==0:
                    q.append([i,j,1])
        mx = 1
        while len(q)>0:
            [i,j,l]=q.pop(0)
            mx = max(mx,l)
            for [a,b] in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
                if 0<=a<m and 0<=b<n and matrix[a][b]>matrix[i][j]:
                    ins[a][b]-=1
                    if ins[a][b]==0:
                        q.append([a,b,l+1])
        return mx


 



matrix=[[int(el) for el in row.split(',')] for row in input()[2:-2].split('],[')]

print(Solution().longestIncreasingPath(matrix))
