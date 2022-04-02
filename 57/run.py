class Solution:
    def insertInterval(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        print(intervals, newInterval)


        def binary(i,j,arr,target):
            while i<j:
                mid = (i+j)//2
                if arr[mid][0]<=target<=arr[mid][1]:
                    return mid
                if arr[mid][0]>target:
                    j=mid
                else:
                    i=mid+1
            return i
        n = len(intervals)
        [s,e] = newInterval
        l = binary(0,n,intervals,s)
        r = binary(0,n,intervals,e)
        print(l,r)
        if l==r:
            if l==0:
                # check for last
                if intervals[0][0]>e:
                    intervals.insert(0,newInterval)
                    return intervals
                else:
                    intervals[0][0]=min(intervals[0][0],newInterval[0])
                    return intervals
            elif l==n:
                intervals.append(newInterval)
                return intervals
            else:
                if intervals[l][0]>e:
                    intervals.insert(l,newInterval)
                else:
                    intervals[l][0]=min(intervals[l][0],newInterval[0])
                return intervals
        else:
            start = min(intervals[l][0],s)
            end = e
            if r<n:
                if intervals[r][0]<=e:
                    end = max(intervals[r][1],e)
                    return intervals[:l]+[[start,end]]+intervals[r+1:]
                else:
                    return intervals[:l]+[[start,end]]+intervals[r:]
            else:
                return intervals[:l]+[[start,end]]+intervals[r+1:]

        return intervals

intervals = [[int(el) for el in row.split(',')] for row in input()[2:-2].split('],[')]

newInterval = [int(el) for el in input()[1:-1].split(',')]

print(Solution().insertInterval(intervals,newInterval))


