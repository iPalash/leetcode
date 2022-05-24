import math
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        print(prices)
        n = len(prices)

        mp = [0 for _ in range(n+2)]

        for i in range(n-1,-1,-1):
            # buy and sell stock at i
            
            buy = prices[i]

            one = 0

            for j in range(i,n):
                prof = prices[j]-buy + mp[j+2]
                one = max(one,prof)

            # do nothing

            two = mp[i+1]
            
            mp[i] = max(one,two)
        return mp[0]



prices = [int(el) for el in input()[1:-1].split(",")]
print(Solution().maxProfit(prices))
