
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        needle = root

        while needle:
            if p.val > needle.val and q.val > needle.val:
                needle = needle.right
            if p.val < needle.val and q.val < needle.val:
                needle = needle.left
            else:
                return needle

        
