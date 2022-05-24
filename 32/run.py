class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lng = 0
        st = [-1]
        for i,ltr in enumerate(s):
         #   print(i,ltr,st)
            if ltr=='(':
                st.append(i)
            else:
                st.pop()
                if len(st)!=0:
                    lng = max(lng,i-st[-1])
                else:
                    st.append(i)
        return lng

s = input()
print(Solution().longestValidParentheses(s[1:-1]))
                
                
                
                
        
