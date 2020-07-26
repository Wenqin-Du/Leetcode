
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(l,r):
            if l == r:
                return [None]
            nodes = []
            for i in range(l,r):
                for lchild in helper(l,i):
                    for rchild in helper(i+1,r):
                        node = TreeNode(i+1)
                        node.left = lchild
                        node.right = rchild
                        nodes.append(node)
            return nodes
        return helper(0,n) if n else []
