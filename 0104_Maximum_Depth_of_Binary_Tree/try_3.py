# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # bottom-up
        
        def bottomUp(node):
            if not node:
                return 0
            
            left = bottomUp(node.left)
            right = bottomUp(node.right)
            return max(left, right) + 1
        
        return bottomUp(root)