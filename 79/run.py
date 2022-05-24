class Solution:
    def dfs(self, board, word, visited, i, x, y, m,n,l):
        #print(visited,i,l)
        if i==l:
            return True
        adj = [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
        for [a,b] in adj:
            if 0<=a<m and 0<=b<n and board[a][b]==word[i] and visited[a][b]==0:
                visited[a][b]=1
                if self.dfs(board,word,visited,i+1,a,b,m,n,l):
                    return True
                visited[a][b]=0
        return False
    def exist(self, board: list[list[str]], word:str) -> bool:
        #print(board,word)
        m = len(board)
        n = len(board[0])
        l = len(word)
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for x in range(m):
            for y in range(n):
                if board[x][y]==word[0]:
                    visited[x][y]=1
                    if self.dfs(board, word, visited, 1, x,y, m,n,l):
                        return True
                    visited[x][y]=0
        return False


board = [[el for el in s[1:-1].split('","')] for s in input()[2:-2].split("],[")]
word = input()[1:-1]
print(Solution().exist(board,word))

