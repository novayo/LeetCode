# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        memo = collections.defaultdict(bool)
        def dfs(node, curSum):
            if not node:
                memo[node, curSum] = False
                return memo[node, curSum]
            
            if (node, curSum) in memo:
                return memo[node, curSum]
            
            curSum += node.val
            if node.left is None and node.right is None:
                memo[node, curSum] = curSum == targetSum
                return memo[node, curSum]
            
            left_ret = dfs(node.left, curSum)
            right_ret = dfs(node.right, curSum)
            
            memo[node, curSum] = left_ret or right_ret
            return memo[node, curSum]
        
        return dfs(root, 0)
