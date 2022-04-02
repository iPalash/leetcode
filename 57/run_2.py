class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        print(intervals, newInterval)
        ans = []
        i = 0
        [s,e]=newInterval
        n = len(intervals)
        # append intervals before 
        while i<n and intervals[i][0]<s:
            ans.append(intervals[i])
            i+=1

        # merge if overlap else insert
        if ans and ans[-1][1]>=s:
            ans[-1][1]=max(ans[-1][1],e)
        else:
            ans.append(newInterval)

        while i<len(intervals):
            # merge or append with last
            [a,b]=intervals[i]
            if ans[-1][1]<a:
                ans.append([a,b])
            else:
                ans[-1][1]=max(ans[-1][1],b)
            i+=1

        return ans

intervals = [[int(el) for el in row.split(',')] for row in input()[2:-2].split('],[')]

newInterval = [int(el) for el in input()[1:-1].split(',')]

print(Solution().insert(intervals,newInterval))


