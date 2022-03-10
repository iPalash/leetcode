class Solution:
    def longestOnes(self, nums: list[int], k:int) -> int:
        print(nums)

        zeroes = []
        n = len(nums)

        idx = 0 
        mx = 0
        start = 0
        for i,el in enumerate(nums):
            print(i,el,start,k, zeroes)
            if el==0:
                # Zero case
                flag = True
                if k==0:
                    if len(zeroes)>0:
                        start = zeroes.pop(0)+1
                        k+=1
                    else:
                        start=i+1
                        flag=False
                if flag:
                    k-=1
                    zeroes.append(i)
                
            mx = max(i-start+1,mx)

        return mx

nums = [int(el) for el in input()[1:-1].split(",")]
k = int(input())
print(Solution().longestOnes(nums,k))
