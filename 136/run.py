from functools import reduce
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return reduce(lambda x,y:x^y,nums, 0)

if __name__=="__main__":
    a=input()
    nums = [int(el) for el in a[1:-1].split(",")]
    print(Solution().singleNumber(nums))