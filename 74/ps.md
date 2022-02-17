# Link: <https://leetcode.com/problems/search-a-2d-matrix//>

## Example

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

## Constraints

- m,n<=100

## Idea

Binary search b/w (0,r*c)
0,20
10
row=4: =>2
col=5: =>0
10=>(2,0)
row = i//c
col = i%c