class Solution:
    def shortestDistanceColor(self, colors: list[int], queries: list[list[int]]) -> list[int]:
        print(colors, queries)
        n = len(colors)
        index = [[n for _ in range(n)] for _ in range(3)]

        # L to R pass
        last_1,last_2,last_3 = -n,-n,-n
        for i,el in enumerate(colors):
            if el==1:
                last_1=i
            index[0][i]=min(index[0][i],i-last_1)
            if el==2:
                last_2=i
            index[1][i]=min(index[1][i],i-last_2)
            if el==3:
                last_3=i
            index[2][i]=min(index[2][i],i-last_3)
        # R to L Pass
        last_1,last_2,last_3 = 2*n,2*n,2*n
        for i in range(n-1,-1,-1):
            if colors[i]==1:
                last_1=i
            index[0][i]=min(index[0][i],last_1-i)
            if colors[i]==2:
                last_2=i
            index[1][i]=min(index[1][i],last_2-i)
            if colors[i]==3:
                last_3=i
            index[2][i]=min(index[2][i],last_3-i)
        ans = []
        for idx,color in queries:
            if (a:=index[color-1][idx])>=n:
                ans.append(-1)
            else:
                ans.append(a)
        return ans

colors = [int(el) for el in input()[1:-1].split(',')]

queries = [[int(el) for el in row.split(",")] for row in input()[2:-2].split("],[")]

print(Solution().shortestDistanceColor(colors, queries))
