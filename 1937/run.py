class Solution:
	def maxPoints(self, points: list[list[int]]) -> int:
		rows=len(points)
		cols=len(points[0])
		# print(points)
		left = [0 for _ in  range(0,cols)]
		right = [0 for _ in  range(0,cols)]
		curr = [0 for _ in  range(0,cols)]
		for r in range(rows):
			for c in range(cols):
				if r==0:
					curr[c]=points[r][c]
				else:
					curr[c]=points[r][c]+max(left[c],right[c])
			for c in range(cols):
				if c==0:
					left[c]=curr[c]
				else:
					left[c]=max(left[c-1]-1,curr[c])
			for c in range(cols-1,-1,-1):
				if c==cols-1:
					right[c]=curr[c]
				else:
					right[c]=max(right[c+1]-1,curr[c])
		ans = max(curr)
		return ans

s = input()
nums = [[int(n) for n in el.split(',')] for el in s[2:-2].split("],[")]
print(Solution().maxPoints(nums))