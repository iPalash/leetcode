# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, Tuple

class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left= left
        self.right=right

def constructTree(arr:list[int]) -> TreeNode:
    if len(arr)==0:
        return None
    root = TreeNode(arr[0])
    nodes={}
    nodes[1]=root
    for i,val in enumerate(arr[1:]):
        if val:
            idx = i+2
            curr = TreeNode(val)
            parent=(idx//2)
            # print(idx, val, parent)
            if idx%2==0:
                #left 
                # print("{} is left of {}".format(val, nodes[parent].val))
                nodes[parent].left=curr
            else:
                # print("{} is right of {}".format(val, nodes[parent].val))
                nodes[parent].right=curr
            nodes[idx]=curr
    return root


def lca(root:TreeNode, a, b):
    if root==None or root.val==a or root.val==b:
        return root
    left = lca(root.left, a, b)
    right = lca(root.right, a, b)
    if left!=None and right!=None:
        return root
    elif left!=None:
        return left
    else:
        return right

def paths(start:TreeNode, val:int, path:list=[]) -> bool:
    # print(start,val,path)
    if start==None:
        return False
    if start.val==val:
        return True
    path.append("L")
    if paths(start.left,val,path):
        return True
    path.pop()
    path.append("R")
    if paths(start.right,val,path):
        return True
    path.pop()
    return False
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # print(root.val, startValue,destValue)
        # (path_s,anc_s)=find(root,startValue)
        # (path_e,anc_e)=find(root,destValue)
        i=0
        lca_n = lca(root,startValue,destValue)
        left = []
        right = []
        paths(lca_n, startValue, left)
        paths(lca_n, destValue, right)
        print(left,right)
        right = "".join(right)
        left = "U"*len(left)
        return left+right
if __name__=='__main__':
    s = input()
    arr = [(lambda x: int(el) if el!="null" else None)(el) for el in s[1:-1].split(',')]
    start = int(input())
    end = int(input())
    # print(arr,start,end)
    print(Solution().getDirections(constructTree(arr),start,end))