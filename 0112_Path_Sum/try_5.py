# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, curSum):
            if not node:
                return False
            
            curSum += node.val
            if node.left is None and node.right is None:
                return curSum == targetSum
            
            left_ret = dfs(node.left, curSum)
            right_ret = dfs(node.right, curSum)
            
            return left_ret or right_ret
        
        return dfs(root, 0)
