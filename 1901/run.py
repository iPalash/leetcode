class Solution:


    def findPeakGrid(self, nums: list[list[int]]) -> list[int]:
        print(nums)
        m = len(nums)
        n = len(nums[0])
        i_m, j_m = 0, m
        i_n, j_n = 0,n
        while 1: # No need to check since we will always find a peak, right?
            mid_m = i = (i_m+j_m)//2
            mid_n = j = (i_n+j_n)//2
            curr = nums[i][j]
            left = nums[i][j-1] if j>0 else -1
            right = nums[i][j+1] if j<n-1 else -1
            top = nums[i-1][j] if i>0 else -1
            bottom = nums[i+1][j] if i<m-1 else -1
            mx = max(curr,left,right,top,bottom)
            if mx==left:
                j_n = mid_n #j=j-1 
            elif mx==right:
                i_n = mid_n+1 #j=j+1
            elif mx==top:
                j_m = mid_m #i=i-1
            elif mx==bottom:
                i_m = mid_m+1 #i=i+1
            else:
                break
        return [i,j]

nums = [[int(el) for el in row.split(",")] for row in input()[2:-2].split("],[")]
print(Solution().findPeakGrid(nums))
