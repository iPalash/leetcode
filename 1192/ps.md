# Link: https://leetcode.com/problems/critical-connections-in-a-network/

## Example

## Constraints

- 2<=n<=10^5
- conns.len<10^5
- No self conns and no repeated edges

## Idea

- Start at any node and keep track of the rank (first discovered distance)
- On encounter any node which already has a lower rank than curr, this is a cycle, return the lower and check recusively and remove edges (since they constitute a cycle and a critical edge can never be a cycle)
- Explore tarjan's for this sometime later !TODO !RETRY

