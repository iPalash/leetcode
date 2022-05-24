from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
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
        while len(q)>0:
            curr = q.pop(0)
            i+=1
            for nxt in after[curr]:
                preq[nxt]-=1
                if preq[nxt]==0:
                    q.append(nxt)
        return i==numCourses

numCourses = int(input())
prerequisites = [[int(el) for el in row.split(',')] for row in input()[2:-2].split('],[')]

print(Solution().canFinish(numCourses,prerequisites))
