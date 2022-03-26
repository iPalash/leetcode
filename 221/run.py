class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        print(matrix)

        m = len(matrix)
        n = len(matrix[0])

        dp = [0]*(n+1)
        last = 0
        mx = 1
        for i in range(m):
            for j in range(n):
                temp = dp[j+1]
                dp[j+1]=(min(dp[j+1],dp[j],last)+1) if matrix[i][j]=='1' else 0
                last=temp
                mx = max(mx,dp[j+1])

        return mx<<1

matrix = [[el for el in row[1:-1].split('","')] for row in input()[2:-2].split("],[")]

print(Solution().maximalSquare(matrix))
