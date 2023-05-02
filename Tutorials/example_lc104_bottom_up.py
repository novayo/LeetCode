# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def recr(node, curDepth):
            nonlocal ans
            if not node:
                return
            
            curDepth += 1
            ans = max(ans, curDepth)
            
            recr(node.left, curDepth)
            recr(node.right, curDepth)
        
        recr(root, 0)
        return ans
            
