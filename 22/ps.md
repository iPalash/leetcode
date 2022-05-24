# Link: <https://leetcode.com/problems/generate-parentheses/>

## Example

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]


## Constraints

- 1<=n<=8

## Idea

- insert a ) or ( but keeping close-open>=0
- This is related to Closure Number and the catalan number for its time complexity analysis !TODO looks into this
