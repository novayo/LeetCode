# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def recr(node):
            nonlocal ans
            if not node:
                return float('inf'), -float('inf')
            
            ret_min = ret_max = node.val
            if node.left:
                left_min, left_max = recr(node.left)
                ans = max(ans, abs(node.val - left_max), abs(node.val - left_min))
                ret_min = min(ret_min, left_min)
                ret_max = max(ret_max, left_max)
            
            if node.right:
                right_min, right_max = recr(node.right)
                ans = max(ans, abs(node.val - right_max), abs(node.val - right_min))
                ret_min = min(ret_min, right_min)
                ret_max = max(ret_max, right_max)
            
            return ret_min, ret_max
        
        recr(root)
        return ans
