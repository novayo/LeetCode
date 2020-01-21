# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if root == None: return 0
        ans = 0
        
        def dfs(node, pre, count=0):
            nonlocal ans
            if not node:
                return
            
            if node.val == pre + 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 1
            pre = node.val
            
            dfs(node.left, pre, count)
            dfs(node.right, pre, count)
        
        dfs(root, root.val-1)
        return ans
