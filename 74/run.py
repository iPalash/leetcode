class Solution:
    def searchMatrix(self, matrix: list[list[int]], target:int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        # print(rows,cols)
        start,end = 0, rows*cols
        while start<end:
            mid = (start+end)//2
            r,c=mid//cols,mid%cols
            # print(start,end,mid,r,c)
            if (el:=matrix[r][c])==target:
                return True
            if el>target:
                end = mid
            else:
                start=mid+1
        return False



arr=[[int(el) for el in s.split(",")] for s in input()[2:-2].split("],[")]
target =int(input())
print(arr,target)
print(Solution().searchMatrix(arr, target))
