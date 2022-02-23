class Solution:
    def rob(self, nums: list[int]) -> int:
        print(nums)
        n = len(nums)
        if n==1:
            return nums[0]
        last2w0, last1w0 = nums[0],nums[1]
        last2wL, last1wL = 0, nums[1]
        for i in range(2,n):
            if i<n-1:
                last2w0, last1w0 = last1w0, max(last1w0-nums[i-1]+nums[i],last2w0+nums[i])
                last2wL, last1wL = last1wL, max(last1wL-nums[i-1]+nums[i],last2wL+nums[i])
            else:
                last2w0, last1w0 = last1w0, max(last1w0,last2w0)
                last2wL, last1wL = last1wL, max(last1wL-nums[i-1]+nums[i], last2wL+nums[i])
                
        return max(last1w0, last2w0, last1wL, last2wL)
            


nums = [int(el) for el in input()[1:-1].split(",")]

print(Solution().rob(nums))
