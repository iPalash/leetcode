Link: https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
Output: 3


Constraints:
All times are unique

Idea:
sort the times and find the first time where all nodes are connected

A list was the simple way of doing this

Maybe try doing this faster with a tree 

Union find