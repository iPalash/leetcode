# Link: https://leetcode.com/problems/find-a-peak-element-ii/

## Example

Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

## Constraints

- All positive
- Assume outer layer of -1s
- No adjacent cells are equal 
- m,n<=500

## Idea

- An O(max(N,M)) approach would be start from the mid and move towards the max, if the element itself is the max we found a peak
