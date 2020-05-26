
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        # Method 1: recursively
        res = []
        def dfs(root, res):
            if root:
                res.append(root.val)
                dfs(root.left, res)
                dfs(root.right, res)
            return res
        return dfs(root, res)

        # Method 2: iteratively
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res


