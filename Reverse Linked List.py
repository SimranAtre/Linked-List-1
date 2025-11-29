# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head is None:
            return None
        prev=None
        curr=head
        fast=curr.next
        while fast is not None:
            curr.next = prev
            prev= curr
            curr=fast
            fast=fast.next
        curr.next=prev
        return curr
