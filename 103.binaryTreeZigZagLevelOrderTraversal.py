
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []
        queue, res = deque([root]), []
        sign = -1

        while queue:
            sign, cur_level, size = -sign, [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level[::sign])

        return res



