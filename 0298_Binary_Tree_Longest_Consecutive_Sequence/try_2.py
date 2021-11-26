# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and node.left.val - node.val != 1:
                left = 0
            
            if node.right and node.right.val - node.val != 1:
                right = 0
            
            current = max(left, right) + 1
            ans = max(ans, current)
            return current
        
        dfs(root)
        return ans
            
