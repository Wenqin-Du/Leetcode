
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # Method 1

        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

        # Method 2 update simultaneously

        dummy = ListNode(float("-inf"))

        while head:
            dummy.next, head.next, head = head, dummy.next, head.next

        return dummy.next
