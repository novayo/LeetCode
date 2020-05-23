# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(node):
            nonlocal ans
            if not node:
                return
            
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        
        ans = []
        inorder(root)
        return ans
