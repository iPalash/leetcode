# Link: <https://leetcode.com/problems/surrounded-regions/>

## Example

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

## Constraints

- 1<=m,n<=200

## Idea

- Do a bfs starting from each of the unflippable borders 'O's.
- Flip everything else
- Missed the other case of border (len-1)
