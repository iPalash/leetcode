# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class ListNode:
	def __init__(self,val=0,next=None) -> None:
		self.val = val
		self.next = next

def constructLL(nums:list[int])-> ListNode:
	if len(nums)==0:
		return None
	head = ListNode(nums[0],constructLL(nums[1:]))
	return head

def printNil(curr:ListNode):
	if curr!=None:
		print(curr.val,end=",")
	else:
		print("None",end=",")

def swap(curr, prv, prv2, i):
	# print(curr.val)
	# list(map(printNil,[prv2,prv,curr]))
	# print(i)
	if curr==None:
		return curr
	if i%2==0:
		#update prv2.next
		#swap prv and curr
		#update prv2,prv,curr
		if prv2:
			prv2.next=curr
		nxt = curr.next
		curr.next=prv
		prv.next=nxt
		prv2=curr
		curr = nxt
	else:
		#do nothing?
		prv2=prv
		prv=curr
		curr=curr.next
	swap(curr,prv,prv2,i+1)
	# printNil(curr)
	return curr

def printLL(head:ListNode):
	while head!=None:
		print(head.val)
		head=head.next
class Solution:
	def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
		dummy = ListNode(0, head)
		prv, curr = dummy, head
		while curr and curr.next:
			prv.next = curr.next
			curr.next = curr.next.next
			prv.next.next = curr
			prv,curr= curr,curr.next 
		# printLL(dummy.next)
		return dummy.next

s=input()
arr=[int(el) for el in s[1:-1].split(",")]
head = constructLL(arr)
print(Solution().swapPairs(head))