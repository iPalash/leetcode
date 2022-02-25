class Solution:
    def numDecodings(self, s:str) -> int:
        print(s)
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[-1]=1
        i=n-1
        while i>=0:
            print(i,dp)
            if (x:=int(s[i]))>0:
                #Consider 1-len
                if dp[i+1]!=0:
                    dp[i]+=dp[i+1]
                #Consider 2-len
                if i<n-1: #ignore last dig
                    if int(s[i:i+2])<27 and dp[i+2]!=0:
                        dp[i]+=dp[i+2]
            i-=1
        return dp[0]

s = input()[1:-1]

print(Solution().numDecodings(s))
