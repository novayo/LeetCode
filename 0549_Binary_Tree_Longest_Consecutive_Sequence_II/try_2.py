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
                return 0, 0
            
            inc = dec = 1
            
            if node.left:
                l_inc, l_dec = dfs(node.left)
                
                if node.val + 1 == node.left.val:
                    inc = max(inc, l_inc + 1)
                elif node.val - 1 == node.left.val:
                    dec = max(dec, l_dec + 1)
            
            if node.right:
                r_inc, r_dec = dfs(node.right)
                
                if node.val + 1 == node.right.val:
                    inc = max(inc, r_inc+1)
                elif node.val - 1 == node.right.val:
                    dec = max(dec, r_dec+1)
                
            ans = max(ans, inc + dec - 1)
            return inc, dec
        
        dfs(root)
        return ans
