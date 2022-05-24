class Solution:
    def util(self, nums: list[int]) -> list[list[int]]:
        if len(nums)==1:
            return [nums]
        ans = []
        d = {}
        for i,el in enumerate(nums):
            u = nums[:i]+nums[i+1:]
            if i>0 and el==nums[i-1]:
                continue
            for arr in self.util(u):
                ans.append(arr+[el])
        return ans

    def permuteUnique(self,nums: list[int]) -> list[list[int]]:
        nums.sort()
        return self.util(nums)


nums = [int(el) for el in input()[1:-1].split(',')]
print(Solution().permuteUnique(nums))
