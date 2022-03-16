import math
class Solution:
    
    def trap(self, height: list[int]) -> int:
        n = len(height)
        left,right = 0,n-1
        leftMax,rightMax=height[0],height[n-1]
        water = 0
        while left<right:
            # Always move the smaller bar
            if height[left]<height[right]:
                # 2 cases either we update max or fill some water
                if height[left]<leftMax:
                    water+=leftMax-height[left]
                else:
                    leftMax=height[left]
                left+=1
            else:
                if height[right]<rightMax:
                    water+=rightMax-height[right]
                else:
                    rightMax=height[right]
                right-=1
        return water

    def trapDP(self, height: list[int]) -> int:
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
