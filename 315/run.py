from collections import defaultdict
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        #print(nums)
        d = defaultdict(int)

        def sort():
            n = len(nums)

            def divide(i,j):
                #print(i,j)
                if i==j:
                    return [(nums[i],i)]
                else:
                    mid = (i+j+1)//2
                    #print("Mid",i,mid,j)
                    return merge(divide(i,mid-1),divide(mid,j))

            def merge(left,right):
                #print("merging",left,right)
                carry = 0
                l,r=0,0
                merged = []

                while l<len(left) and r<len(right):
                    if left[l][0]>right[r][0]:
                        carry+=1
                        #Ensure carry only gets added once
                        merged.append(right[r])
                        r+=1
                    else:
                        d[left[l][1]]+=carry
                        merged.append(left[l])
                        l+=1
                while l<len(left):
                    d[left[l][1]]+=carry
                    merged.append(left[l])
                    l+=1
                while r<len(right):
                    merged.append(right[r])
                    r+=1
                #print("merged",d)
                return merged
            divide(0,n-1)

        sort()
        print(d)
        ans = []
        for i in range(len(nums)):
            ans.append(d[i])

        return ans

nums = [int(el) for el in input()[1:-1].split(',')]

print(Solution().countSmaller(nums))
