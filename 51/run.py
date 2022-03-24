class Solution:
    def solveNQueens(self, n:int) -> list[list[str]]:
        
        queens = [] 
        def solve(i,prev):
            # processing ith ro
            #print(i,prev)
            if i<n:
                # find j such that no queen placed in the previous rows is in conflict
                for j in range(n):
                    # Avoid same column
                    if j in prev:
                        #print("Pos {} conflicts with before {} in {}".format(j,j,prev))
                        continue
                    # Avoid either diagonals
                    ## rights
                    conflict=False
                    for idx,k in enumerate(prev):
                        if (right:=k+(i-idx))<n and right==j:
                            #print("Pos {} conflicts with before {} in {}".format(j,k,prev))
                            conflict=True
                            break
                    if conflict:
                        continue
                    ## left
                    for idx,k in enumerate(prev):
                        if (left:=k-(i-idx))>=0 and left==j:
                            #print("Pos {} conflicts with before {} in {}".format(j,k,prev))
                            conflict=True
                            break
                    if conflict:
                        continue

                    # Found a possible move
                #    print("Possible in row {}".format(i),prev,j)
                    prev.append(j)
                    solve(i+1,prev)
                    prev.pop()
            else:
                queens.append(prev.copy())
                

        solve(0,[])

        ans = []

        for q in queens:
            ans.append([['.' for _ in range(n)] for _ in range(n)])
            for i,piece in enumerate(q):
                ans[-1][i][piece]='Q'
            ans[-1]=[''.join(el) for el in ans[-1]]



        return ans

n = int(input())

print(Solution().solveNQueens(n))
