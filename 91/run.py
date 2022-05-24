class Solution:
    def numDecodings(self, s:str) -> int:
        print(s)
        n = len(s)
        prv1,prv2 = 1,0
        i=n-1
        while i>=0:
            curr = 0
            if (x:=int(s[i]))>0:
                #Consider 1-len
                if prv1!=0:
                    curr+=prv1
                #Consider 2-len
                if i<n-1: #ignore last dig
                    if int(s[i:i+2])<27 and prv2!=0:
                        curr+=prv2
            i-=1
            prv1,prv2=curr,prv1
        return prv1

s = input()[1:-1]

print(Solution().numDecodings(s))
