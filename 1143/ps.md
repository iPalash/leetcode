# Link: <https://leetcode.com/problems/longest-common-subsequence/>

## Example

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

## Constraints

- 1<length<1000

## Idea

- l[i][j] = max(1+l[i-1][j-1] if s[i]==s[j], l[i-1][j], l[i][j-1])
- optimise to use just a single array !TODO 
