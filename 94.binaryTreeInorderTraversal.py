
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        # def inorder(node):
        #     if node.left != None:
        #         inorder(node.left)
        #     res.append(node.val)
        #     if node.right != None:
        #         inorder(node.right)

        res = []
        inorder(root)
        return res
