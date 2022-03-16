# Link: https://leetcode.com/problems/sliding-window-maximum/

## Example

## Constraints

## Idea

- Use a heap

- A crude impl using array is too slow since insert or delete is O(n) even though finding the indices is just o(logk), need to use a heap to do this faster in logK
- Solved in linear time after seeing the solution !RETRY
- This could also have been done in linear using the same ideas as trapping rain water. For getting the max of a range, get the max of left_block[end] and right_block[start]
