class Solution:
    def binaryLeft(self, nums, i, j, target, arr):
        if i==j:
            return i
        mid = (i+j)//2
        if arr[nums[mid]]>=target:
            return self.binaryLeft(nums, i,mid,target, arr)
        else:
            return self.binaryLeft(nums,mid+1,j,target,arr)

    def findNumberOfLIS(self, nums: list[int]) -> int:
        print(nums)
        n = len(nums)
        
        arr2 = [[0]]
        for i in range(1,n):
            arr2_=set()
            for cnt,arr in enumerate(arr2):
                #print(arr)
                idx = self.binaryLeft(arr, 0, len(arr), nums[i], nums)
                if nums[i]>nums[arr[-1]]:
                    arr.append(i)
                    arr2_.add(":".join(map(str,arr)))
                else:
                    arrT = arr.copy()
                    arr[idx]=i
                    arr2_.add(":".join(map(str,arr)))
                    arr2_.add(":".join(map(str,arrT)))
                #print(arr,i,idx,nums[i])
            arr2=[[int(el) for el in s] for s in map(lambda x:x.split(":"),arr2_)]
        l = max(map(len,arr2))

        arr2 = list(filter(lambda x:len(x)==l, arr2))
        arr2 = list(filter(lambda x:x==sorted(x), arr2))
        #print(arr2)
        return len(arr2)

nums = [int(el) for el in input()[1:-1].split(",")]

print(Solution().findNumberOfLIS(nums))
