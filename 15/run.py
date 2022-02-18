class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        n=len(nums)
        # print(nums)
        for k in range(n-2):
            if k>0 and nums[k]==nums[k-1]:
                #Skip counting this
                continue
            target = - nums[k]
            i = k+1
            j = n - 1
            while i<j:
                # print("idx:",i,j,k)
                
                # print("elements:",nums[i],nums[j],target)
                # print("compare:", target, nums[i]+nums[j])
                if target>nums[i]+nums[j]:
                    i+=1
                elif target<nums[i]+nums[j]:
                    j-=1
                elif target==(nums[i]+nums[j]):
                    # print(i,j,k)
                    #Skipping duplicates

                    ans.append((el:=[nums[i],nums[j],nums[k]]))
                    while i<j and nums[i]==el[0]:
                        i+=1
                    while i<j and nums[j]==nums[1]:
                        j-=1
                    # i+=1
                    # j-=1
        # print(ans)
        return ans

nums=[int(el) for el in input()[1:-1].split(",")]
print(Solution().threeSum(nums))
