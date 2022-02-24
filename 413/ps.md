# Link: <https://leetcode.com/problems/arithmetic-slices/>

## Example

-Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

## Constraints

- nums.len<=1000
- -1000<=nums[i]<=1000

## Idea

- Starting at i find max cnt such that that subarray is an AP. Then number subarrays would be (n2-3n+2)/2 
- Impl is a bit complicated. !TODO retry to simplify
