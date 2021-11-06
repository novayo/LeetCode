# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i
        
        postorder_index = len(postorder) - 1
        def recr(i, j):
            nonlocal postorder_index
            
            if i > j:
                return
            
            root = TreeNode(postorder[postorder_index])
            postorder_index -= 1
            
            if i == j:
                return root
            
            root.right = recr(index[root.val]+1, j)
            root.left = recr(i, index[root.val]-1)
            
            return root
        
        return recr(0, len(inorder)-1)