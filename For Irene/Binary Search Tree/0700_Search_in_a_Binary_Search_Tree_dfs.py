# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        ans = None
        
        def dfs(node):
            
            nonlocal ans
            
            if ans:
                return
            
            if not node:
                return
            
            if node.val == val:
                ans = node
                return
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ans