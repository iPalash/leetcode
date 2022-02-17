def binary(nums, a, i, j):
            m=(i+j)//2
            if i>j:
                return -1
            start,mid,end = nums[i], nums[m], nums[j]
            if mid==a:
                return m
            if mid<start:
                #Pivot is on left
                if end>=a and a>=mid:
                    return binary(nums,a,m+1,j)
                else:
                    return binary(nums,a,i,m-1)
                pass
            elif mid>end:
                #Pivot in on right
                if start<=a and mid>=a:
                    return binary(nums,a,i,m-1)
                else:
                    return binary(nums,a,m+1,j)
            else:
                #no pivot
                if mid>a:
                    return binary(nums,a,i,m-1)
                else:
                    return binary(nums,a,m+1,j)

def getPivot(nums):
    start,end = 0, len(nums)-1
    while start<end:
        mid=(start+end)//2
        # print(start,mid,end)
        # print(nums[start],nums[mid])
        #TODO Try reversing the condition and finding pivot
        if nums[mid]>nums[end]:
            #Pivot to right
            start=mid+1
        else:
            end=mid
    return start

class Solution:
    def search(self, nums: list[int], target:int) -> int:
        print(nums,len(nums),getPivot(nums))
        # return binary(nums,target,0,len(nums)-1)


arr=[int(el) for el in input()[1:-1].split(",")]
target =int(input())
print(Solution().search(arr, target))
