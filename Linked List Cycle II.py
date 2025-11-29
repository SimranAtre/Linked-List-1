# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        # if head is None:
        #     return None
        # ans = False
        # slow = head
        # fast = head

        # while fast.next is not None and fast.next.next is not None:
        #     slow= slow.next
        #     fast= fast.next.next

        #     if slow == fast:
        #         ans= True
        #         break
        # if ans == False:
        #     return None

        # slow = head
        # while slow != fast:
        #     slow= slow.next
        #     fast = fast.next
        # return fast
        
        s= set()
        curr= head

        while curr is not None:
            if curr in s:
                return curr
            s.add(curr)
            curr=curr.next
        return None
    