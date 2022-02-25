class Solution:
    def longestCommonSubsequence(self, text1: str, text3: str) -> int:
        print(text1,text2)
        m,n = len(text1),len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=max(dp[i][j],1+dp[i-1][j-1])
        print(dp)
        return dp[m][n]

text1, text2 = input()[1:-1], input()[1:-1]

print(Solution().longestCommonSubsequence(text1,text2))

