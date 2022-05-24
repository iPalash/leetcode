class Solution:
    def intervalIntersection(self, firstList:list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        # print(firstList,secondList)
        times=[]
        for el in firstList:
            times.append((el[0],0,1)) # 0 signifies start
            times.append((el[1],1,1))
        for el in secondList:
            times.append((el[0],0,2))
            times.append((el[1],1,2))
        first,second = False,False
        times.sort()
        ans = []
        active_open = None
        for (time, start, num) in times:
            # print(time,start,num,active_open,first,second)
            if num==1:
                #From first list
                if start==0:
                    #open
                    first=True
                else:
                    first=False
                    #closed
            else:
                #From second list
                if start==0:
                    second=True
                    #open
                else:
                    second=False
                    #closed
            if (first!=second) and active_open!=None:
                ans.append([active_open,time])
                active_open=None
            if first==second==True:
                active_open = time
        return ans


first = [[int(el) for el in s.split(",")] for s in input()[2:-2].split("],[")]
second = [[int(el) for el in s.split(",")] for s in input()[2:-2].split("],[")]
print(Solution().intervalIntersection(first,second))

