# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def preorder(node, arr):
            if not node:
                arr.append(None)
                return
            
            arr.append(node.val)
            preorder(node.left, arr)
            preorder(node.right, arr)
        
        def postorder(node, arr):
            if not node:
                arr.append(None)
                return
            
            postorder(node.left, arr)
            postorder(node.right, arr)
            arr.append(node.val)
        
        p1 = []
        p2 = []
        preorder(root, p1)
        postorder(root, p2)
        
        p2 = p2[::-1]
        for i in range(len(p1)):
            if p1[i] != p2[i]:
                return False
        
        return True
        
