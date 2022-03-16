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

        def divide(mid,k):
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
