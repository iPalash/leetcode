from collections import deque

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #print(board)
        row = [set(range(1,10)) for _ in range(9)]
        col = [set(range(1,10)) for _ in range(9)]
        squares = [set(range(1,10)) for _ in range(9)]
        dots = deque([])
        def findSquare(r,c):
            return (r//3)*3+(c//3)
        for r in range(9):
            for c in range(9):
                if board[r][c]!=".":
                    row[r].remove(int(board[r][c]))
                    col[c].remove(int(board[r][c]))
                #    print(r,c,(r//3)*3+(c//3))
                    squares[(r//3)*3+(c//3)].remove(int(board[r][c]))
                else:
                    dots.append([r,c])
        
        def candidates(row,col,squares):
            cand = []
      #      print(row,col,squares)
            for x in row:
                if x in col and x in squares:
                    cand.append(x)
            return cand
        
        def solver(dots,row,col,squares):
            if len(dots)==0:
                return True
            [r,c] = dots.popleft()
            cand = candidates(row[r],col[c],squares[findSquare(r,c)])
            #print("candidates at {},{} are {}".format(r,c,cand))
            for x in cand:
                row[r].remove(x)
                col[c].remove(x)
                squares[findSquare(r,c)].remove(x)
             #   print("Trying {} at ({},{})".format(x,r,c))
                board[r][c]=str(x)
                res = solver(dots,row,col,squares)
                if res:
                    return True
                board[r][c]='.'
                row[r].add(x)
                col[c].add(x)
                squares[findSquare(r,c)].add(x)
            dots.appendleft([r,c])
            return False
        solver(dots,row,col,squares)
                
            
            
            
            
        
        
