class Solution:
    def numSubarrayProductLessThanK(self, nums:list[int], k:int)-> int:
        n=len(nums)
        m = 1
        mult = [-1 for _ in range(n)]
        j = 0
        last_j = -1
        ans = 0
        for i in range(0,n):
            #Find max j for which product < k
            #print("S:",i,j,m)
            if last_j!=-1 and last_j>i:
                j = last_j
                m = int(m/nums[i-1])
                if m<k:
                    mult[i]=j
            else:
                j = i
                m = 1
            while j<n:
                m*=nums[j]
                #print("In:",i,j,m)
                if m<k:
                    mult[i]=j
                    last_j = j
                    last_mult = m
                    j+=1
                else:
                    last_j=-1
                    break
                    
        ans=0
        #print(mult)
        for i,j in enumerate(mult):
            if j!=-1:
                ans+=j-i+1
        return ans
                    



nums = [int(el) for el in input()[1:-1].split(",")]
k=int(input())
print(Solution().numSubarrayProductLessThanK(nums,k))
