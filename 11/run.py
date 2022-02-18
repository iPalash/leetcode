class Solution:
    def maxArea(self, height: list[int]) -> int:
        # print(height)
        i,j=0,len(height)-1
        mx = (j-i)*min(height[i],height[j])
        while i<j:
            mx=max(mx,(j-i)*min(height[i],height[j]))
            # print(i,j)
            lower = h_i if (b:=(h_i:=height[i])<(h_j:=height[j])) else h_j
            lo= i if b else j
            if lo==i:
                k=i+1
                while k<j and height[k]<height[i]:
                    k+=1
                i=k
            else:
                k=j-1
                while i<k and height[k]<height[j]:
                    k-=1
                j=k
            

            
        return mx

height = [int(el) for el in input()[1:-1].split(",")]
print(Solution().maxArea(height))
