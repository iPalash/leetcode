class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        count = dict()
        n = len(s)
        i = 0
        j = 0
        ans = 0
        while j<n:
            # print(i,j,count)
            if s[j] not in count:
                count[s[j]]=j
                if j-i+1==k:
                    # print("#ANS", i,j,s[i:j+1])
                    ans+=1
                    del count[s[i]]
                    i+=1
                j+=1
            else:
                idx = count[s[j]]
                # print(i,j,idx,count)
                for l in range(i,idx+1):
                    del count[s[l]]
                count[s[j]]=j
                i=idx+1
                j+=1
            if j-i+1>k:
                del count[s[i]]
                i+=1
            # print(count)
        return ans


if __name__ == "__main__":
    s = input()[1:-1]
    k= int(input())
    print(Solution().numKLenSubstrNoRepeats(s,k))
    