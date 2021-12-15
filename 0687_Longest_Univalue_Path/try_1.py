# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            
            if not node:
                return 0
            
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            
            ret = 0
            cur = 1
            if node.left and node.left.val == node.val:
                ret = max(ret, left_length)
                cur += left_length
            
            if node.right and node.right.val == node.val:
                ret = max(ret, right_length)
                cur += right_length
            
            ans = max(ans, cur - 1)
            
            return ret + 1
        
        dfs(root)
        return ans
