# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

## Example

## Constraints

- len<=5000
- prices[i] b/w [0,1000]

## Idea

- Trying brute force recursion first
- Options at every index are buy this or next => sell (if bought) this or next & then cd

- had to take a look at the solution to solve this, a 3-state dp was required, I was trying with just two
- The other DP solution looked like what I was trying to do but will take a look at it later, not getting the approach right now.
