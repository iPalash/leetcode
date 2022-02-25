class Solution:

    def binaryLeft(self, nums, i, j, target):
        if i==j:
            return i
        mid = (i+j)//2
        if nums[mid]>=target:
            return self.binaryLeft(nums, i,mid,target)
        else:
            return self.binaryLeft(nums,mid+1,j,target)

    def lengthOfLIS(self, nums: list[int]) -> int:
        print(nums)
        n = len(nums)
        
        arr = [nums[0]]
        for i in range(1,n):
            if arr[-1]<nums[i]:
                arr.append(nums[i])
            else:
                idx = self.binaryLeft(arr, 0, len(arr), nums[i])
                print(idx,nums[i],arr)
                arr[idx]=nums[i]
        print(arr)
        return len(arr)

nums = [int(el) for el in input()[1:-1].split(",")]

print(Solution().lengthOfLIS(nums))
