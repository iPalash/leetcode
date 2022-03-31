"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
import heapq

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.ans = 0
        self.traverse(root)
        return self.ans
    def traverse(self,node):
        if node==None:
            return 0
        h = []
        for child in node.children:
            heapq.heappush(h,-self.traverse(child))
        p = 0
        mx=0
        if len(h)>0:
            mx = -heapq.heappop(h) 
            p+=mx
        if len(h)>0:
            p-=heapq.heappop(h)
        self.ans=max(self.ans,p)
        return 1+mx
                
