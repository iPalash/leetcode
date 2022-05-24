class Solution:
    def util(self, s):
        s_=""
        for ch in s:
            if ch=='#':
                s_=s_[:-1]
            else:
                s_+=ch
        return s_
        
    def backspaceCompare(self, s:str, t:str) -> bool:
        i,j,ih,jh=len(s)-1,len(t)-1,0,0
        print(s,t)
        while 1:
            # print(i,j)
            while i>=0:
                if s[i]=='#':
                    i-=1
                    ih+=1
                elif ih>0 and s[i]!='#':
                    i-=1
                    ih-=1
                else:
                    break
            while j>=0:
                if t[j]=='#':
                    j-=1
                    jh+=1
                elif jh>0 and t[j]!='#':
                    j-=1
                    jh-=1
                else:
                    break
            if not(i>=0 and j>=0 and s[i]==t[j]):
                return i==j==-1
            i-=1
            j-=1
s=input()[1:-1]
t=input()[1:-1]
print(Solution().backspaceCompare(s,t))
