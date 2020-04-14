
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        f = s = ListNode(float("Inf"))
        f = s = head
        stack = []

        while f and f.next:
            stack.append(s.val)
            s = s.next
            f = f.next.next

        if f:
            s = s.next

        while s:
            if stack.pop() != s.val:
                return False
            s = s.next

        return True
        
