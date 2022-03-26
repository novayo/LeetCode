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
                return float('inf'), float('inf')
            
            ret_small = ret_big = node.val
            if node.left:
                small, big = recr(node.left)
                ans = max(ans, abs(node.val - small), abs(node.val - big))
                ret_small = min(ret_small, small)
                ret_big = max(ret_big, big)
            
            if node.right:
                small, big = recr(node.right)
                ans = max(ans, abs(node.val - small), abs(node.val - big))
                ret_small = min(ret_small, small)
                ret_big = max(ret_big, big)
            
            return ret_small, ret_big
        
        recr(root)
        return ans
