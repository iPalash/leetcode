class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        print(nums)
        nums.sort()
        n = len(nums)
        sets = {}
        ans = []
        for i in range(1<<n):
            el = []
            el2 = []
            for j in range(n):
                if (i>>j)&1:
                    el.append(nums[j])
                    el2.append(str(nums[j]))
            if (x:=":".join(el2)) not in sets:
                sets[x]=1
                ans.append(el)
        return ans






nums = [int(el) for el in input()[1:-1].split(',')]
print(Solution().subsetsWithDup(nums))
