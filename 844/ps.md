# Link: <https://leetcode.com/problems/backspace-string-compare/>

## Example

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

## Constraints

- only lowercase and # characters
- try to find o(n) time and o(1) space solution

## Idea

The extra space is straightforward
Compute both strings and compare

for o(1) space, counter are needed for hashes and finally they should all be zero

This was more complicated than expected
The approach was to use two pointers to keep count of active 
Faced some impl issues ended up taking hint 

Retry this!