# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        target_depth = None
        ans = None
        
        def dfs(node, depth=0):
            nonlocal target_depth, ans
            
            if ans:
                return
            
            if not node:
                return
            
            if target_depth == depth:
                ans = node
                return
            
            if node == u:
                target_depth = depth
            
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        
        dfs(root)
        return ans
