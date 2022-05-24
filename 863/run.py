# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
from typing import DefaultDict, Optional, Tuple

class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left= left
        self.right=right

def constructTree(arr:list[int]) -> TreeNode:
    if len(arr)==0:
        return None
    root = TreeNode(arr[0])
    nodes=[root]
    for i,val in enumerate(arr[1:]):
        if val:
            idx = i
            curr = TreeNode(val)
            parent=(idx//2)
            print(idx, val, parent)
            if idx%2==0:
                #left 
                # print("{} is left of {}".format(val, nodes[parent].val))
                nodes[parent].left=curr
            else:
                # print("{} is right of {}".format(val, nodes[parent].val))
                nodes[parent].right=curr
            nodes.append(curr)
    return root


def find(node, target):
    if node:
        if node.val==target:
            return node
        return find(node.left,target) or find(node.right,target)
    return None

class Solution:

    def findK(self, node, k):
        if k==0 and node:
            self.ans.append(node.val)
        if node:
            self.findK(node.left,k-1)
            self.findK(node.right,k-1)
    
    def postorder(self, node, target, k, d):
        if not node:
            return False, -1
        if node.val==target.val:
            # Get all nodes k dist from here in the subtree
            self.findK(node,k)
            return True, d
        foundL,distL = self.postorder(node.left,target,k,d+1)
        foundR,distR = self.postorder(node.right,target,k,d+1)
        if (foundL or foundR):
            # get all nodes k-dist from here in its subtree (the one with found as false)
            dist = distL if distL!=-1 else distR
            print(node.val,dist,foundL,foundR)
            distanceToTarget = dist-d
            if distanceToTarget==k:
                self.ans.append(node.val)
            elif foundL and k>distanceToTarget:
                self.findK(node.right, k-distanceToTarget-1)
            elif foundR and k>distanceToTarget:
                self.findK(node.left,k-distanceToTarget-1)

            return True, dist
        return False, -1



    def distanceK(self, root: TreeNode, target: TreeNode, k: int)-> list[int]:
        print(root.val, target.val, k)
        self.ans=[]
        
        self.postorder(root,target,k,0)

        return self.ans

arr = [(lambda x: int(el) if el!="null" else None)(el) for el in input()[1:-1].split(',')]
target = int(input())
k = int(input())

root = constructTree(arr)
target = find(root,target)

print(Solution().distanceK(root,target,k))
