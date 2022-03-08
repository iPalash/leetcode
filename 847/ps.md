# Link: <https://leetcode.com/problems/shortest-path-visiting-all-nodes/>

## Example

Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

## Constraints

- 1<=n<=12
- No self links graph[i]!=i
- Reflective : graph[a] contains b then graph[b] contains a
- Input graph is always connected

## Idea

- A random idea is to visit the nodes which are the least connected
