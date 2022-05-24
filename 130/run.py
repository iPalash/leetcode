class Solution:
    def dfs(self, board, r, c):
        if board[r][c]=='O':
            board[r][c]='V'
            if r-1>=0:
                self.dfs(board,r-1,c)
            if r+1<len(board):
                self.dfs(board,r+1,c)
            if c-1>=0:
                self.dfs(board,r,c-1)
            if c+1<len(board[0]):
                self.dfs(board,r,c+1)
    def solve(self, board: list[list[str]]) -> None:
        print(board)
        m=len(board)
        n=len(board[0])
        for r in range(m):
            for c in range(n):
                # Find a border 0
                if (r==0 or c==0 or r==m-1 or c==n-1) and board[r][c]=='O':
                    self.dfs(board,r,c)
        for r in range(m):
            for c in range(n):
                if board[r][c]=='O':
                    board[r][c]='X'
                if board[r][c]=='V':
                    board[r][c]='O'
        print(board)
                    



board = [[s for s in el[1:-1].split('","')] for el in input()[2:-2].split("],[")] 
print(Solution().solve(board))


