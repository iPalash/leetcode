from heapq import heappush,heapreplace

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        times=[]
        intervals.sort(key=lambda x:x[0])
        heap = []
        for i in intervals:
            # if min of heap (end time) is greater than next start time, it means they overlap, need more rooms so push to heap end of this
            if len(heap)==0 or heap[0]>i[0]:
                heappush(heap, i[1])
            else:
                # if not then it can be replaced
                heapreplace(heap, i[1])
            # print(i,heap)
        # print(heap)
        return len(heap)
        

arr=[[int(el) for el in s.split(",")] for s in input()[2:-2].split("],[")]
print(arr)
print(Solution().minMeetingRooms(arr))
