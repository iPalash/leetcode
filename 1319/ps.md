# Link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/

## Constraints

- n<10^5
- No repeated connections
- No two are connected by more than 1 cable

## Idea

- Get the number of connected components -> this is standard
- Get the number of redundant cables -> count an edge when we encounter an already visited node
- Ans should be connComponents-1 if number of extra cable is more than that else -1
