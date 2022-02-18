# Link: <https://leetcode.com/problems/container-with-most-water/>

## Example

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

## Constraints

- n<=10^5

## Idea

- Keep two pointers left and right & change acc to which area is greater while maintaining the max
- Instead of deciding by which area is greater switch to the next greater line of the min of current 
