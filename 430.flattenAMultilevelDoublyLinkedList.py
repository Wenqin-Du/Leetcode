
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        stack = [head]
        last = None
        while stack:
            temp = stack.pop()
            if last:
                last.next, temp.prev = temp, last
            last = temp
            if temp.next:
                stack.append(temp.next)
            if temp.child:
                stack.append(temp.child)
                temp.child = None
        return head
