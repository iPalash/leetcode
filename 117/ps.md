# Link: <https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/>

## Example

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

## Constraints

- It is not a perfect binary tree
- Only use constant extra space (recursive is fine, assume implicity stack space doesn't count extra)

## Idea

- Just like 116 but with for finding next we need to have a recursive logic to find the leftmost node of the next level
- This one had a few edge cases, like None nodes not being in the array for parent lookup
- Another one was how to traverse the tree, node right and then left else few next pointer would be missed since next won't be set for the right side of the tree
