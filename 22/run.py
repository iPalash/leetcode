def util(n, o, c, val, ans):
    if o==c==n:
        ans.append(val)
        return
    if c>o or c>n or o>n:
        return
    util(n,o+1,c,val+"(",ans)
    util(n,o,c+1,val+")",ans)


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        util(n, 0,0,"",ans)
        return ans
        

print(Solution().generateParenthesis(int(input())))
