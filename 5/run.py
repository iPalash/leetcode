class Solution:
    def longestPalindrome(self, s:str) -> str:
        #print(s)
        n = len(s)
        if n==1:
            return s
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans = ""
        for i in range(n):
            dp[i][i]=True
            if ans=="":
                ans=s[i]
            if i<n-1:
                dp[i][i+1]=(s[i]==s[i+1])
                if dp[i][i+1]:
                    ans=s[i:i+2]
        for k in range(2,n):
            for i in range(n-1):
                if i+k<n:
                    #print(i,i+k)
                    if s[i]==s[i+k]:
                        if dp[i+1][i+k-1]:
                            dp[i][i+k]=True
                            if len(ans)<k+1:
                                ans = s[i:i+k+1]
        return ans

s = input()[1:-1]

print(Solution().longestPalindrome(s))
