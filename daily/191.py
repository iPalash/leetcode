# link: https://leetcode.com/problems/number-of-1-bits/

# level : easy

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n!=0:
           # print(n,bin(n))
            cnt+=1
            n &= (n-1) # set the least sig one to zero
        return cnt
            
        
