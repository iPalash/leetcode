class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s:str) -> int:
        print(s)
        if len(s)<=2:
            return len(s)

        start = 0
        nxt = 0
        last1 = s[0]
        i = 1
        mx = 1
        last2 = None
        while i < len(s):
            el = s[i]
            print(i,el,last1,last2,start,mx)
            if el==last1 and not last2:
                mx = max(mx,i-start+1)
            elif el!=last1 and not last2:
                last2 = el
                nxt = i
                mx = max(mx,i-start+1)
            elif el==last1 and last2:
                nxt = i
                last1,last2=last2,last1
                mx = max(mx,i-start+1)
            elif el==last2:
                mx = max(mx,i-start+1)
            else:
                # Distinct char
                start = nxt
                nxt = i
                last1=last2
                last2 = el
            i+=1


        return mx

s = input()[1:-1]
print(Solution().lengthOfLongestSubstringTwoDistinct(s))
