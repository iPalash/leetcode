def binary(nums, i, j, el):
		mid = (i+j)//2
		if i==j:
			return mid
		if nums[mid]<el:
			return binary(nums,mid+1,j,el)
		else:
			return binary(nums,i,mid,el)


class Solution:
	def findOriginalArray(self, nums: list[int]) -> list[int]:
		nums.sort()
		n=len(nums)
		marked = {}
		ans = []
		if n%2==1:
			return []
		for i,num in enumerate(nums):
			# print(i,num)
			if i not in marked:
				# print("unmarked")
				marked[i]=1
				double = num<<1
				# Look for double 
				#Found
				idx = binary(nums, i+1, n, double)
				# print("found {} at {} b/w ({},{})".format(double,idx,i+1,n))
				# if marked[idx] is present or not
				if idx!=n and nums[idx]==double:
						
					# not marked
					if idx not in marked:
						marked[idx]=1
					else:
						# marked
						while True:
							idx+=1
							# print("here",idx)
							if idx<n and nums[idx]==double and idx not in marked:
								marked[idx]=1
								break
							if idx==n or nums[idx]!=double:
								return []
				else:
					return []
				ans.append(num)
			else:
				pass
				# print("marked")
			# print("ans",ans)
		return ans

if __name__=="__main__":
	s=input()
	nums = [int(el) for el in s[1:-1].split(",")]
	
	print(Solution().findOriginalArray(nums))
	# print(nums,len(nums))