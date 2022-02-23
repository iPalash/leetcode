class Node:
    def __init__(self, val:int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from typing import Optional

class Solution:
    def traverse(self, node: Node):
        if node!=None:
            if node.left:
                node.left.next=node.right
                print("next of {} is {}".format(node.left.val,node.right.val))
                self.traverse(node.left)
            if node.right:
                if node.next:
                    node.right.next=node.next.left
                self.traverse(node.right)

    def connect(self, root: Optional[Node]) -> Optional[Node]:
        print(root)
        if root==None:
            return root
        self.traverse(root)
        return root

arr = [int(el) for el in input()[1:-1].split(',')]

def readTree(arr):
    nodes = []
    root = None
    for i,el in enumerate(arr):
        if root==None:
            root = Node(el)
            curr = root
        else:
            curr = Node(el)
        nodes.append(curr)
        if i>0:
            parentIdx=(i-1)//2
            isLeft = i%2==1
            if isLeft:
                print("{} is left to {}".format(curr.val,nodes[parentIdx].val))
                nodes[parentIdx].left=curr
            else:
                print("{} is right to {}".format(curr.val,nodes[parentIdx].val))
                nodes[parentIdx].right=curr
    return root

root = readTree(arr)

print(Solution().connect(root))

