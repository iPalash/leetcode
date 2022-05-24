from random import randint as ri
class Solution:

    def __init__(self, nums:list[int]):
        self.nums = nums
        self.n = len(nums)
        self.numsbackup = nums.copy()

    def reset(self) -> list[int]:
        self.nums = self.numsbackup.copy()
        return self.nums

    def shuffle(self) -> list[int]:
        for i in range(n):
            idx = ri(i,n-1)
            self.nums[i],self.nums[idx]=self.nums[idx],nums[i]
        return self.nums
