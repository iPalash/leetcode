import math
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        print(prices)
        n = len(prices)
        b1 = -math.inf
        s1 = 0 
        b2 = -math.inf
        s2 = 0
        
        for i,p in enumerate(prices):
            b1,s1,b2,s2 = max(b1,-p),max(s1,p+b1),max(b2,-p+s1),max(s2,p+b2)
            

        return max(s1,s2)

prices = [int(el) for el in input()[1:-1].split(',')]

print(Solution().maxProfit(prices))
