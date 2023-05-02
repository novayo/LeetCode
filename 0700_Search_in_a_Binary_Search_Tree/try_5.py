# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = None
        def recr(node):
            nonlocal ans
            
            if ans:
                return
            
            if not node:
                return
            
            if node.val == val:
                ans = node
                return
            elif node.val > val:
                recr(node.left)
            else:
                recr(node.right)
        
        recr(root)
        return ans
            
            
