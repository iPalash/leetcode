class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        # In place rotate by 90 degree

        n = len(matrix)
        start = 0
        end = n-1
        while start<end:
            for i in range(start,end):
                matrix[start][i],matrix[i][n-1-start],matrix[n-1-start][n-i-1],matrix[n-1-i][start]=matrix[n-1-i][start],matrix[start][i],matrix[i][n-1-start],matrix[n-1-start][n-i-1]
            start+=1
            end-=1


matrix= [[int(el) for el in row.split(',')] for row in input()[2:-2].split('],[')]

print(Solution().rotate(matrix))
