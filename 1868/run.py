class Solution:
    def findRLEArray(self, encoded1: list[list[int]], encoded2: list[list[int]]) -> list[list[int]]:
        print(encoded1,encoded2)

        pos=0
        i,pos_i = 0,0
        j,pos_j = 0,0
        ans = []
        last = -1
        while i<len(encoded1):
            print(i,j,last,ans)
            if encoded1[i][1]-pos_i<encoded2[j][1]-pos_j:
                # 1st array has fewer element to multiply
                freq = encoded1[i][1]-pos_i
                product = encoded1[i][0]*encoded2[j][0]
                i+=1
                pos_i=0
                pos_j+=freq
            elif encoded1[i][1]-pos_i>encoded2[j][1]-pos_j:
                # 2nd array has fewer
                freq = encoded2[j][1]-pos_j
                product = encoded1[i][0]*encoded2[j][0]
                j+=1
                pos_j=0
                pos_i+=freq
            else:
                #equal jump both
                freq = encoded2[j][1]-pos_j
                product = encoded1[i][0]*encoded2[j][0]
                j+=1
                pos_j=0
                i+=1
                pos_i=0

            
            if last==product:
                # combine if equal
                ans[-1]=[product,freq+ans[-1][1]]
            else:
                last=product
                ans.append([product,freq])



        return ans

encoded1 = [[int(e) for e in l.split(',')] for l in input()[2:-2].split('],[')]
encoded2 = [[int(e) for e in l.split(',')] for l in input()[2:-2].split('],[')]

print(Solution().findRLEArray(encoded1,encoded2))

