
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def issym(l,r):
            if not l and not r:
                return True
            elif not l or not r or l.val != r.val:
                return False
            return issym(l.left, r.right) and issym(r.left, l.right)

        return issym(root, root)
