import math
class Solution:
    def getPrimeFactors(self, n, lim, last):
        if last>lim:
            return
        if n%last==0:
            self.f.append(last)
            self.getPrimeFactors(n//last,lim, last)
        else:
            self.getPrimeFactors(n,lim,last+1)
    def rec(self, n, i, series):
        if len(series)>=1 and series[-1]<=n:
            self.ans.append(":".join(map(str,series+[n])))
        
        if i==self.fn:
            return

        # Multiply all>= ith factor to last element of series
        if len(series)>0: 
            last = series[-1]
            for j in range(i,self.fn):
                if last*self.f[j]<= n/self.f[j]:
                    series[-1]=last*self.f[j]
                    self.rec(int(n/self.f[j]),j+1,series)
                    series[-1]=last

        # Add all >= ith prime factor to the series
        for j in range(i,self.fn):
            if self.f[j]<=n and (j==i or self.f[j]!=self.f[j-1]):
                series.append(self.f[j])
                self.rec(int(n/self.f[j]),j+1,series)
                series.pop()


    def getFactors(self, n:int) -> list[list[int]]:
        print(n)
        self.f = []
        self.ans = []
        self.getPrimeFactors(n, math.ceil(math.sqrt(n)), 2)
        self.fn = len(self.f)
        print(self.f)

        self.rec(n,0,[])

        return list(map(lambda x:[int(el) for el in x.split(":")],list(set(self.ans))))

n = int(input())

print(Solution().getFactors(n))
