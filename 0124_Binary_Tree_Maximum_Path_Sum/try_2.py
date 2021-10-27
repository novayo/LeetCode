# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def postorder(node):
            nonlocal ans
            if not node:
                return 0
            
            left = postorder(node.left)
            right = postorder(node.right)
            
            ans = max(ans, node.val, left + node.val, right + node.val, left + right + node.val)
            
            return max(max(left, right) + node.val, node.val)
            
        ans = -float('inf')
        postorder(root)
        return ans