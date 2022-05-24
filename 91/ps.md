# Link: <https://leetcode.com/problems/decode-ways/>

## Example

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

## Constraints

- 1<=s.len<=100
- s may contain leading zeros

## Idea

- dp[i] = 1+d[i+1] + 1 + dp[i+2] (both should be > 0 that is valid)
- Can do this with just 2 vars as well
