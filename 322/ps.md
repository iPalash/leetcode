# Link: <https://leetcode.com/problems/coin-change/>

## Example

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

## Constraints

- coint.len <=12
- n < 10^4

## Idea

- dp[n] = min(for every coin in coins c : dp[n-c]+1)
- can also do bfs for this 
