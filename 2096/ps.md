# Link: <https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/>

## Example

Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

## Constraints

All node val are unique
2<=n<=10^5

## Idea

The idea was straightforward
find LCA
get LCA to start (left)
get LCA to end (right)
answer would be (len(left)*U)+right

Challenge was in impl.

Algo for getting the lca without calculating common path was to mark each subtree with the node value
Then getting the path without using extra mem was contigent on pass by reference property of python args (go or c it would be pointers)
