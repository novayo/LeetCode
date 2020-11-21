# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # recr
        
        def recr(node, ans):
            if not node:
                return
            
            recr(node.left, ans)
            recr(node.right, ans)
            ans.append(node.val)
        
        ans = []
        recr(root, ans)
        return ans