# Link: <https://leetcode.com/problems/permutations-ii/>

## Example

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

## Constraints

- May have duplicates

## Idea

- All sets with some dedup strategy
- How to do this without dedup? Just sort the initial array and then skip processing over duplicates
