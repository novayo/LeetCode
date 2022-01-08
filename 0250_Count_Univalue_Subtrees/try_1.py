# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            
            if not node:
                return True
            
            left = dfs(node.left)            
            right = dfs(node.right)
            
            ret = left and right
            
            # if left and right are valid and val is equal to me
            if ret and ((not node.left or node.left.val == node.val) and (not node.right or node.right.val == node.val)):
                ans += 1
            else:
                ret = False
            
            return ret
        
        dfs(root)
        return ans
            
