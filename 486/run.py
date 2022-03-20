class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        print(nums)

        n = len(nums)

        dp1 = [[0 for _ in range(n)] for _ in range(n)]
        dp2 = [[0 for _ in range(n)] for _ in range(n)]

        sm= sum(nums)

        for i in range(n):
            dp1[i][i]=nums[i]
        

        for k in range(1,n):
            for i in range(n):
                j = i+k
                if j<n:
                    dp1[i][j]=max(dp2[i+1][j]+nums[i],dp2[i][j-1]+nums[j])
                    dp2[i][j]=min(dp1[i+1][j],dp1[i][j-1])
                    #print(i,j,dp1[i][j],dp2[i][j])
        print(dp1,dp2)
        return dp1[0][n-1]>=(sm-dp1[0][n-1])

nums = [int(el) for el in input()[1:-1].split(",")]

print(Solution().PredictTheWinner(nums))
