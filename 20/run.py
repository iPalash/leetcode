class Solution:
	def isValid(self, s:str):
		st = []
		for ltr in s:
			if ltr=='(' or ltr=='[' or ltr=='{':
				st.append(ltr)
			else:
				if len(st)==0:
					return False
				if (ltr==')' and st.pop()=='(') or (ltr==']' and st.pop()=='[') or (ltr=='}' and st.pop()=='{'):
					continue
				return False
		return len(st)==0

s = input()

print(Solution().isValid(s[1:-1]))
