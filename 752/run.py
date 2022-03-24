class Solution:
    def openLock(self, deadends: list[str], target:str) -> int:
        print(deadends, target)

        deadends = set(deadends)

        visited = {}
        q = [("0000",0)]

        def possibleMoves(s):
            moves = []
            for pos in range(4):
                val=int(s[pos])
                plusOne = (val+1)%10
                minOne = (val-1)%10
                moves.append(s[:pos]+str(plusOne)+s[pos+1:])
                moves.append(s[:pos]+str(minOne)+s[pos+1:])
            return moves

        while len(q)>0:
            pos, turn = q.pop(0)
            if pos in deadends:
                continue
            if pos==target:
                return turn
            for move in possibleMoves(pos):
                if move not in visited:
                    visited[move]=True
                    q.append((move,turn+1))
            
        return -1

deadends = [el for el in input()[2:-2].split('","')]
target = input()[1:-1]

print(Solution().openLock(deadends, target))
