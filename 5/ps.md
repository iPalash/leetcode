# Link: <https://leetcode.com/problems/longest-palindromic-substring/>

## Example

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

## Constraints

- 1<=s.len=1000
- only digits and english letters

## Idea

- The brute way of doing this is if s[0]==s[-1] then 1+pal(s[1:-1]) else max(pal(s[0:-1]),pal(s[1:]))
