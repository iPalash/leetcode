from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        print(numCourses, prerequisites)
        preq = defaultdict(int)
        after = defaultdict(set)
        for curr,before in prerequisites:
            preq[curr]+=1
            after[before].add(curr)
        q = []
        for i in range(numCourses):
            if preq[i]==0:
                q.append(i)
        i = 0
        ans = []
        while len(q)>0:
            curr = q.pop(0)
            ans.append(curr)
            i+=1
            for nxt in after[curr]:
                preq[nxt]-=1
                if preq[nxt]==0:
                    q.append(nxt)
        return ans if i==numCourses else []

numCourses = int(input())
prerequisites = [[int(el) for el in row.split(',')] for row in input()[2:-2].split('],[')]

print(Solution().findOrder(numCourses,prerequisites))
