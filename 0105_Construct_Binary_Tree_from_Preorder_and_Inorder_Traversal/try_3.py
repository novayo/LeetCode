# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_preorder = 0
        index_map = {}
        for i in range(len(inorder)):
            index_map[inorder[i]] = i
        
        
        def recr(left, right):
            nonlocal index_preorder
            
            if left > right:
                return None
            
            target = preorder[index_preorder]
            index_inorder = index_map[target]
            
            root = TreeNode(target)
            index_preorder += 1
            
            root.left = recr(left, index_inorder-1)
            root.right = recr(index_inorder+1, right)
            
            return root
        
        return recr(0, len(inorder)-1)