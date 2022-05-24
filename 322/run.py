import math
class Solution:
    def coinChange(self, coins: list[int], amount:int) -> int:
        print(coins, amount)
        coins.sort()
        dp = [math.inf]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin>=0 and dp[i-coin]!=math.inf:
                    dp[i]=min(dp[i-coin]+1,dp[i])
        return dp[amount] if dp[amount]!=math.inf else -1

coins = [int(el) for el in input()[1:-1].split(",")]
amount = int(input())

print(Solution().coinChange(coins, amount))
