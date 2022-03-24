# Link: https://leetcode.com/problems/kill-process/

## Example

## Constraints

- n<=5x10^4
- Only 1 process is root
- All pids are unique

## Idea

- Construct a tree with root process as the root node
- Also maintain a hash from pid to treenode
- Return the subtree including the node as the ans
