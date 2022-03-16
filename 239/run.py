
class Solution:
    def maxSlidingWindow(self, nums: list[int], k:int) -> int:
        print(nums,k)
        n = len(nums)
        left = 0 
        ans = []
        curr = [nums[0]]
        for i in range(1,n):
            if i-left==k:
                ans.append(curr[0])
                left+=1
                if curr[0]==nums[left-1]:
                    curr.pop(0)
            while len(curr)>0 and nums[i]>curr[-1]:
                curr.pop()
            curr.append(nums[i])
        ans.append(curr.pop(0))

        return ans

nums = [int(el) for el in input()[1:-1].split(',')]
k = int(input())

print(Solution().maxSlidingWindow(nums,k))
