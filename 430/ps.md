Link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/submissions/

nput: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

Constraints:
nodes<1000

Idea:
Simple dfs
The challenging part was reading the list