class Solution:
    def matchBracket(self, s):
        curr = []
        brackets = {}
        for i,el in enumerate(s):
            if el=='[':
                curr.append(i)
            elif el==']':
                brackets[curr.pop()]=i
        return brackets
    def decodeString(self, s: str) -> str:
        brackets = self.matchBracket(s)
        i = 0
        ans = ""
        n = len(s)
        while i<n:
            # If a char
            el = s[i]
            if 97<=ord(el)<=122:
                ans += el
                i+=1
            else:
                j = i
                while s[j]!='[':
                    j+=1
                k = int(s[i:j])
                ans+=k*self.decodeString(s[j+1:brackets[j]])
                i=brackets[j]+1
        return ans
        
