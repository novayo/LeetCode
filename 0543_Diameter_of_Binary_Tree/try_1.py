# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node, layer=0):
            nonlocal ans
            if not node:
                return layer
            
            left = dfs(node.left, layer+1)
            right = dfs(node.right, layer+1)
            
            ans = max(ans, left-layer-1 + right-layer-1)
            return max(left, right)
        
        ans = 0
        dfs(root)
        return ans
