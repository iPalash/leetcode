# Link: https://leetcode.com/problems/longest-valid-parentheses/

## Example

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

## Constraints
- len<3*10^4
- only ) or (

## Idea
- Store the indices in a stack
- Push the ( idx into the stack
- Pop the stack when ) and then calculate len by peeking 
- In case stack becomes empty, push the current idx
