import math
class Solution:
    def jump(self, nums:int)->int:
        print(nums)
        n = len(nums)
        if n==1:
            return 0
        i = 0
        jump = 0
        j = 0
        j_end = 0
        while i<n-1:
            j_end = max(j_end,i+nums[i])
            if i==j:
                jump+=1
                j = j_end
            i+=1
        return jump



nums = [int(el) for el in input()[1:-1].split(",")]

print(Solution().jump(nums))
