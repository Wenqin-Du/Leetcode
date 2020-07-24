"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.root_node = root # make a copy to return the result
        curr = temp = Node(0)
        while root:
            while root:
                if root.left:
                    curr.next = root.left
                    curr = root.left
                if root.right:
                    curr.next = root.right
                    curr = root.right
                root = root.next
            root = temp.next
            curr = temp
            curr.next = None

        return self.root_node
