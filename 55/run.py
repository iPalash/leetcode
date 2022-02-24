class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        j = n-1
        for i in range(n-2, -1,-1):
            if i+nums[i]>=j:
                j = i
        return j==0

nums = [int(el) for el in input()[1:-1].split(",")]

print(Solution().canJump(nums))
