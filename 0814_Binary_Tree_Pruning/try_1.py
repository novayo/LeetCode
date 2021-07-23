# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def recr(root):
            if not root:
                return False
            
            left = recr(root.left)
            right = recr(root.right)

            if not left:
                root.left = None

            if not right:
                root.right = None

            return root.val != 0 or left or right
        
        newRoot = TreeNode(1)
        newRoot.right = root
        recr(newRoot)
        return newRoot.right
