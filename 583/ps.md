# Link: <https://leetcode.com/problems/delete-operation-for-two-strings/>

## Example

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".


## Constraints

- 1<length<500

## Idea

- Just find LCS and then (l1+l2-lcs) is the ans

- Try this some other time as a simple DP without using LCS and finding edit directly
