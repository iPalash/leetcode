class Solution:
    
    def util(self, nums, i, sm, path, k):
        if sm==k:
            return [path]
        if i==len(nums) or sm>k:
            return []
        ans = []
        for idx,el in enumerate(nums):
            if idx>=i:
                for el in self.util(nums,idx,sm+el, path+[el], k):
                    ans.append(el)
        return ans


    def combinationSum(self, candidates: list[int],target: int) -> list[list[int]]:
        #print(candidates,target)
        return self.util(candidates, 0, 0, [],target)

nums=[int(el) for el in input()[1:-1].split(",")]
k = int(input())

print(Solution().combinationSum(nums,k))

