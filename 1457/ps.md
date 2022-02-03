Link:https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/



Input: root = [2,3,1,3,1,null,1]
      2
   3     1
3    1      1


Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).


Idea
On every path keep counting digits 0-9 so far


If height is even:
All digits must have even count

If height is odd:
All digits bar one must have even count


A Simple graph traversal maintaining a dp of digit count being even or odd worked