# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        # non-tail recursion
        def recr(node, depth=0):
            if not node:
                return depth
            
            return max(recr(node.left, depth+1), recr(node.right, depth+1))
        
        return recr(root)