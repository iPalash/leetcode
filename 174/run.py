import math
class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        print(dungeon)

        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[math.inf,math.inf] for _ in range(n)]

        start = 1
        if (val:=dungeon[m-1][n-1])<0:
            start = 1-val
        dp[n-1]=[start,start]

        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                curr = dungeon[r][c]
                if r==m-1 and c==n-1:
                    continue
                if r==m-1: #last row, all down will be inf,so leave them be
                    pass
                else:
                    # do something for calculting value needed for next down move
                    down = min(dp[c])
                    if curr>=down:
                        dp[c][0]=1
                    else:
                        dp[c][0]=down-curr

                if c==n-1: #last column, all right will be inf, so leave them be
                    dp[c][1]=math.inf
                else:
                    # do something for right
                    right = min(dp[c+1])
                    if curr>=right:
                        dp[c][1]=1
                    else:
                        dp[c][1]=right-curr

        return min(dp[0])

dungeon = [[int(el) for el in row.split(',')] for row in input()[2:-2].split('],[')]

print(Solution().calculateMininumHP(dungeon))


