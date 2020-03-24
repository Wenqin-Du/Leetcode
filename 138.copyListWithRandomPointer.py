
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:

    def __init__(self):
        self.visitedDict = {}

    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head: return None

        if head in self.visitedDict:
            new_node = self.visitedDict[head]
            return new_node
        else:
            new_node = Node(head.val, None, None)
            self.visitedDict[head] = new_node
            new_node.next = self.copyRandomList(head.next)
            new_node.random = self.copyRandomList(head.random)
            return new_node



        
