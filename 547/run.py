class Solution:
    def findCircleNum(self, isConnected:list[list[int]]) -> int:
        n = len(isConnected)
        provinces=0
        visited = [False for el in range(n)]
        queue=[0]
        for city in range(n):
            if not visited[city]:
                #Visit city and ones it is connected to
                provinces+=1
                queue = [city]
                while len(queue)>0:
                    curr = queue.pop()

                    # print("Q:", queue, curr)
                    visited[curr]=True
                    for j in range(n):
                        if curr!=j and isConnected[curr][j]==1 and not visited[j]:
                            queue.append(j)
        return provinces

grid = [[int(s) for s in el.split(',')] for el in input()[2:-2].split("],[")]
print(Solution().findCircleNum(grid))
