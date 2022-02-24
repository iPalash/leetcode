class Solution:
    def util(self, s, count, i, j, new="") -> str:
        if i>j:
            return new+new[::1]
        if i==j:
            return new+s[i]+new[::-1]
        op1 = ""
        if s[i]==s[j]:
            op1 = self.util(s,count+2,i+1,j-1,new+s[i])
        op2 = self.util(s,0,i,j-1)
        op3 = self.util(s,0,i+1,j)
        if len(op2)>len(op1):
            op1,op2=op2,op1
        if len(op3)>len(op1):
            op1,op3=op3,op1
        return op1
    def longestPalindrome(self, s:str) -> str:
        print(s)
        self.d= {}
        n = len(s)
        if n==1:
            return s
        return self.util(s,0,0,n-1)

s = input()[1:-1]

print(Solution().longestPalindrome(s))
