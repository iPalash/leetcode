# Link: <https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/>

## Example

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]


## Constraints

- list is sorted in asc order
- nodes.len<=300

## Idea

Just del both nodes when curr=curr.next also having prev to point to curr.next.next
Also take care of when that deleted matches the next

!TODO the solutions seems slow, think upon a faster one without using the deleted jugaad
Nevermind it wasn't slow, just too much printing but still find a cleaner way for this.
