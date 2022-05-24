class Solution:
    def findMin(self, nums: list[int]) -> int:
        print(nums)
        s,e = 0,len(nums)-1
        while s<e:
            mid = (s+e)//2
            f,b,l = nums[s],nums[mid],nums[e]
            print("idx:",s,mid,e)
            print("elements:",f,b,l)
            if b>l:
                s=mid+1
            else:
                e=mid
        return nums[s]
# input is [3,4,5,1,2]
nums = [int(el) for el in input()[1:-1].split(',')]
print(Solution().findMin(nums))
