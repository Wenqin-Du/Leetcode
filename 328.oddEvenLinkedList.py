
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy1 = odd = ListNode(float('inf'))
        dummy2 = even = ListNode(float('inf'))

        while head:
            odd.next, even.next = head, head.next
            odd, even = odd.next, even.next

            if even:
                head = head.next.next
            else:
                head = None

        odd.next = dummy2.next

        return dummy1.next

