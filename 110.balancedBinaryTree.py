
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:
                return 0
            l_height, r_height = helper(root.left), helper(root.right)
            if l_height == -1 or r_height == -1 or abs(l_height - r_height) > 1:
                return -1
            return max(l_height, r_height) + 1
        return helper(root) != -1

