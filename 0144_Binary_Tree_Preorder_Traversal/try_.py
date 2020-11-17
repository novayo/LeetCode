# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # recursion
        if not root:
            return []
        
        def recr(node, ans):
            if not node:
                return
            
            ans.append(node.val)
            recr(node.left, ans)
            recr(node.right, ans)
        
        ans = []
        recr(root, ans)
        return ans
