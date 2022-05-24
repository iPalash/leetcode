from functools import reduce
class Solution:
    def minAvailableDuration(self, slots1: list[list[int]], slots2: list[list[int]], duration: int) -> list[int]:
        # Ensure 1 is always the larger one
        if len(slots1)<len(slots2):
            slots1,slots2=slots2, slots1
        n = len(slots1)
        # Sort the two wrt to start times
        slots1.sort(key=lambda x:x[0])
        slots2.sort(key=lambda x:x[0])
        print(slots1,slots2, duration)

        temp = reduce(lambda a,b:a+b, slots1)
        ans = []
        for [start,end] in slots2:
            i,j= 0,n*2
            while i<j:
                mid = (i+j)//2
                if temp[mid]>=start:
                    j=mid
                else:
                    i=mid+1
            if i<2*n:
                # Found a match
                i = i//2
                start2,end2 = slots1[i][0],slots1[i][1]
                print(i,start,end,start2,end2)
                if min(end2,end)-(st:=max(start2,start))>=duration:
                    ans.append(st)
        slots1,slots2=slots2, slots1
        n = len(slots1)
        # Sort the two wrt to start times
        slots1.sort(key=lambda x:x[0])
        slots2.sort(key=lambda x:x[0])
        print(slots1,slots2, duration)

        temp = reduce(lambda a,b:a+b, slots1)
        for [start,end] in slots2:
            i,j= 0,n*2
            while i<j:
                mid = (i+j)//2
                if temp[mid]>=start:
                    j=mid
                else:
                    i=mid+1
            if i<2*n:
                # Found a match
                i = i//2
                start2,end2 = slots1[i][0],slots1[i][1]
                print(i,start,end,start2,end2)
                if min(end2,end)-(st:=max(start2,start))>=duration:
                    ans.append(st)

        if len(ans)>0:
            return [min(ans),min(ans)+duration]
        return []

slots1 =  [[int(e) for e in l.split(',')] for l in input()[2:-2].split('],[')]
slots2 =  [[int(e) for e in l.split(',')] for l in input()[2:-2].split('],[')]
duration = int(input())

print(Solution().minAvailableDuration(slots1,slots2,duration))
