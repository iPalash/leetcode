class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        times=[]
        intervals.sort(key=lambda x:x[0])
        for meeting in intervals:
            times.append((meeting[0],0)) #0 denote start
            times.append((meeting[1],1)) #1 denotes end

        times.sort(key=lambda x:x[0])
        #print(times)
        rooms = 0
        mx = -1
        for time in times:
            # print(time,rooms)
            if time[1]==0:
                rooms+=1
            else:
                rooms-=1
            mx=max(mx,rooms)
        return mx

arr=[[int(el) for el in s.split(",")] for s in input()[2:-2].split("],[")]
print(arr)
print(Solution().minMeetingRooms(arr))
