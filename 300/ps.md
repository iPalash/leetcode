# Link: <https://leetcode.com/problems/longest-increasing-subsequence/>

## Example

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

## Constraints

- nums.len<2500

## Idea

- A straightforward O(n2) approach is to store longest subsequence length ending at i in dp[i] and get max over all
