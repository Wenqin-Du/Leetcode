
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return head

        dummy, count = head, 0
        while dummy:
            dummy = dummy.next
            count += 1
        if k % count == 0:
            return head

        slow = fast = head

        for _ in range(k % count):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        fast.next = head

        return temp
