# Link: https://leetcode.com/problems/shortest-distance-to-target-color/

## Example

Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).

## Constraints

- colors.len<5x10^4
- queries.len<5x10^4

## Idea

- Just store nearest 1,2,3 for every index and calculate that by a 2 pass first LR then RL using 3 pointers
