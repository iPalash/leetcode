# Link: https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

## Example

## Constraints

- m,n<=100

## Idea

- Just dfs on the min cost path and backtrack to the next best if 0,0 isn't reachable
- The first took too long since we were trying unnecessary long paths, just a simple bfs solves this in time
- An optimization is while inserting to queue we either insert to first or last position based on cost incr
