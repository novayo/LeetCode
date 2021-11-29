# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, current_val):
            if not node:
                return False

            if not node.left and not node.right:
                if current_val + node.val == targetSum:
                    return True
                else:
                    return False
            
            if dfs(node.left, current_val + node.val):
                return True
            if dfs(node.right, current_val + node.val):
                return True
            
            return False
        
        return dfs(root, 0)
