# Link: <https://leetcode.com/problems/populating-next-right-pointers-in-each-node/>

## Example

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

## Constraints

- It is a perfect binary tree
- Only use constant extra space (recursive is fine, assume implicity stack space doesn't count extra)

## Idea

- We have done this before but that was a level order traversal using extra space, how to do this without that?
- set left.next = right and right.next = parent, now for on right, set next to right.next.next.left (snce the next of previous levels are now set correctly to that will give parent.next.left)
