class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        print(nums)
        n = len(nums)
        dp = [1 for _ in range(n)]

        for j in range(1,n):
            for i in range(0,j):
                if nums[j]>nums[i]:
                    dp[j]=max(dp[j],dp[i]+1)
        return max(dp)

nums = [int(el) for el in input()[1:-1].split(",")]

print(Solution().lengthOfLIS(nums))
