class Solution:
    def longestPalindrome(self, s:str) -> str:
        print(s)
        n = len(s)
        if n==1:
            return s
        ans = s[0]
        mx = 1
        for i in range(n):
            #odd size palindrone starting at i
            j = 1
            while i-j>=0 and i+j<n:
                if s[i-j]==s[i+j]:
                    print("Found odd:", s[i-j:i+j+1])
                    if j*2+1>mx:
                        mx=j*2+1
                        ans=s[i-j:i+j+1]
                    j+=1
                else:
                    break
            #even size palindrome with first center as i
            if i<n-1 and s[i]==s[i+1]:
                if 2>mx:
                    mx=2
                    ans=s[i:i+2]
                j=1
                while i-j>=0 and i+1+j<n:
                    if s[i-j]==s[i+1+j]:
                        print("Found even:", s[i-j:i+j+2])
                        if j*2+2>mx:
                            mx=j*2+2
                            ans=s[i-j:i+j+2]
                        j+=1
                    else:
                        break

        return ans

s = input()[1:-1]

print(Solution().longestPalindrome(s))
