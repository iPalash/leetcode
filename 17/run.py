mp = {'2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']}
class Solution:
    def utils(self, digits):
        if len(digits)==0:
            return [""]
        ans = []
        el = digits[0]
        for el2 in mp[el]:
            for res in self.utils(digits[1:]):
                ans.append(el2+res)
        return ans

    def letterCombination(self, digits: str) -> list[str]:
        a = self.utils(digits)
        if a==[""]:
            return []
        return a



print(Solution().letterCombination(input()[1:-1]))
