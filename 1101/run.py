class Solution:
	def earliestAcq(self, logs: list[list[int]], n: int) -> int:
		represent = list(range(0,n))
		nodes = [[el] for el in range(0,n)]
		mapper = {el:el for el in range(0,n)}
		logs.sort(key=lambda x:x[0])
		for log in logs:
			[t,x,y]=log
			# print(t,x,y)
			# print(nodes)
			color_x = mapper[x]
			color_y = mapper[y]
			if color_x!=color_y:
				# print("X/Y",color_x,color_y)
				color = min(color_x,color_y)
				other_color = color^color_x^color_y
				# print("Low/high",color,other_color)
				# print("Nodes", nodes[color],nodes[other_color])
				nodes[color]=nodes[color]+nodes[other_color]
				for node in nodes[other_color]:
					mapper[node]=color
				nodes[other_color]=[]
			if len(nodes[0])==n:
				return t
		return -1

if __name__=="__main__":
	s=input()
	#Remove [[ ]] at start and end
	logs = [[int(q) for q in el.split(",")] for el in s[2:-2].split("],[")]

	n=int(input())
	print(Solution().earliestAcq(logs,n))