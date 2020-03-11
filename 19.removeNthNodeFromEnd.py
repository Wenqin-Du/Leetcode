
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dummy = ListNode(128)
        dummy.next = head
        slow = fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:  # 表示当 fast.next 还有元素时 (在 NULL 时停下循环)
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
