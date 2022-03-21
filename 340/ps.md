# Link: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

## Example

## Constraints

- len<10^4
- k->[0,50]

## Idea

- Maintain a map of char to count
- Keep incr j until distinct<=k
- On exceeeding, incr i until distinct becomes <=k
- Keep track of longest so far
