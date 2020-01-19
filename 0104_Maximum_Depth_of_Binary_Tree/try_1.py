# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # dfs
        def dfs(node, ans, d):
            if not node:
                return d
            ans = max(ans, max(dfs(node.left, ans, d+1), dfs(node.right, ans, d+1)))
            return ans
        
        return dfs(root, 0, 0)
