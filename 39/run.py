from collections import defaultdict


def find(candidates, target, curr, path, ans={}):
	if target==curr:
		# print(ans)
		for el in ans[target]:
			if el==path:
				return 
		ans[target].append(path)
		return path
	if curr > target:
		return None
	for candidate in candidates:
		if curr+candidate<=target:
			#memorisation here
			path_t = path+[candidate]
			path_t.sort()
			# print(curr+candidate,path_t)
			a = find(candidates, target, curr+candidate, path_t,ans)
	return 
	

		


class Solution:
	def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
		# print(candidates,target)
		ans = defaultdict(list)
		find(candidates, target, 0, [], ans)
		return ans[target]

def main():
	s=input()
	arr=[int(el) for el in s[1:-1].split(",")]
	target = int(input())
	print(Solution().combinationSum(arr, target))

main()