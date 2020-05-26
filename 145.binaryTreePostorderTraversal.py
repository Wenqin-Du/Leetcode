
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root, res):
            if not root: return
            else:
                dfs(root.left, res)
                dfs(root.right, res)
                res.append(root.val)
            return res
        return dfs(root, res)

