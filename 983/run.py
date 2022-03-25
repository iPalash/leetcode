import math
class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        print(days,costs)
        n = len(days)
        total = [math.inf]*(n+1)
        total[0]=0

        def binary(arr,i,j,target):
            #print("finding {} b/w [{},{}]".format(target,i,j))
            while i<j:
                mid = (i+j+1)//2
                if arr[mid]<=target:
                    i=mid
                else:
                    j=mid-1
            return j
        for idx,day in enumerate(days):
            for jump,cost in zip([1,7,30],costs):
                if day-jump>=days[0]:
                    prev = binary(days,0,idx,day-jump)+1
                else:
                    prev = 0
                print("Previous to {} at jump {} is {}".format(day,jump,prev))
                total[idx+1]=min(total[idx+1],total[prev]+cost)
            #print(day,total[idx+1])
        print(total)        

        return total[-1]

days = [int(el) for el in input()[1:-1].split(',')]
costs = [int(el) for el in input()[1:-1].split(',')]
print(Solution().mincostTickets(days,costs))
