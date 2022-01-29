# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def recr(node):
            nonlocal ans
            if not node:
                return 0
            
            left = recr(node.left)
            right = recr(node.right)
            ans += abs(left) + abs(right)
            return left + right - 1 + node.val
        
        recr(root)
        return ans
