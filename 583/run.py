class Solution:
    def minDistance(self, t1,t2) -> int:
        return len(t1)+len(t2)-2*self.longestCommonSubsequence(t1,t2)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        print(text1,text2)
        m,n = len(text1),len(text2)
        if m<n: #ensuring text2 is smaller
            m,n=n,m
            text1,text2=text2,text1

        prv = [0 for _ in range(n+1)]
        curr = [0 for _ in range(n+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                curr[j]=max(prv[j],curr[j-1])
                if text1[i-1]==text2[j-1]:
                    curr[j]=1+prv[j-1]
            prv,curr=curr,prv #have to prv to curr but the other way to it to just reset curr
        return prv[n]

text1, text2 = input()[1:-1], input()[1:-1]

print(Solution().minDistance(text1,text2))

