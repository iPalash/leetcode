

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


def intNull(s):
    if s=='null':
        return None
    else:
        return int(s)

def readTree(arr):
    nodes = []
    root = None
    for i,el in enumerate(arr):
        if root==None:
            root = TreeNode(el)
            curr = root
        elif el!=None:
            curr = TreeNode(el)
        else:
            continue
        nodes.append(curr)
        if i>0:
            parentIdx=(i-1)//2
            isLeft = i%2==1
            #print(i,el, parentIdx,isLeft, len(nodes))
            if isLeft:
                print("{} is left to {}".format(curr.val,nodes[parentIdx].val))
                nodes[parentIdx].left=curr
            else:
                print("{} is right to {}".format(curr.val,nodes[parentIdx].val))
                nodes[parentIdx].right=curr
    return root

        
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        mx = 1

        def traverse(node):
            nonlocal mx
            if node:
                l = traverse(node.left)
                r = traverse(node.right)
                mx = max(1+l+r,mx)
                return max(l,r)+1
            return 0

        traverse(root)
        return mx


arr = [intNull(el) for el in input()[1:-1].split(',')]

print(Solution().diameterOfBinaryTree(readTree(arr)))

