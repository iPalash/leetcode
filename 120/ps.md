Link: https://leetcode.com/problems/triangle/

Input:
[[2],[3,4],[6,5,7],[4,1,8,3]]

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

- While moving down can only move to i or i+1 of the next row

brute force would be:
using n2 space
save dp[x][y] = el[x][y]+max(dp[x-1][y],dp[x-1][y-1])

Stretch: Using only o(n) space  [n=>numbers of rows]
