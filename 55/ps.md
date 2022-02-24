# Link: <https://leetcode.com/problems/jump-game/>

## Example

- Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

## Constraints

- nums.len<=10^4 (so no poly algo)

## Idea

- Maintain a min j for which last index is reachable
- Go reverse and see if either j or n-1 itself is reachable
