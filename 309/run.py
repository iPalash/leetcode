import math
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        print(prices)
        n = len(prices)

        buy = [-math.inf for _ in range(n+1)]
        sell = [-math.inf for _ in range(n+1)]
        rest = [-math.inf for _ in range(n+1)]

        buy[0]=-math.inf
        sell[0]=-math.inf
        rest[0]=0

        

        for i,price in enumerate(prices):
            i+=1
            buy[i]= max(buy[i-1],rest[i-1]-price)
            sell[i] = max(sell[i-1],buy[i-1]+price)
            rest[i]=max(buy[i-1],rest[i-1],sell[i-1])

        return max(sell[n],rest[n])


prices = [int(el) for el in input()[1:-1].split(",")]
print(Solution().maxProfit(prices))
