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
            print("at node with value: {}".format(node.val))
            if node.next:
                print("next of {} is {}".format(node.val,node.next.val))
            if node.left:
                if node.right:
                    node.left.next=node.right
                else:
                    nxt = node.next
                    f = None
                    while nxt!=None:
#                        print("{} is at left whose next might be {}".format(node.left.val,nxt.val))
                        if nxt.left:
                            f=nxt.left
                            break
                        if  nxt.right:
                            f=nxt.right
                            break
                        nxt=nxt.next
                    if f:
                        node.left.next=f
                #print("next of {} is {}".format(node.left.val,node.right.val))
            if node.right:
                if node.next:
                    nxt = node.next
                    f = None
                    while nxt!=None:
                        if nxt.left:
                            f=nxt.left
                            break
                        if nxt.right:
                            f=nxt.right
                            break
                        nxt=nxt.next
                    if f:
                        node.right.next=f
            self.traverse(node.right)
            self.traverse(node.left)

    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root==None:
            return root
        self.traverse(root)
        return root


def intNull(s):
    if s=='null':
        return None
    else:
        return int(s)
arr = [intNull(el) for el in input()[1:-1].split(',')]

def readTree(arr):
    nodes = []
    root = None
    for i,el in enumerate(arr):
        if root==None:
            root = Node(el)
            curr = root
        elif el!=None:
            curr = Node(el)
        else:
            continue
        nodes.append(curr)
        if i>0:
            parentIdx=(i-1)//2
            isLeft = i%2==1
            #print(i,el, parentIdx,isLeft, len(nodes))
            if isLeft:
                #print("{} is left to {}".format(curr.val,nodes[parentIdx].val))
                nodes[parentIdx].left=curr
            else:
                #print("{} is right to {}".format(curr.val,nodes[parentIdx].val))
                nodes[parentIdx].right=curr
    return root
root = readTree(arr)

print(Solution().connect(root))

