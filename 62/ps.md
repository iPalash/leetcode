# Link: <https://leetcode.com/problems/unique-paths/>

## Example

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

## Constraints

- 1<=m,n<=100

## Idea

- dp[i][j] = dp[i+1][j]+dp[i][j+1]
- Can reduce it to just two size column arrays prv and curr & Return curr[0] at the end
