# Link: <https://leetcode.com/problems/all-paths-from-source-to-target/>

## Example

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.


## Constraints

- graph is a DAG
- 2<=n<=15
- No self loops
- All are unique

## Idea
- Just do bfs until we reach n-1 starting at 0
- Since it is a DAG, we don't even need to maintain a visited array
