from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
def construct(arr:list[int]) -> ListNode:
    if len(arr)==0:
        return None
    return ListNode(arr[0],construct(arr[1:]))

def printLL(head):
    a=""
    while head!=None:
        a+="{},".format(head.val)
        head=head.next
    print(a)

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101,head)
        prv = dummy
        curr = head
        deleted = None
        while curr:
            print(prv.val,curr.val,deleted)
            if curr.next and curr.val==curr.next.val:
                ##Delete both
                deleted=curr.val
                prv.next = curr.next.next
                curr = prv.next
            elif deleted!=None and curr.val==deleted:
                prv.next = curr.next
                curr = prv.next
            else:
                deleted=None
                prv = curr
                curr = curr.next
        printLL(dummy.next)
        return dummy.next


nums = [int(el) for el in input()[1:-1].split(",")]
head = construct(nums)
printLL(head)
print(Solution().deleteDuplicates(head))
