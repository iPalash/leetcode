class Solution:
    def numberofArithmeticSlices(self, nums: list[int])-> int:
        print(nums)
        n = len(nums)
        if n<=2:
            return 0
        cnt = 0
        ans=0
        i=0
        while i<n-1:
            print(i)
            if cnt==0:
                while i<n-2 and nums[i+2]-nums[i+1]!=nums[i+1]-nums[i]:
                    i+=1
                if i<n-2:
                    diff = nums[i+2]-nums[i+1]
                    cnt+=3
                    i+=2
                else:
                    break
            else:
                print(i,cnt)
                if diff==nums[i+1]-nums[i]:
                    cnt+=1
                    i+=1
                else:
                    ans+=(cnt*cnt-3*cnt+2)//2
                    print("cnt",cnt)
                    cnt=0
        if cnt>0:
            ans+=(cnt*cnt-3*cnt+2)//2
        return ans



            

nums = [int(el) for el in input()[1:-1].split(",")]

print(Solution().numberofArithmeticSlices(nums))
