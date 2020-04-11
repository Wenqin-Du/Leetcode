
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root: return 0
        self.k = k
        self.res = 0

        def inorder(node):
            if not node: return

            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val

            inorder(node.right)

        inorder(root)
        return self.res

#         Same idea:

#         if not root: return 0
#         self.res = 0
#         self.k = k
#         self.dfs(root)
#         return self.res

#     def dfs(self, node):
#         if not node: return

#         self.dfs(node.left)
#         self.k -= 1
#         # print(self.k)
#         if self.k == 0:
#             self.res = node.val

#         self.dfs(node.right)

