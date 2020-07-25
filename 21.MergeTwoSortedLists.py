# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        ### Method 1. while & needle
        curr = dummy = ListNode(0)

        while l1 and l2:

            if l1.next < l2.next:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2

        return dummy.next

        ### Method 2. Recursion
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            return ListNode(l1.val, self.mergeTwoLists(l1.next,l2))
        else:
            return ListNode(l2.val, self.mergeTwoLists(l1,l2.next))
