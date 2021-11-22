# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def postorder(node):
            if not node:
                return 0
            
            left = postorder(node.left)
            right = postorder(node.right)
            
            return max(left, right) + 1
        
        return postorder(root)
