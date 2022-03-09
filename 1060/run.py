class Solution:
    def missingNumsLeft(self, i, mid):
        return self.nums[mid]-self.nums[i] - mid + i
    def binary(self, i, j, k):
        mid = (i+j)//2
        if i==mid:
            return (i,k)
        miss = self.missingNumsLeft(i,mid)

        if miss>=k:
            # Look into left side for kth missing
            return self.binary(i,mid,k)
        else:
            # Look into right for (k-miss)th missing
            return self.binary(mid,j,k-miss)

    def missingElement(self, nums: list[int], k:int) -> int:
        print(nums,k)
        self.nums = nums

        (el,k) = self.binary(0,len(nums),k)
        print(el,k)
        return nums[el]+k

nums = [int(el) for el in input()[1:-1].split(",")]
k = int(input())

print(Solution().missingElement(nums,k))
