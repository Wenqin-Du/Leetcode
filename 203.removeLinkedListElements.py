
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        # Method 1

        while head.val == val:
            head = head.next
        temp = head
        while temp and temp.next:
            if temp.next == val:
                temp.next = temp.next.next
                temp = temp.next.next
            else:
                temp = temp.next
        return head

        # Method 2: Recursively

        if not head:
            return None
        if head.val == val:
            head = self.removeElements(head.next,val)
        else:
            head.next = self.removeElements(head.next,val)
        return head

