import math
class Solution:
    def trap(self, height: list[int]) -> int:
        print(height)
        n=len(height)
        left = [-math.inf for _ in range(n)]
        right = [-math.inf for _ in range(n)]
        left[0]=height[0]
        right[n-1]=height[n-1]
        for i in range(1,n):
            left[i]=max(left[i-1],height[i])
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],height[i])

        water = 0
        for i in range(n):
            water += min(left[i],right[i]) - height[i]


        return water

height = [int(el) for el in input()[1:-1].split(',')]

print(Solution().trap(height))
