class Solution:
    def rob(self, nums: list[int]) -> int:
        print(nums)
        if len(nums)==1:
            return nums[0]
        last2, last1 = nums[0],nums[1]
        for i in range(2,len(nums)):
            curr = max(last1-nums[i-1]+nums[i],last2+nums[i])
            last2,last1=last1,curr
        return max(last1,last2)
            


nums = [int(el) for el in input()[1:-1].split(",")]

print(Solution().rob(nums))
