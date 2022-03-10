# Link: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

## Example

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

## Constraints

- len<10^5
- only english letters

## Idea

- Keep start, next and last 2 chars
- Update next when a different char comes
- Reset start when a 3rd char appears
