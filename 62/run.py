class Solution:
    def uniquePaths(self, m: int, n:int) -> int:
        prv = [0 for _ in range(n+1)]
        curr = [0 for _ in range(n+1)]
        curr[-2]=1
        for x in range(m-1,-1,-1):
            for y in range(n-1,-1,-1):
                if x==m-1 and y==n-1:
                    continue
                curr[y]=curr[y+1]+prv[y]
            #print(prv,curr)
            prv = [el for el in curr]
        return curr[0]

m = int(input())
n = int(input())

print(Solution().uniquePaths(m,n))

