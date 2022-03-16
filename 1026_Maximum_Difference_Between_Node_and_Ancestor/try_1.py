# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def minmax(node):
            nonlocal ans
            if not node:
                return float('inf'), 0
            if not node.left and not node.right:
                return node.val, node.val
            
            left_min, left_max = minmax(node.left)
            right_min, right_max = minmax(node.right)
            
            ans = max(ans, abs(node.val - min(left_min, right_min)), abs(node.val - max(left_max, right_max)))
            
            return min(left_min, right_min, node.val), max(left_max, right_max, node.val)
        
        minmax(root)
        return ans