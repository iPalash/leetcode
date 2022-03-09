class Solution:


    def findPeakGrid(self, nums: list[list[int]]) -> list[int]:
        print(nums)
        m = len(nums)
        n = len(nums[0])
        i,j = m//2,n//2
        while i>=0 and i<m and j>=0 and j<n:
            curr = nums[i][j]
            left = nums[i][j-1] if j>0 else -1
            right = nums[i][j+1] if j<n-1 else -1
            top = nums[i-1][j] if i>0 else -1
            bottom = nums[i+1][j] if i<m-1 else -1
            mx = max(curr,left,right,top,bottom)
            if mx==left:
                j=j-1
            elif mx==right:
                j=j+1
            elif mx==top:
                i=i-1
            elif mx==bottom:
                i=i+1
            else:
                break
        return [i,j]

nums = [[int(el) for el in row.split(",")] for row in input()[2:-2].split("],[")]
print(Solution().findPeakGrid(nums))
