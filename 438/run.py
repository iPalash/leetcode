DEBUG=False

from collections import Counter
import logging 
l = logging.getLogger()
if DEBUG:
    logging.basicConfig(level=logging.DEBUG)

class Solution:
    def findAnagrams(self, s:str, p:str) -> list[int]:
        l.debug("input: %s %s",s,p)
        i,j=0,0
        n = len(s)
        ln = len(p)
        counts = Counter(p)
        original = counts.copy()
        # print(counts,original)
        ans = []
        while j<n:

            l.debug("i:%d j:%d: %s %s",i,j,counts,s[j])
            if s[j] in counts:
                if counts[s[j]]>0:
                    counts[s[j]]-=1
                    if j-i+1==ln:
                        ans.append(i)
                        counts[s[i]]+=1
                        i+=1
                    j+=1
                else:
                    # Find next k and set i to that such that s[k]=s[j] and update counts
                    while s[i]!=s[j]:
                        counts[s[i]]+=1
                        i+=1
                    i+=1
                    j+=1
            else:
                counts=original.copy()
                j+=1
                i=j
        return ans


s=input()[1:-1]
p=input()[1:-1]
# l.info("asdadas")
print(Solution().findAnagrams(s,p))
