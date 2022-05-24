class Solution:
    def lengthOfLongestSubstringKDistinct(self, s:str, k:int) -> int:
        print(s)
        if k==0:
            return 0

        n = len(s)

        d = {}
        u = 0

        i = 0
        j = 0
        mx = -1
        while i < n and j < n:
            print(i,j,d)
            if s[j] in d:
                d[s[j]]+=1
            else:
                d[s[j]]=1
                u+=1
            if u<=k:
                mx=max(mx,j-i+1)
            else:
                #Decr i until u becomes <=
                while u>k and i<j:
                    # Remove s[i] from d
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        del d[s[i]]
                        u-=1
                    i+=1
                mx = max(mx,j-i+1)
            print("After:",i,j,d,u,mx)
            j+=1
        return mx

s = input()[1:-1]
k = int(input())

print(Solution().lengthOfLongestSubstringKDistinct(s,k))
