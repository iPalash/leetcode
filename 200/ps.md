# Link: <https://leetcode.com/problems/number-of-islands/>

## Example

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

## Constraints

- 1<=m,n<=300

## Idea

- An island is basically 1 single component
- Do a dfs starting at i,j and then visit all
