import math
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        print(nums)
        start , end = 0,(n:=len(nums))
        while start<end:
            mid = (start+end)//2
            first = -math.inf
            if mid-1>=0:
                first = nums[mid-1]
            last = -math.inf
            if mid+1<n:
                last = nums[mid+1]
            print("idx:",start,end,mid)
            middle = nums[mid]
            print("elements:",first,middle,last)
            # if first<=middle>=last:
            #     return mid
            if first>middle:
                end = mid
            else:
                start = mid+1
        return start    

#[1,2,3,1]
nums = [int(el) for el in input()[1:-1].split(",")]
print(Solution().findPeakElement(nums))
