
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS
class Solution:
    def __init__(self):
        self.res = []

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.dfs_level(root, 0)
        return self.res

    def dfs_level(self, node, level):
        if not node:
            return
        if level >= len(self.res):
            self.res.append([])
        self.res[level].append(node.val)
        self.dfs_level(node.left, level + 1)
        self.dfs_level(node.right, level + 1)

# BFS

# from collections import deque
# class Solution:
#     def levelOrder(self, root):
#         if not root: return []
#         queue, res = deque([root]), []

#         while queue:
#             cur_level, size = [], len(queue)
#             for i in range(size):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#                 cur_level.append(node.val)
#             res.append(cur_level)
#         return res
