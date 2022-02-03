Link: https://leetcode.com/problems/largest-plus-sign/

Input:
5
[[4,2]]

Example 1:
Input: n = 5, mines = [[4,2]]


1  1  1  1  1
1  1  1  1  1
1  1  1  1  1
1  1  1  1  1
1  1  0  1  1 

Output: 2
Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.


Idea:
For every direction, L R U D: store value to first zero or end assuming that to be centre. This would be the max length of the arm in that direction

This would require two loops:
fist starting top left (fills R U) another starting bottom right (fills L D)
