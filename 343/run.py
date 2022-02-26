import math

pow = lambda a,b : int(math.pow(a,b))

class Solution:
    def integerBreak(self, n:int) -> int:
        print(n)
        div3 = n//3
        mod3 = n%3
        if mod3==0:
            return pow(3,div3)
        elif mod3==1:
            return pow(3,div3-2)<<2
        else:
            return pow(3,div3)<<1


n = int(input())

print(Solution().integerBreak(n))
