# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, maxValue):
            nonlocal ans
            
            if not node:
                return
            
            if node.val >= maxValue:
                ans += 1
                maxValue = node.val
            
            dfs(node.left, maxValue)
            dfs(node.right, maxValue)
        
        dfs(root, root.val)
        return ans
