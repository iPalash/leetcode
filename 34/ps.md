# Link: <https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/>

## Example

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

## Constraints

- Nums is a non-decreasing array
- order should logn
- len <=10^5

## Idea

Binary search with a little modification to find first and last occurence

The trick was in what to return at the end and how to manipulate mid around
(i,j) in each case act as placeholder of left/right msot index
