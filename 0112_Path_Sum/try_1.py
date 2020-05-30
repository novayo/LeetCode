# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            if root.val == sum:
                return True
            else:
                return False
        
        ans = False
        def dfs(node, curval):
            nonlocal ans
            if ans:
                return
            
            if not node:
                return
            
            curval += node.val
            if curval == sum and not node.left and not node.right:
                ans = True
                return
            
            
            dfs(node.left, curval)
            dfs(node.right, curval)
            #curval -= node.val
        
        dfs(root, 0)
        return ans
