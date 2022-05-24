class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        print(nums,target,n)
        def binaryL(nums, target, i,j):
            mid = (i+j)//2
            # print(i,j,mid)
            if i>j:
                    return i
            if nums[mid]>=target:
                return binaryL(nums,target,i,mid-1)
            else:
                return binaryL(nums,target,mid+1,j)
        def binaryR(nums, target, i,j):
            mid = (i+j)//2
            # print(i,j,mid)
            if i>j:
                return j
            if nums[mid]<=target:
                return binaryR(nums,target,mid+1,j)
            else:
                return binaryR(nums,target,i,mid-1)
        # print(binaryR(nums,target,0,n-1))
        # return
        return [a,b] if (a:=binaryL(nums,target,0,n-1))<=(b:=binaryR(nums,target,0,n-1)) else [-1,-1]

arr=[int(el) for el in input()[1:-1].split(",")]
target =int(input())
print(Solution().searchRange(arr, target))
