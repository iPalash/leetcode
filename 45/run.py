import math
class Solution:
    def jump(self, nums:int)->int:
        print(nums)
        n = len(nums)
        if n==1:
            return 0
        i = 0
        jump = 0
        j = -1
        j_end = -1
        while i<n:
            jump+=1
            if i+nums[i]>=n-1:
                break
            if j==-1:
                j = i+1
            else:
                j = j_end
            j_end =i+nums[i]

            j_final = -1
            mx = -math.inf
            while j<j_end+1:
                if nums[j]!=0 and j+nums[j]>mx:
                    mx = j+nums[j]
                    j_final = j
                j+=1
            print("jump from {} to {}".format(i,j_final))
            i=j_final
        return jump



nums = [int(el) for el in input()[1:-1].split(",")]

print(Solution().jump(nums))
