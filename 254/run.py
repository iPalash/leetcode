import math
class Solution:
    def getAllFactors(self,n):
        i = 2
        while i*i<=n:
            if n%i==0:
                self.f.append(i)
            i+=1
    def rec(self, n, i, series):
        print(n,i,series)
        if n==0:
            return
        


        # Add all >= ith prime factor to the series
        for j in range(i,self.fn):
            if n%self.f[j]==0 and self.f[j]<=n and (len(series)==0 or self.f[j]>=series[-1]) and self.f[j]<=n/self.f[j]:
                series.append(self.f[j])
                self.ans.append(series+[int(n/self.f[j])])
                self.rec(int(n/self.f[j]),j,series)
                series.pop()


    def getFactors(self, n:int) -> list[list[int]]:
        print(n)
        self.f = []
        self.ans = []
        self.getAllFactors(n)
        print(self.f)
        self.f = list(set(self.f))
        self.fn = len(self.f)
        print("factors",self.f)

        self.rec(n,0,[])
        return self.ans
        #return list(map(lambda x:[int(el) for el in x.split(":")],list(set(self.ans))))

n = int(input())

print(Solution().getFactors(n))
