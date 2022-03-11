# Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

## Example

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

## Constraints

- n<500
- All are unique
- 0<=k<=1000
- target is in tree

## Idea
 
- Extra space or marking struct is easy
- Do dfs and backtrack using the depth of the target and the current node with traversing the other subtree when it makes sense acc to the distanceToTarget node and k
