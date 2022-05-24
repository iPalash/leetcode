import math
class Solution:
    def maximizeSweetness(self, sweetness: list[int], k:int) -> int:
        print(sweetness,k)
        n = len(sweetness)
        k+=1
        if k==n:
            return min(sweetness)
        mn = 1
        mx = math.ceil(sum(sweetness)/k)

        prefix = [0 for _ in range(1+n)]
        prefix[0]=sweetness[0]
        for i in range(n):
            if i==0:
                continue
            prefix[i]=prefix[i-1]+sweetness[i]
        print(prefix)


        def divideFast(mid):
            # this works by using binary search on prefix array to find parts instead of linear time
            # Instead of o(n) it would be klogN

            i=0
            def binary(i,j,target):
                while i<j:
                    mid = (i+j)//2
                    if prefix[mid]<target:
                        i=mid+1
                    else:
                        j=mid
                print("Finding",target,prefix[i])
                return i
            count = 0 
            last = 0
            print("Faster counting",mid,k)
            print("prefix",prefix)
            while i<n:
                j = binary(i,n,last+mid)
                if j>=n:
                    return count
                print(i,j)
                count +=1
                last=prefix[j]
                i = j+1
            return count


        def divide(mid,k):
            return divideFast(mid)
            print("Fast count:",mid,divideFast(mid))
            curr = 0
            count = 0
            parts = []
            sub = []
            for part in sweetness:
                if curr+part>=mid:
                    # New segment after this
                    parts.append(sub+[part])
                    sub = []
                    count+=1
                    curr = 0
                else:
                    # Add to existing segment
                    sub.append(part)
                    curr+=part


            print("count:",mid,count, parts)
            return count


        
        while mn<mx:
            mid = (mn+mx+1)//2
            print(mn,mid,mx)
            if divide(mid,k)>=k:
                mn=mid
            else:
                mx=mid-1


        return mx

sweetness = [int(el) for el in input()[1:-1].split(",")]
k = int(input())

print(Solution().maximizeSweetness(sweetness,k))
