class Solution:
    
    def util(self, nums, i, sm, path, k):
        if sm==k:
            return [path]
        if i==len(nums) or sm>k:
            return []
        ans = []
        for idx,el in enumerate(nums):
            if idx>i and nums[idx]==nums[idx-1]:
                continue
            if idx>=i:
                for el2 in self.util(nums,idx+1, sm+el, path+[el],k):
                    #print(el,el2)
                    ans.append(el2)

        return ans


    def combinationSum(self, candidates: list[int],target: int) -> list[list[int]]:
        #print(candidates,target)
        candidates.sort()
        return self.util(candidates, 0 , 0, [],target)

nums=[int(el) for el in input()[1:-1].split(",")]
k = int(input())

print(Solution().combinationSum(nums,k))

