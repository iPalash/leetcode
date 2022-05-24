class Solution:
    def numberOfPatterns(self, m:int, n:int) -> int:
       # print(m,n)
#

        toVisit = []
        _ = [(toVisit:=toVisit+el) for el in [[(i,j,0) for j in range(3)] for i in range(3)]]
        # print(len(toVisit))

        count = 0

        def backtrack(i,j,l):
            nonlocal count,m,n
            if m<=l<=n:
                count+=1
            if l>n:
                return

            for idx,(a,b,c) in enumerate(toVisit):
                if (i==-1 and j==-1): # first pick
                    toVisit[idx]=(a,b,1)
                    backtrack(a,b,l+1)
                    toVisit[idx]=(a,b,0)
                elif c==0:
                    # check cross
                    midx,midy=i+a,j+b
                    if midx%2==0 and midy%2==0:
                        midx=midx//2
                        midy=midy//2
                        if toVisit[midx*3+midy][2]==1: # Mid has already been visited
                            
                            toVisit[idx]=(a,b,1)
                            backtrack(a,b,l+1)
                            toVisit[idx]=(a,b,0)
                        else:
                            pass # Mid exists but wasn't visited
                    else:
                        # No mid
                        toVisit[idx]=(a,b,1)
                        backtrack(a,b,l+1)
                        toVisit[idx]=(a,b,0)

        backtrack(-1,-1,0)

        return count



m=int(input())
n=int(input())

print(Solution().numberOfPatterns(m,n))
