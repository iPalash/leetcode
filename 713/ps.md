# Link: <https://leetcode.com/problems/subarray-product-less-than-k/>

## Example

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

## Constraints

- 1<=nums.len<3x10^4
- 0<=k<=10^6
- 1<=nums[i]<=1000

## Idea

- The idea was to keep track of the best index from i satisfying the condition and resue it to calculate forward
- Took way too long to implement the idea, probably because I was married to the idea of not repeating a few things way too much
