import math
class Solution:
	def minSubArrayLen(self, target:int, nums:list[int]) -> int:
		# print(target,nums)
		i,j=0,0
		n=len(nums)
		mn=math.inf
		sm=0
		while j<n:
			sm+=nums[j]

			if sm<target:
				j+=1
			else:
				# print(i,j,sm)
				mn = min(mn, j-i+1)
				sm-=nums[i]
				i+=1
				j=max(j,i)
				if j<n:
					sm-=nums[j]
		return mn if mn!=math.inf else 0
target = int(input())
nums = [int(el) for el in input()[1:-1].split(",")]
print(Solution().minSubArrayLen(target,nums))