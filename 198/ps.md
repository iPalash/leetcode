# Link: <https://leetcode.com/problems/house-robber/>

## Example

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4. 

## Constraints

- nums.len<=100
- 0<=nums[i]<=400

## Idea

- take max(last-2 + curr, last-1 - lastelement + curr)
