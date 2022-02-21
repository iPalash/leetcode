# Link: <https://leetcode.com/problems/shortest-path-in-binary-matrix/>

## Example

Input: grid = [[0,1],[1,0]]
Output: 2

## Constraints

- 1<=n<=100
- grid[i] is 0 or 1

## Idea

- A simple bfs
- Forgot an edge case with a single element matrix
- An optimisation here could be using A* search where instead of a complete bfs we expand on the node with best heuristic guess towards our destination !TODO

